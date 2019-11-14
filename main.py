from selenium import webdriver
import time



def list_thumbnails(query, driver):
    driver.get("https://www.images.google.com")

    # search_bar = driver.find_elements_by_tag_name("input")
    search_bar = driver.find_element_by_xpath("//input[contains(@title,'Search')]")
    search_bar.send_keys(query)
    search_bar.send_keys(u'\ue007')

    search_results = driver.find_element_by_id('search')

    imgs = search_results.find_elements_by_tag_name('img')

    for img in imgs:
        print(img.get_attribute('data-src'))

    print("---END---")

    for img in imgs:
        link = img.find_elements_by_xpath('..')[0]
        link.click()

        full_images = driver.find_elements_by_class_name('irc_mi')
        print(full_images)
        print(full_images[1].get_attribute('src'))
        # print(full_images[1].get_attribute('outerHTML'))
        time.sleep(1)


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
# options.add_argument('window-size=800x841')
# options.add_argument('headless')

driver = webdriver.Chrome(options=options)


list_thumbnails('LendingTree', driver)

# Iterate through <a> tags

# links = search_results.find_elements_by_tag_name('a')

# print(links[0].get_attribute('innerHTML'))

# for i in range(min(3,len(links)-1)):
#     print(links[i].get_attribute('innerHTML'))

# print(driver.page_source)



# driver.close()
