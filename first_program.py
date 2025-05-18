from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    message = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    message.click()

    # Ваш код, который заполняет обязательные поля
    x_element1 = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(int(x_element1))

    inputt = browser.find_element(By.CSS_SELECTOR,"#answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", inputt)
    inputt.send_keys(y)

#    browser.execute_script("return arguments[0].scrollIntoView(true);", x_element3)
#    x_element3.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
