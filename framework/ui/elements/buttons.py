class Buttons:
    def __init__(self, page: Page, selector: str, name: str):
        self.page = page
        self.locator = page.locator(selector)
        self.name = name

    def count(self):
        return self.locator.count()

    def get_texts(self):
        return [self.locator.nth(i).inner_text() for i in range(self.count())]

    def click_first(self):
        if self.count() > 0:
            self.locator.nth(0).click()
