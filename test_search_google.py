from selene import have, browser


def test_search_1(browser_set_up):
    browser.open("https://www.google.com/")
    browser.element('[name="q"]').type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))


def test_search_2(browser_set_up):
    browser.open("https://www.google.com/")
    browser.element('[name="q"]').type('0435968092435#%$#$%^#$%^$#%^').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
    print('По данному запросу ничего не найдено')