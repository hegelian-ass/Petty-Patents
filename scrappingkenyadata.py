from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time


def scrape_utility_models(page_num=3):
    """
    Scrape utility models data from IP Database
    """

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')

    driver = webdriver.Chrome(options=chrome_options)

    try:
        url = f'https://ipdatabase.cipit.org/more/search/results/utility_models?page={page_num}'
        print(f"Accessing: {url}")
        driver.get(url)


        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        time.sleep(2)

        results = []

        selectors = [
            ".result-item",
            ".search-result",
            "tr[class*='result']",
            ".utility-model",
            "tbody tr"
        ]

        items = []
        for selector in selectors:
            try:
                items = driver.find_elements(By.CSS_SELECTOR, selector)
                if items:
                    print(f"Found {len(items)} items using selector: {selector}")
                    break
            except:
                continue

        if not items:

            print("No items found with common selectors. Getting page source...")
            print("\nPage title:", driver.title)
            print("\nFirst 500 characters of body:")
            body = driver.find_element(By.TAG_NAME, "body")
            print(body.text[:500])

            
            with open('page_source.html', 'w', encoding='utf-8') as f:
                f.write(driver.page_source)
            print("\nFull page source saved to 'page_source.html'")

        else:
            for item in items:
                try:

                    data = {
                        'text': item.text,
                        'html': item.get_attribute('innerHTML')[:200]  # First 200 chars
                    }
                    results.append(data)
                except Exception as e:
                    print(f"Error extracting item: {e}")
                    continue

            
            if results:
                df = pd.DataFrame(results)
                df.to_csv('utility_models_data.csv', index=False)
                print(f"\nScraped {len(results)} items")
                print("\nFirst few results:")
                print(df.head())

    except Exception as e:
        print(f"Error occurred: {e}")

        try:
            driver.save_screenshot('error_screenshot.png')
            print("Screenshot saved as 'error_screenshot.png'")
        except:
            pass

    finally:
        driver.quit()
        print("\nBrowser closed")


if __name__ == "__main__":

    scrape_utility_models(page_num=3)
