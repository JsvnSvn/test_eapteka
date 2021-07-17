rm -r allure_results
pytest -s -v -m desktop --mode="desktop" --reruns 5 --alluredir=allure_results
allure serve allure_results