const BASE = process.env.BASE_URL || 'http://localhost:8099/';
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport:{width:1360,height:900} });
  const page = await ctx.newPage();
  const errs = [];
  page.on('console', m => { if (m.type()==='error') errs.push(m.text()); });
  page.on('pageerror', e => errs.push('PAGEERROR: '+e.message));
  await page.goto(BASE);
  await page.waitForTimeout(700);
  if (await page.isVisible('#gate')){
    await page.fill('#gName','Shiv'); await page.fill('#gEmail','shiv@example.com');
    await page.click('#gateGo'); await page.waitForTimeout(700);
  }
  await page.screenshot({ path:'screenshots/a1-calendar.png' });

  // event
  await page.click('#mAdd');
  await page.waitForSelector('#scrim:not([hidden])');
  await page.fill('#sTitle','Soccer practice');
  const d=new Date(); d.setDate(d.getDate()+3);
  const iso=`${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`;
  await page.fill('#sDate',iso); await page.fill('#sTime','16:30');
  await page.fill('#sNotes','Bring cleats');
  await page.click('#sheetFoot .btn.solid');
  await page.waitForTimeout(400);

  // tasks
  await page.click('#nav button[data-v=tasks]');
  await page.fill('#tTitle','Finish history essay');
  await page.fill('#tDate',iso); await page.fill('#tNotes','Three pages, two sources');
  await page.click('#taskForm button[type=submit]');
  await page.waitForTimeout(300);
  await page.fill('#tTitle','Renew library books');
  await page.click('#taskForm button[type=submit]');
  await page.waitForTimeout(300);
  await page.screenshot({ path:'screenshots/a2-tasks.png' });

  // foods — built from the ingredient library
  await page.click('#nav button[data-v=pantry]');
  await page.waitForTimeout(400);
  const addFromLib = async (term) => {
    await page.fill('#ingSearch', term);
    await page.waitForTimeout(280);
    await page.click('#ingResults .pick .plus');
    await page.waitForTimeout(220);
  };
  await page.fill('#fName','Chicken tacos'); await page.fill('#fNotes','About 20 minutes');
  await addFromLib('chicken breast'); await addFromLib('flour tortilla'); await addFromLib('cheddar');
  await page.click('#fSave'); await page.waitForTimeout(500);
  await page.fill('#fName','Veggie stir fry');
  await addFromLib('brown rice'); await addFromLib('broccoli'); await addFromLib('cheddar');
  await page.click('#fSave'); await page.waitForTimeout(500);
  await page.screenshot({ path:'screenshots/a3-foods.png' });

  // meal plan drag & drop
  await page.click('#nav button[data-v=week]');
  await page.waitForSelector('.dish');
  await page.waitForTimeout(300);
  await page.locator('.dish').first().dragTo(page.locator('.slot').nth(17)); // dinner, col 3
  await page.waitForTimeout(500);
  await page.locator('.dish').nth(1).dragTo(page.locator('.slot').nth(8));   // lunch, col 1
  await page.waitForTimeout(500);
  await page.locator('.dish').first().dragTo(page.locator('.slot').nth(19)); // dinner again -> qty doubles
  await page.waitForTimeout(500);
  console.log('served chips:', (await page.$$('.served')).length);
  await page.screenshot({ path:'screenshots/a4-week.png' });

  // ingredient popup
  await page.click('.served span');
  await page.waitForSelector('#scrim:not([hidden])');
  await page.waitForTimeout(300);
  await page.screenshot({ path:'screenshots/a5-ingredients.png' });
  await page.click('#sheetX');

  // the grocery list now lives on its own page (covered by carttest.js)
  await page.click('#wShop'); await page.waitForTimeout(500);
  console.log('shopping page opens from meal plan:', await page.isVisible('#v-shop'),
              '| to buy:', (await page.$$('#buyList .gitem')).length, 'items');

  // back to calendar
  await page.click('#nav button[data-v=month]');
  await page.waitForTimeout(500);
  await page.screenshot({ path:'screenshots/a7-calendar-full.png' });
  console.log('calendar entries:', (await page.$$('.month .ent')).length);
  console.log('upcoming rows:', (await page.$$('#upcoming .up')).length);

  // persistence across reload
  await page.reload(); await page.waitForTimeout(900);
  console.log('after reload — entries:', (await page.$$('.month .ent')).length,
              '| sync:', await page.textContent('#syncText'));

  // dark theme
  const dctx = await browser.newContext({ colorScheme:'dark', viewport:{width:1360,height:900} });
  const dp = await dctx.newPage();
  await dp.goto(BASE);
  await dp.waitForTimeout(600);
  if (await dp.isVisible('#gate')){ await dp.fill('#gName','Shiv'); await dp.click('#gateGo'); await dp.waitForTimeout(600); }
  await dp.click('#nav button[data-v=week]');
  await dp.waitForTimeout(600);
  await dp.screenshot({ path:'screenshots/a8-dark.png' });

  // mobile
  const mctx = await browser.newContext({ viewport:{width:390,height:844} });
  const mp = await mctx.newPage();
  await mp.goto(BASE);
  await mp.waitForTimeout(600);
  if (await mp.isVisible('#gate')){ await mp.fill('#gName','Shiv'); await mp.click('#gateGo'); await mp.waitForTimeout(600); }
  await mp.screenshot({ path:'screenshots/a9-mobile.png' });

  console.log('ERRORS:', errs.length ? errs : 'none');
  await browser.close();
})();
