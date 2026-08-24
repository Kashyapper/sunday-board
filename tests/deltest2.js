const BASE = process.env.BASE_URL || 'http://localhost:8099/';
const { chromium } = require('playwright');
(async () => {
  const now = Date.now();
  const seed = {
    v:1, updatedAt:now, profile:{name:'Shiv',email:'s@e.com'}, targets:{},
    events:[], foods:[], meals:[], alerts:[], fired:{}, desktop:false,
    tasks:[
      { id:'t1', title:'Finish history essay', notes:'Three pages', dueAt: now + 24*3600e3 - 60e3, done:false },
      { id:'t2', title:'Renew library books',  notes:'',            dueAt: now + 24*3600e3 - 90e3, done:false }
    ]
  };
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport:{width:1400,height:950} });
  await ctx.addInitScript(v => { try { if(!localStorage.getItem('sundayboard.v1')) localStorage.setItem('sundayboard.v1', v); } catch {} }, JSON.stringify(seed));
  const p = await ctx.newPage();
  p.on('pageerror', e => console.log('PAGEERROR:', e.message));
  await p.goto(BASE); await p.waitForTimeout(1500);

  console.log('alert cards on screen:', await p.$$eval('.alertcard .head', e => e.map(x => x.textContent)));
  console.log('reminder badge       :', await p.textContent('#bellCount'));

  // now delete BOTH tasks
  await p.click('#nav button[data-v=tasks]'); await p.waitForTimeout(400);
  for (let i = 0; i < 2; i++){
    const r = await p.$$('#taskRows .row');
    if (!r.length) break;
    await (await r[0].$('[data-a=del]')).click();
    await p.waitForTimeout(400);
  }
  console.log('task list after delete:', await p.$$eval('#taskRows .row .name', e => e.map(x => x.textContent)).catch(()=>[]),
              '| empty msg:', await p.textContent('#taskRows'));

  // ...and look at what the Reminders panel still claims
  console.log('\nbadge after deleting :', await p.textContent('#bellCount'));
  console.log('alert cards still up :', await p.$$eval('.alertcard .head', e => e.map(x => x.textContent)));
  await p.click('#bellBtn'); await p.waitForSelector('#scrim:not([hidden])'); await p.waitForTimeout(300);
  console.log('reminders feed shows :', await p.$$eval('.feed .item .head', e => e.map(x => x.textContent)));
  await p.screenshot({ path:'screenshots/z1-ghost-reminders.png' });

  // clicking a ghost reminder — what happens?
  const items = await p.$$('.feed .item');
  if (items.length){
    await items[0].click(); await p.waitForTimeout(500);
    console.log('after clicking ghost -> tasks view visible:', await p.isVisible('#v-tasks'));
  }
  await b.close();
})();
