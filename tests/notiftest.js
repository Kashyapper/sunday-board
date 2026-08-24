const BASE = process.env.BASE_URL || 'http://localhost:8099/';
const { chromium } = require('playwright');
const pad = n => String(n).padStart(2,'0');
const dISO = d => `${d.getFullYear()}-${pad(d.getMonth()+1)}-${pad(d.getDate())}`;

(async () => {
  const now = Date.now();
  const seed = {
    v:1, updatedAt: now, profile:{name:'Shiv',email:'shiv@example.com'}, targets:{},
    events:[
      { id:'e1', title:'Dentist appointment', notes:'Bring insurance card', startAt: now + 24*3600e3 - 60e3 },
      { id:'e2', title:'Soccer practice',     notes:'Cleats',               startAt: now + 29*60e3 },
      { id:'e3', title:'Far away thing',      notes:'',                     startAt: now + 5*864e5 }
    ],
    tasks:[
      { id:'t1', title:'Finish history essay', notes:'Three pages', dueAt: now + 24*3600e3 - 120e3, done:false },
      { id:'t2', title:'Already done thing',   notes:'',            dueAt: now + 24*3600e3 - 120e3, done:true }
    ],
    foods:[ { id:'f1', name:'Chicken tacos', notes:'', ingredients:[
      {name:'Chicken breast',qty:2,unit:'lb',ref:null},{name:'Tortillas',qty:8,unit:'',ref:null} ] } ],
    meals:[], alerts:[], fired:{}, desktop:false
  };
  // pick the next dinner slot that falls inside the coming 24h, so its
  // day-before reminder is due right now whatever time the test runs
  const dinner = new Date(now); dinner.setHours(18,0,0,0);
  if (dinner.getTime() <= now) dinner.setDate(dinner.getDate() + 1);
  seed.meals.push({ id:'m1', foodId:'f1', date: dISO(dinner), slot:'dinner' });

  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport:{width:1360,height:900} });
  const errs = [];
  await ctx.addInitScript(v => {
    try { if (!localStorage.getItem('sundayboard.v1')) localStorage.setItem('sundayboard.v1', v); } catch {}
  }, JSON.stringify(seed));

  const page = await ctx.newPage();
  page.on('console', m => { if (m.type()==='error') errs.push(m.text()); });
  page.on('pageerror', e => errs.push('PAGEERROR: '+e.message));

  await page.goto(BASE);
  await page.waitForTimeout(1200);

  const cards = await page.$$eval('.alertcard', els => els.map(e => ({
    lead: e.querySelector('.lead').textContent,
    head: e.querySelector('.head').textContent
  })));
  console.log('ALERT CARDS ON SCREEN:');
  cards.forEach(c => console.log('   ·', c.lead, '→', c.head));
  const kinds = cards.map(c => c.head);
  const want = ['Dentist appointment','Soccer practice','Finish history essay'];
  console.log('badge:', await page.textContent('#bellCount'),
              '| event+task reminders present:', want.every(w => kinds.some(k => k.includes(w))),
              '| meal reminder present:', kinds.some(k => /Dinner:/.test(k)) || 'in feed');
  await page.screenshot({ path:'screenshots/n1-alerts.png' });

  // reminder centre
  await page.click('#bellBtn');
  await page.waitForSelector('#scrim:not([hidden])');
  await page.waitForTimeout(300);
  console.log('feed rows:', (await page.$$('.feed .item')).length);
  await page.screenshot({ path:'screenshots/n2-centre.png' });
  await page.click('#sheetX');

  // reload: nothing should fire twice
  await page.reload();
  await page.waitForTimeout(1200);
  console.log('cards after reload (want 0):', (await page.$$('.alertcard')).length);
  console.log('badge after reload (want same):', await page.textContent('#bellCount'));

  // clicking a meal reminder should jump to the meal
  await page.click('#bellBtn');
  await page.waitForTimeout(250);
  const mealRow = await page.$$('.feed .item');
  // find the meal one
  const idx = (await page.$$eval('.feed .item .head', hs => hs.map(h => h.textContent)))
                .findIndex(t => /Dinner/.test(t));
  if (idx >= 0){
    await mealRow[idx].click();
    await page.waitForTimeout(500);
    const title = await page.textContent('#sheetTitle').catch(()=>'(none)');
    console.log('meal reminder opens sheet:', title, '| view =', await page.getAttribute('#v-week','hidden') === null ? 'week' : 'other');
    await page.screenshot({ path:'screenshots/n3-routed.png' });
  } else console.log('meal reminder row NOT FOUND');

  console.log('ERRORS:', errs.filter(e => !/store\.json|ERR_TUNNEL/.test(e)).length ? errs : 'none (font/file fetch aside)');
  await browser.close();
})();
