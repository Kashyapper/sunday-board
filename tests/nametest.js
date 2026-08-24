const BASE = process.env.BASE_URL || 'http://localhost:8099/';
const { chromium } = require('playwright');
const URL = BASE;
(async () => {
  const b = await chromium.launch();
  for (const [w,h,tag] of [[1440,980,'desk'],[390,844,'phone']]){
    const c = await b.newContext({ viewport:{width:w,height:h} });
    const p = await c.newPage();
    await p.goto(URL); await p.waitForTimeout(700);
    await p.fill('#gName','Shiv'); await p.click('#gateGo'); await p.waitForTimeout(700);

    await p.click('#nav button[data-v=tasks]'); await p.waitForTimeout(300);
    for (const t of ['Finish history essay','Maths homework','Call the dentist about the appointment']){
      await p.fill('#tTitle', t);
      await p.click('#taskForm button[type=submit]');
      await p.waitForTimeout(250);
    }
    await p.click('#nav button[data-v=month]'); await p.waitForTimeout(600);

    const chips = await p.$$eval('.month .ent.tk', els => els.map(e => ({
      text: e.textContent.trim(),
      w: Math.round(e.getBoundingClientRect().width),
      clipped: e.scrollWidth > e.clientWidth + 1
    })));
    console.log(`\n--- ${tag} (${w}px) ---`);
    chips.forEach(c => console.log(`  cell chip ${String(c.w).padStart(3)}px  clipped=${c.clipped}  "${c.text}"`));
    const cell = await p.$eval('.day', e => Math.round(e.getBoundingClientRect().width));
    console.log('  day cell width:', cell + 'px');
    await p.screenshot({ path:`screenshots/n-${tag}.png` });
    await c.close();
  }
  await b.close();
})();
