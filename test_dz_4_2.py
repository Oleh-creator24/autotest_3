from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


def test_image_loading_detailed():
    print("=" * 50)
    print("ТЕСТ: Проверка загрузки изображений")
    print("=" * 50)

    # Настройка ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Шаг 1: Перейдите на сайт
        print("1. 📍 Переходим на сайт Loading Images...")
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

        # Проверяем, что страница загрузилась
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        print("   ✅ Страница успешно загрузилась")

        # Шаг 2: Дождитесь загрузки всех изображений
        print("2. ⏳ Ожидаем загрузки изображений...")

        # Ждем исчезновения спиннера загрузки
        WebDriverWait(driver, 15).until(
            EC.invisibility_of_element_located((By.ID, "spinner"))
        )
        print("   ✅ Спиннер загрузки исчез")

        # Дополнительная проверка - ждем пока изображения станут видимыми
        WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#image-container img"))
        )
        print("   ✅ Все изображения стали видимыми")

        # Небольшая пауза для полной загрузки
        time.sleep(1)

        # Шаг 3: Получите значение атрибута alt у третьего изображения
        print("3. 🔍 Ищем третье изображение...")

        # Находим все изображения в контейнере
        images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
        print(f"   Найдено изображений: {len(images)}")

        # Проверяем, что есть хотя бы 3 изображения
        if len(images) < 3:
            print("❌ Недостаточно изображений на странице")
            return False

        # Берем третье изображение (индекс 2, так как индексация с 0)
        third_image = images[2]

        # Получаем все атрибуты для отладки
        alt_value = third_image.get_attribute("alt")
        src_value = third_image.get_attribute("src")

        print(f"   📸 Изображение: {src_value}")
        print(f"   🏷️  Атрибут alt: '{alt_value}'")

        # Шаг 4: Проверяем, что значение атрибута alt равно "award"
        print("4. ✅ Проверяем значение атрибута alt...")

        if alt_value == "award":
            print("   🎉 ТЕСТ ПРОЙДЕН УСПЕШНО!")
            print("   Атрибут alt третьего изображения равен 'award'")
            return True
        else:
            print(f"   ❌ ТЕСТ НЕ ПРОЙДЕН")
            print(f"   Ожидалось: 'award'")
            print(f"   Получено: '{alt_value}'")
            return False

    except Exception as e:
        print(f"❌ КРИТИЧЕСКАЯ ОШИБКА: {e}")
        return False

    finally:
        # Делаем скриншот перед закрытием
        try:
            driver.save_screenshot("test_result.png")
            print("   📸 Скриншот сохранен как 'test_result.png'")
        except:
            pass

        driver.quit()
        print("=" * 50)
        print("Браузер закрыт. Тест завершен.")
        print("=" * 50)


# Запуск теста
if __name__ == "__main__":
    test_image_loading_detailed()