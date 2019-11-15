from selenium import webdriver
import time
import urllib.request



def list_thumbnails(query, driver):
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

    for i in range(3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    imgs = search_results.find_elements_by_tag_name('img')
    print(len(imgs))

    # for img in imgs:
    #     print(img.get_attribute('data-src'))

    # print("---END---")

    i = 0

    urls = []

    for img in imgs:
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

        # print(full_images[1].get_attribute('outerHTML'))

        if i == 9:
            break

        i += 1

        time.sleep(0.2)

    print(urls)

    for url in urls:
        try:
            file_name = url.rsplit('/', 1)[1]
            # response = urllib.request.urlopen(url)
            urllib.request.urlretrieve(url, '/users/nick.rogers/desktop/google_imgs/' + file_name)
        except Exception as e:
            print(e)



    # links = imgs[0].find_elements_by_xpath('..')
    # links[0].click()
    # # imgs[0].click()
    #
    # full_images = driver.find_elements_by_class_name('irc_mi')
    # print(full_images)
    # print(full_images[1].get_attribute('src'))
    # print(full_images[1].get_attribute('outerHTML'))


options = webdriver.ChromeOptions()
options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
# options.add_argument('window-size=1197x952')
# options.add_argument('headless')

driver = webdriver.Chrome(options=options)

try:

    list_thumbnails('LendingTree', driver)

except Exception as e:
    print(e)
finally:
    driver.close()

# Iterate through <a> tags

# links = search_results.find_elements_by_tag_name('a')

# print(links[0].get_attribute('innerHTML'))

# for i in range(min(3,len(links)-1)):
#     print(links[i].get_attribute('innerHTML'))

# print(driver.page_source)
