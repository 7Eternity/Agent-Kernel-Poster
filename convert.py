import asyncio
from playwright.async_api import async_playwright
import os


async def html_to_pdf(html_file, output_pdf):
    async with async_playwright() as p:
        # 使用本地 Chrome 渲染效果最好
        browser = await p.chromium.launch(channel="chrome")

        # 核心设置：将视口设置为海报的像素尺寸
        # 780mm 约等于 2948px (以 96DPI 计算)
        # 这里直接设置一个足够大的视口，避免滚动条和截断
        context = await browser.new_context(viewport={"width": 2948, "height": 7559}, device_scale_factor=1)
        page = await context.new_page()

        file_path = "file://" + os.path.abspath(html_file)
        print(f"正在加载并精确对齐尺寸...")

        await page.goto(file_path, wait_until="networkidle")

        # 强制等待所有资源完全稳定
        await page.wait_for_timeout(2000)

        await page.pdf(
            path=output_pdf,
            width="780mm",
            height="2000mm",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
            scale=1,  # 必须是 1
            prefer_css_page_size=True,  # 优先使用 CSS 定义的尺寸
        )

        await browser.close()
        print(f"完美对齐的 PDF 已生成: {output_pdf}")


if __name__ == "__main__":
    asyncio.run(html_to_pdf("poster.html", "Agent_Kernel_Final_78x200.pdf"))
