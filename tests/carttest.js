const BASE = process.env.BASE_URL || 'http://localhost:8099/';
const { chromium } = require('playwright');
const URL = BASE;
const buy  = p => p.$$eval('#buyList .gitem .gname',  e => e.map(x => x.textContent.trim()));
const cart = p => p.$$eval('#cartList .gitem .gname', e => e.map(x => x.textContent.trim()));

(async () => {
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport:{width:1420,height:980} });
  const page = await ctx.newPage();
  const errs = [];
  page.on('pageerror', e => errs.push('PAGEERROR: ' + e.message));
  page.on('console', m => { if (m.type()==='error' && !/store\.json|ERR_TUNNEL|404/.test(m.text())) errs.push(m.text()); });

  await page.goto(URL); await page.waitForTimeout(700);
  await page.fill('#gName','Shiv'); await page.click('#gateGo');
  await page.waitForSelector('#shell:not([hidden])');

  // build two foods from the library
  await page.click('#nav button[data-v=pantry]'); await page.waitForTimeout(400);
  const add = async term => { await page.fill('#ingSearch', term); await page.waitForTimeout(280); await page.click('#ingResults .pick .plus'); await page.waitForTimeout(200); };
  await page.fill('#fName','Dal tadka'); await add('toor dal'); await add('ghee'); await add('onion');
  await page.click('#fSave'); await page.waitForTimeout(400);
  await page.fill('#fName','Palak paneer'); await add('spinach'); await add('paneer'); await add('onion');
  await page.click('#fSave'); await page.waitForTimeout(400);

  // plan them
  await page.click('#nav button[data-v=week]'); await page.waitForTimeout(500);
  await page.locator('.dish').first().dragTo(page.locator('.slot').nth(15));
  await page.waitForTimeout(400);
  await page.locator('.dish').nth(1).dragTo(page.locator('.slot').nth(9));
  await page.waitForTimeout(400);

  // the meal plan's button should land on the shopping page
  await page.click('#wShop'); await page.waitForTimeout(500);
  console.log('shopping page visible:', await page.isVisible('#v-shop'), '| week:', await page.textContent('#shopWeek'));
  console.log('to buy :', await buy(page));
  console.log('cart   :', await cart(page));
  await page.screenshot({ path:'screenshots/c1-shop.png' });

  // DRAG an item into the cart
  const first = await page.$$eval('#buyList .gitem .gname', e => e[0].textContent.trim());
  await page.locator('#buyList .gitem').first().dragTo(page.locator('#cartList'));
  await page.waitForTimeout(450);
  console.log('\nafter dragging "%s":', first);
  console.log('to buy :', await buy(page));
  console.log('cart   :', await cart(page));
  console.log('nav badge:', await page.textContent('#cartCount'), '| hidden:', await page.getAttribute('#cartCount','hidden') !== null);

  // click the + on another
  await page.click('#buyList .gitem .gbtn'); await page.waitForTimeout(400);
  console.log('\nafter + button — cart:', await cart(page));

  // drag one back out
  await page.locator('#cartList .gitem').first().dragTo(page.locator('#buyList'));
  await page.waitForTimeout(450);
  console.log('after dragging back — to buy:', await buy(page));
  console.log('                      cart  :', await cart(page));

  // add something of your own
  await page.fill('#ownName','Coffee beans'); await page.fill('#ownAmt','250 g');
  await page.click('#ownForm button[type=submit]'); await page.waitForTimeout(400);
  console.log('\nafter own item — cart:', await cart(page));

  // tick one off
  await page.click('#cartList .gitem input[type=checkbox]'); await page.waitForTimeout(400);
  console.log('tally:', await page.textContent('#cartTally'), '| badge:', await page.textContent('#cartCount'));
  await page.screenshot({ path:'screenshots/c2-cart.png' });

  // add everything
  await page.click('#cartAll'); await page.waitForTimeout(500);
  console.log('\nafter "Add everything" — to buy:', await buy(page));
  console.log('                          cart :', (await cart(page)).length, 'items');

  // survives a reload
  await page.reload(); await page.waitForTimeout(1400);
  await page.click('#nav button[data-v=shop]'); await page.waitForTimeout(500);
  console.log('after reload — cart:', (await cart(page)).length, 'items | badge:', await page.textContent('#cartCount'));

  // empty it
  await page.click('#cartClear'); await page.waitForSelector('#scrim:not([hidden])'); await page.waitForTimeout(300);
  await page.click('#sheetFoot .btn.warn'); await page.waitForTimeout(500);
  console.log('after empty  — cart:', await cart(page), '| to buy:', (await buy(page)).length, 'items');
  console.log('badge hidden:', await page.getAttribute('#cartCount','hidden') !== null);

  // mobile + dark
  const m = await browser.newContext({ viewport:{width:390,height:844} });
  const mp = await m.newPage(); await mp.goto(URL); await mp.waitForTimeout(600);
  await mp.fill('#gName','Shiv'); await mp.click('#gateGo'); await mp.waitForTimeout(600);
  await mp.click('#nav button[data-v=shop]'); await mp.waitForTimeout(500);
  await mp.screenshot({ path:'screenshots/c3-mobile.png' });

  console.log('\nERRORS:', errs.length ? errs : 'none');
  await browser.close();
})();
