from selene.support.conditions import be
from selene.support.jquery_style_selectors import s

from libs.locators.login_page_locators import LoginPageLocators


class LoginPage(LoginPageLocators):
    """
    Ta klasa powinna zawierac wszystkie metody, ktore definiuja operacje na lokatorach
    """

    def return_login_form_title(self):
        s(self.LOGIN_PAGE_LOGIN_PANEL_HEADING).should(be.visible, timeout=20)
        return s(self.LOGIN_PAGE_LOGIN_PANEL_HEADING).text

    def fill_username_and_password(self, username, password):
        s(self.LOGIN_PAGE_USERNAME_INPUT).send_keys(username)
        s(self.LOGIN_PAGE_PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        s(self.LOGIN_PAGE_LOGIN_BUTTON).click()
