import logging

from playwright.async_api import Page

from framework.ui.elements.button import Button
from framework.ui.elements.frame import Frame
from framework.ui.pages.base_page import BasePage

logger = logging.getLogger(__name__)


class AccuWeatherMainPage(BasePage):
    def __init__(self, page: Page):
        search_bar = page.locator(".search-input")
        super().__init__(page, search_bar, "AccuWeather Main Page")

        self._consent_data_usage_btn = Button(page=page, locator=".banner-button:has-text('I Understand')",
                                              name="I Understand Button")
        self.close_ad_frame = Frame(
            page=page,
            locator=".close-ad",
            name="Close Ad Button"
        )

    def accept_consent_data_usage(self) -> None:
        """
        Accept the consent data usage prompt by clicking the 'I Understand' button.
        """
        logger.debug("Accepting consent data usage prompt.")
        self._consent_data_usage_btn.click()
        logger.info("Consent data usage accepted.")

    # def dismiss_ad_if_present(self, timeout: int = 5000):
    #     """
    #     Dismisses ad using Frame element if present
    #     """
    #     try:
    #         # Wait for frame to be visible
    #         self.close_ad_frame.state.wait_for_displayed(timeout=timeout)
    #         logger.info("Ad frame detected - attempting to dismiss")
    #         # Click the close ad button
    #         self.close_ad_frame.click()
    #
    #     except Exception as e:
    #         logger.debug(f"No ad appeared or error dismissing: {str(e)}")

    def dismiss_ad_if_present(self):
        if self.close_ad_frame.state.is_visible():
            logger.info("Ad frame detected")
            frame_context = self.close_ad_frame.switch_to_frame()
            frame_context.locator(self.close_ad_frame.locator).click()
            self.close_ad_frame.state.is_displayed_in_viewport()
