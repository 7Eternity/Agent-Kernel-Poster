// export.js
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  await page.goto('file:///绝对路径/poster.html', {
    waitUntil: 'networkidle'
  });

  await page.pdf({
    path: 'Agent-Kernel-poster.pdf',
    width: '80cm',
    height: '200cm',
    printBackground: true
  });

  await page.screenshot({
    path: 'Agent-Kernel-poster.png',
    fullPage: true
  });

  await browser.close();
})();
