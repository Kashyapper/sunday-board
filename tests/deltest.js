const BASE = process.env.BASE_URL || 'http://localhost:8099/';
const { chromium } = require('playwright');
const URL = BASE;
const names = p => p.$$eval('#taskRows .row .name', e => e.map(x => x.textContent.trim()));

(async () => {
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport:{width:1400,height:950} });
  const page = await ctx.newPage();
  const errs = [];
  page.on('pageerror', e => errs.push('PAGEERROR: ' + e.message));
  page.on('console', m => { if (m.type()==='error' && !/store\.json|ERR_TUNNEL/.test(m.text())) errs.push(m.text()); });

  await page.goto(URL); await page.waitForTimeout(700);
  await page.fill('#gName','Shiv'); await page.click('#gateGo');
  await page.waitForSelector('#shell:not([hidden])');

  await page.click('#nav button[data-v=tasks]'); await page.waitForTimeout(300);
  for (const t of ['Alpha task','Beta task','Gamma task']){
    await page.fill('#tTitle', t);
    await page.click('#taskForm button[type=submit]');
    await page.waitForTimeout(250);
  }
  console.log('after adding 3 :', await names(page));

  // delete the middle one with the ✕ button
  const rows = await page.$$('#taskRows .row');
  await (await rows[1].$('[data-a=del]')).click();
  await page.waitForTimeout(500);
  console.log('after deleting Beta:', await names(page));

  // does it survive a reload?
  await page.reload(); await page.waitForTimeout(1200);
  await page.click('#nav button[data-v=tasks]'); await page.waitForTimeout(400);
  console.log('after reload       :', await names(page));

  // delete from inside the edit sheet
  const r2 = await page.$$('#taskRows .row');
  await (await r2[0].$('[data-a=edit]')).click();
  await page.waitForSelector('#scrim:not([hidden])'); await page.waitForTimeout(300);
  await page.click('#sheetFoot .btn.warn');
  await page.waitForTimeout(500);
  console.log('after sheet-delete :', await names(page));

  // tick one done, switch to Done filter, delete there
  await page.fill('#tTitle','Delta task'); await page.click('#taskForm button[type=submit]');
  await page.waitForTimeout(300);
  await page.click('#taskRows .row [data-a=tog]'); await page.waitForTimeout(400);
  console.log('open list after tick:', await names(page));
  await page.click('#tFilter button[data-f=done]'); await page.waitForTimeout(300);
  console.log('done list          :', await names(page));
  const dr = await page.$$('#taskRows .row');
  if (dr.length){ await (await dr[0].$('[data-a=del]')).click(); await page.waitForTimeout(500); }
  console.log('done list after del:', await names(page));
  await page.click('#tFilter button[data-f=all]'); await page.waitForTimeout(300);
  console.log('all list           :', await names(page));

  // and does the calendar still show a deleted task?
  await page.click('#nav button[data-v=month]'); await page.waitForTimeout(500);
  console.log('calendar task chips:', await page.$$eval('.month .ent.tk', e => e.map(x => x.textContent.trim())));

  console.log('ERRORS:', errs.length ? errs : 'none');
  await browser.close();
})();
