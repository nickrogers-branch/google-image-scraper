from selenium import webdriver
import time
import urllib.request
import threading
import os



_home_directory = 'nicholasrogers'


def save_file_at_url(url, folder_name):
    try:
        file_name = url.rsplit('/', 1)[1]
        # response = urllib.request.urlopen(url)
        urllib.request.urlretrieve(url, '/Users/' + _home_directory + '/temp/google_images/' + folder_name + '/' + file_name)
    except Exception as e:
        print(e)


def load_images(query, folder_name, driver):
    # try:
    # except Exception as e:
    #     print(e)
    # finally:
    #     driver.close()
    driver.get("https://www.images.google.com")

    # search_bar = driver.find_elements_by_tag_name("input")
    search_bar = driver.find_element_by_xpath("//input[contains(@title,'Search')]")
    search_bar.send_keys(query)
    search_bar.send_keys(u'\ue007')

    search_results = driver.find_element_by_id('search')

    # Force more of the page to load.
    for i in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    imgs = search_results.find_elements_by_tag_name('img')
    print(len(imgs))

    i = 0

    urls = []

    for img in imgs:
        try:
            link = img.find_elements_by_xpath('..')[0]
            # Sometimes you'll need to use
            # imgs[0].click()
            # instead. Why? Because Google is dynamic and likes to be unpredictable
            # (actually don't have too much of an idea)
            link.click()

            full_images = driver.find_elements_by_class_name('irc_mi')
            # print(full_images)
            url = full_images[1].get_attribute('src')

            urls.append(url)

            img_save_thread = threading.Thread(target=save_file_at_url, args=(url,folder_name,))
            img_save_thread.start()

            # print(full_images[1].get_attribute('outerHTML'))

            if i > 19:
                break

            # i += 1

            time.sleep(0.2)

        except Exception as e:
            print(e)


options = webdriver.ChromeOptions()
options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
# options.add_argument('window-size=1197x952')
# options.add_argument('headless')

driver = webdriver.Chrome(options=options)

try:
    flower_names_file = open(os.getcwd() + '/flowers.txt')
    flower_name = flower_names_file.readline().strip().lower()

    while flower_name:
        print(flower_name)

        os.mkdir('/Users/' + _home_directory + '/temp/google_images/' + flower_name + '/')

        load_images(flower_name + ' flower', flower_name, driver)

        flower_name = flower_names_file.readline().strip().lower()

    # load_images('Aconitum flower', 'aconitum', driver)

except Exception as e:
    print(e)
finally:
    driver.close()
