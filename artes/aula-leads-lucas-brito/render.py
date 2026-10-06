import sys, asyncio
from playwright.async_api import async_playwright
html, out, theme = sys.argv[1], sys.argv[2], (sys.argv[3] if len(sys.argv)>3 else "light")
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/opt/pw-browsers/chromium-1194/chrome-linux/chrome")
        pg = await b.new_page(viewport={"width":1080,"height":1350}, device_scale_factor=1)
        await pg.goto("file://"+html)
        if theme=="dark": await pg.evaluate("document.documentElement.classList.add('dark')")
        await pg.evaluate("document.fonts.ready")
        await pg.wait_for_timeout(300)
        await pg.screenshot(path=out, clip={"x":0,"y":0,"width":1080,"height":1350})
        await b.close()
asyncio.run(main())
