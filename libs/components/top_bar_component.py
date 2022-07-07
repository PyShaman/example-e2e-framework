from selene.support.conditions import be
from selene.support.jquery_style_selectors import s

from libs.locators.top_bar_locators import TopBarLocators


class TopBarComponent(TopBarLocators):
    """
    Ta klasa powinna zawierac wszystkie metody, ktore sie odnosza do elementow gornej listwy (Logo, Marketplace, znak
    zapytania dzwonek, awatar z tekstem 'Welcome Paul'
    """

    def return_avatar_text(self):
        s(self.TOP_BAR_AVATAR).should(be.visible, timeout=20)
        return s(self.TOP_BAR_AVATAR).text
