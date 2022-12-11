from selenium import webdriver


def time_url(driver, url):
    driver.get(url)

    # Use the browser Navigation Timing API to get some numbers:
    # https://developer.mozilla.org/en-US/docs/Web/API/Navigation_timing_API
    navigation_start = driver.execute_script(
        "return window.performance.timing.navigationStart")
    dom_complete = driver.execute_script(
        "return window.performance.timing.domComplete")
    total_time = dom_complete - navigation_start

    print(f"Time {total_time}ms")


driver = webdriver.Safari()

try:
    url = "https://youtube.com"
    time_url(driver, url + '1')
    time_url(driver, url + '2')

finally:
    driver.close()