# coding=utf-8
from selenium import webdriver
from util.find_element import my_get_element
import unittest, time, os
from business.brand_business import BrandBusiness

class SepcialPageTag(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'e:\webdrivers\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.get('https://www.zhe800.com')
        self.brand=BrandBusiness(self.driver)

    def tearDown(self):
        # time.sleep(2)
        self.driver.quit()

    # 品牌专场入口测试
    def test01_special_tag01(self):
        self.brand.click_one('brand_btn')  # 点击品牌团
        self.brand.click_one('list_a')  # 点击第一个分类按钮
        self.brand.click_one('list_pop_a')  # 点击第一个热卖品牌图标

        today_element=self.brand.open_url_get_element('list_pop_a','special_today_pop')#打开新网页
        before_location= self.brand.get_element_location('special_today_pop_target')
        today_element.click()#点击今日必抢
        after_location=self.brand.get_element_location('special_today_pop_target')
        return self.assertTrue(before_location==after_location, "测试失败")

    def test01_special_tag02(self):
        self.brand.click_one('brand_btn')  # 点击品牌团
        self.brand.click_one('list_a')  # 点击第一个分类按钮
        self.brand.click_one('list_pop_a')  # 点击第一个热卖品牌图标

        today_element=self.brand.open_url_get_element('list_pop_a','special_today_after')#打开新网页
        print(today_element.get_attribute('textContent'))
        before_location= self.brand.get_element_location('special_today_after_target')
        today_element.click()#点击下一个tag
        after_location=self.brand.get_element_location('special_today_after_target')
        return self.assertTrue(before_location==after_location, "测试失败")


# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(SepcialPageTag('test01_special_tag01'))
#     unittest.TextTestRunner().run(suite)
