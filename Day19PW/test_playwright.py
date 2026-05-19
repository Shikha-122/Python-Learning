from playwright.sync_api import Page,expect

def test_verifyPageUrl(page:Page):
    page.goto('https://www.wikipedia.org/') #passing url

    myurl =page.url
    print('Url of the page',myurl)

    expect(page).to_have_url('https://www.wikipedia.org/') #expected url


def test_verifyTitle(page:Page):
    page.goto('https://www.wikipedia.org/')
    pagetitle=page.title()
    print('Title of the page:',pagetitle)
    expect(page).to_have_title('Wikipedia')