# coding=utf-8
from selenium import webdriver
from util.find_element import my_get_element
import unittest, time, os
from business.brand_business import BrandBusiness


class SepcialPagePrice(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'e:\webdrivers\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.get('https://www.zhe800.com')
        self.brand = BrandBusiness(self.driver)

    def tearDown(self):
        # time.sleep(2)
        self.driver.quit()

    # 品牌专场入口测试
    def test01_special_price_ascend(self):
        self.brand.click_one('brand_btn')  # 点击品牌团
        self.brand.click_one('pop_brand_a')  # 点击热卖品牌第一个品牌图标
        sort_element = self.brand.open_url_get_element('pop_brand_a', 'special_price_sort')
        sort_element.click()
        first_price = self.brand.get_text_from_content('special_item01_price')  # 获取第一个商品价格
        second_price = self.brand.get_text_from_content('special_item02_price')  # 获取第二个商品价格
        return self.assertTrue(first_price <= second_price, "测试失败")

    def test02_special_price_descend(self):
        self.brand.click_one('brand_btn')  # 点击品牌团
        self.brand.click_one('pop_brand_a')  # 点击热卖品牌第一个品牌图标
        sort_element = self.brand.open_url_get_element('pop_brand_a', 'special_price_sort')
        sort_element.click()
        sort_element.click()
        first_price = self.brand.get_text_from_content('special_item01_price')  # 获取第一个商品价格
        second_price = self.brand.get_text_from_content('special_item02_price')  # 获取第二个商品价格
        print(first_price)
        print(second_price)
        return self.assertTrue(first_price >= second_price, "测试失败")


# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(SepcialPagePrice('test01_special_price_ascend'))
#     suite.addTest(SepcialPagePrice('test02_special_price_descend'))
#     unittest.TextTestRunner().run(suite)
