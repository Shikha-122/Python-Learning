# from playwright.sync_api import Page,expect
import pytest
from playwright.async_api import async_playwright, Page,expect

@pytest.mark.asyncio
async def test_verifyPageUrl():
    async with async_playwright() as p:
        browser=await p.chromium.launch()
        mypage = await browser.new_page()
        await mypage.goto('https://www.wikipedia.org/')

        await expect(mypage).to_have_url('https://www.wikipedia.org/') #expected url


