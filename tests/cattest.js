const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const errs=[];
  const p = await (await b.newContext({viewport:{width:1440,height:1000}})).newPage();
  p.on('pageerror', e=>errs.push('PAGEERROR: '+e.message));
  p.on('console', m=>{ if(m.type()==='error'&&!/store|TUNNEL|404/.test(m.text())) errs.push(m.text()); });
  await p.goto((process.env.BASE_URL || 'http://localhost:8099/')); await p.waitForTimeout(700);
  await p.fill('#gName','Shiv'); await p.click('#gateGo'); await p.waitForSelector('#shell:not([hidden])');
  await p.click('#nav button[data-v=lib]'); await p.waitForTimeout(600);

  console.log('tab:', await p.textContent('#libTabs .tab.on'), '|', await p.textContent('#shelfCount'));
  console.log('aisles:', (await p.$$eval('.shelflist .aisle', a=>a.map(x=>x.textContent))).join(' | '));

  // browse a shelf
  await p.click('.shelflist .shelf:has-text("Leaves & greens")'); await p.waitForTimeout(500);
  console.log('\nLeaves & greens:', await p.textContent('#libTally'));
  console.log('rows:', (await p.$$eval('#libRows .pick b', b=>b.slice(0,6).map(x=>x.textContent.trim()))).join(' · '));

  // add to cart from the shelf
  await p.$eval('#libRows .pick .acts .plus:last-child', e=>e.click()); await p.waitForTimeout(400);
  console.log('cart badge:', await p.textContent('#cartCount'));

  // use one in a dish
  await p.$eval('#libRows .pick .plus.dish', e=>e.click()); await p.waitForTimeout(700);
  console.log('jumped to:', await p.textContent('#nav button.on'));
  console.log('composer open:', !(await p.$eval('#foodCompose', e=>e.hidden)));
  console.log('recipe row:', await p.$$eval('#ingBox .ingitem input', i=>i.slice(0,1).map(x=>x.value)));
  await p.click('#fCancel'); await p.waitForTimeout(300);

  // repeat one from the shelf
  await p.click('#nav button[data-v=lib]'); await p.waitForTimeout(500);
  await p.$eval('#libRows .pick .plus.rep', e=>e.click()); await p.waitForTimeout(700);
  console.log('\nrepeat form prefilled with:', await p.inputValue('#rpName'), '| on page:', await p.textContent('#nav button.on'));
  await p.click('#rpSave'); await p.waitForTimeout(500);
  console.log('cart:', await p.$$eval('#cartList .gitem .gname', n=>n.map(x=>x.textContent)));

  // supplies + mine tabs
  await p.click('#nav button[data-v=lib]'); await p.waitForTimeout(400);
  await p.click('#libTabs .tab[data-t=sup]'); await p.waitForTimeout(500);
  console.log('\nsupplies:', await p.textContent('#shelfCount'), '| first shelf rows:',
    (await p.$$eval('.shelflist .shelf span', a=>a.slice(0,5).map(x=>x.textContent))).join(' · '));
  await p.click('#libTabs .tab[data-t=mine]'); await p.waitForTimeout(400);
  await p.fill('#myName','Amma\'s pickle masala'); await p.selectOption('#myCat','__new');
  await p.waitForTimeout(200); await p.fill('#myNewCat','Family recipes');
  await p.click('#mineForm button[type=submit]'); await p.waitForTimeout(500);
  console.log('mine shelves:', (await p.$$eval('.shelflist .shelf span', a=>a.map(x=>x.textContent))).join(' · '));
  console.log('mine rows:', await p.$$eval('#libRows .pick b', b=>b.map(x=>x.textContent.trim())));

  // it turns up in the recipe builder
  await p.click('#nav button[data-v=pantry]'); await p.waitForTimeout(300);
  await p.click('#newFoodBtn'); await p.waitForTimeout(500);
  await p.fill('#ingSearch','pickle masala'); await p.waitForTimeout(400);
  console.log('\nin the recipe library:', await p.$$eval('#ingResults .pick.mineown b', b=>b.map(x=>x.textContent)));

  // shopping still points at the library
  await p.click('#fCancel'); await p.click('#nav button[data-v=shop]'); await p.waitForTimeout(400);
  await p.click('#supBtn'); await p.waitForTimeout(500);
  console.log('“+ Add from the library” lands on:', await p.textContent('#nav button.on'));
  await p.screenshot({ path:'screenshots/lib3.png' });
  console.log('\nERRORS:', errs.length ? errs : 'none');
  await b.close();
})();
