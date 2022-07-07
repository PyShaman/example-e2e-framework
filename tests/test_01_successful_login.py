import pytest

from assertpy import assert_that

from libs.components.top_bar_component import TopBarComponent
from libs.pages.login_page import LoginPage


@pytest.mark.usefixtures("session_browser")
class TestSuccessfulLogin:

    def step_01_navigate_to_hrm_page(self, session_browser):
        session_browser.open_url("https://opensource-demo.orangehrmlive.com/")
        assert_that(LoginPage().return_login_form_title()).contains("LOGIN Panel")

    def step_02_fill_username_and_password(self):
        LoginPage().fill_username_and_password("Admin", "admin123")

    def step_03_click_login_button(self):
        LoginPage().click_login_button()

    def step_04_verify_that_user_is_logged_in(self):
        assert_that(TopBarComponent().return_avatar_text()).contains("Paul")
