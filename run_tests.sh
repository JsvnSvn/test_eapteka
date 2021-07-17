rm -r allure_results
pytest -s -v -m mobile --mode="mobile" --reruns 5 --alluredir=allure_results
allure serve allure_results