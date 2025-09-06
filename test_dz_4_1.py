from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def test_button_text_change_detailed():  # ← Правильное имя функции
    print("Запуск теста: Проверка изменения текста кнопки")

    # Настройка ChromeDriver через WebDriver Manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        print("1. Переходим на сайт Text Input...")
        driver.get("http://uitestingplayground.com/textinput")

        print("2. Находим поле ввода и кнопку...")
        input_field = driver.find_element(By.ID, "newButtonName")
        button = driver.find_element(By.ID, "updatingButton")

        # Запоминаем исходный текст кнопки
        original_text = button.text
        print(f"   Исходный текст кнопки: '{original_text}'")

        print("3. Вводим текст 'ITCH' в поле ввода...")
        input_field.clear()
        input_field.send_keys("ITCH")

        print("4. Нажимаем на синюю кнопку...")
        button.click()

        print("5. Ожидаем изменение текста кнопки...")
        # Ждем пока текст кнопки изменится
        WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element(By.ID, "updatingButton").text != original_text
        )

        # Проверяем конечный текст
        updated_button = driver.find_element(By.ID, "updatingButton")
        final_text = updated_button.text

        print(f"   Текст кнопки после изменения: '{final_text}'")

        # Проверяем утверждение
        assert final_text == "ITCH", f"Ожидалось 'ITCH', но получено '{final_text}'"

        print("✅ ТЕСТ ПРОЙДЕН УСПЕШНО!")
        print("   Текст кнопки успешно изменился на введенное значение")
        return True

    except AssertionError as e:
        print(f"❌ ТЕСТ НЕ ПРОЙДЕН: {e}")
        return False

    except Exception as e:
        print(f"❌ ПРОИЗОШЛА ОШИБКА: {e}")
        return False

    finally:
        driver.quit()
        print("Браузер закрыт.")



if __name__ == "__main__":
    test_button_text_change_detailed()