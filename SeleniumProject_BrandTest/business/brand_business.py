# coding=utf-8
from selenium import webdriver
from util.find_element import my_get_element

class BrandBusiness:
    def __init__(self,driver):
        self.driver = driver

    def click_one(self,key):
        element = my_get_element(self.driver, key)  # 点击品牌团
        element.click()
        return element

    def get_brand_expect_name(self,key):
        # 获取品牌专场的链接
        pop_brand_a_element = my_get_element(self.driver, key)
        a_url = pop_brand_a_element.get_attribute('href')
        # 获取打开链接的专场名字
        self.driver.get(a_url)
        brand_h1_element = my_get_element(self.driver, 'brand_h1')
        expect_name = brand_h1_element.get_attribute('textContent')
        return expect_name


    def get_brand_target_name(self,key):
        # 获取品牌专场的链接
        pop_brand_a_element = my_get_element(self.driver, key)
        a_url = pop_brand_a_element.get_attribute('href')
        # 获取打开链接的专场名字
        self.driver.get(a_url)
        brand_h1_element = my_get_element(self.driver, 'brand_h1')
        expect_name = brand_h1_element.get_attribute('textContent')
        return expect_name

    def get_text_from_content(self,key):
        element = my_get_element(self.driver, key)
        text = element.get_attribute('textContent').replace(' ', '').strip()
        return text

    def get_text_from_img(self,key):
        element = my_get_element(self.driver, key)
        text = element.get_attribute('alt')[:-2]
        return text

    def open_url_get_element(self,url_key,target_key):
        # 获取品牌专场的链接
        url_element = my_get_element(self.driver, url_key)
        url = url_element.get_attribute('href')
        # 获取打开链接的专场名字
        self.driver.get(url)
        element = my_get_element(self.driver, target_key)
        return element

    def get_element_location(self,key):
        element = my_get_element(self.driver, key)
        return element.location

    def get_strip_text(self,element):
        return element.get_attribute('textContent').replace(' ', '').strip()