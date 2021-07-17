import pytest
import allure

from fragments.main_page_fragments.search_fragment.search_steps import SearchSteps


@allure.epic('WEB-auto')
@allure.feature('Поиск')
class TestSearch:

    @pytest.mark.desktop
    @allure.title('Поиск и переход на детальную страницу товара с плашкой "Только по рецепту"')
    def test_search_product_recipe_strict(self, browser):
        page = SearchSteps(browser)
        page.open()
        page.accept_region()
        page.fill_search_input('Фенибут')
        page.click_search_btn()
        page.go_to_detail_product_recipe_strict()


@allure.epic('WEB-auto')
@allure.feature('Поиск')
class TestSearchMobile:

    @pytest.mark.mobile
    @allure.title('Поиск и переход на детальную страницу товара с плашкой "Только по рецепту" в мобильной версии')
    def test_mobile_search_product_recipe_strict(self, browser):
        page = SearchSteps(browser)
        page.open()
        page.accept_region()
        page.close_notification()
        page.fill_search_input('Фенибут')
        page.click_search_btn()
        page.go_to_detail_product_recipe_strict()