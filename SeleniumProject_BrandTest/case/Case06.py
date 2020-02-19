# coding=utf-8
from selenium import webdriver
from util.find_element import my_get_element
import unittest, time, os
from business.brand_business import BrandBusiness


class ListPageItem(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'e:\webdrivers\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.get('https://www.zhe800.com')
        self.brand = BrandBusiness(self.driver)

    def tearDown(self):
        # time.sleep(2)
        self.driver.quit()

    # 品牌专场入口测试
    def test01_list_item_card(self):
        self.brand.click_one('brand_btn')  # 点击品牌团
        self.brand.click_one('list_a')  # 点击第一个分类按钮
        target_name = self.brand.get_text_from_content('list_item_card_text_a')# 获取商品名字
        self.brand.click_one('list_item_card_a')  # 点击第一个商品卡片
        item_name_element = self.brand.open_url_get_element('list_item_card_a', 'item_name')  # 打开新网页
        expect_name = self.brand.get_strip_text(item_name_element)  # 获取打开链接后的商品名字
        return self.assertTrue(expect_name == target_name, "测试失败")

    def test02_list_item_text(self):
        self.brand.click_one('brand_btn')  # 点击品牌团
        self.brand.click_one('list_a')  # 点击第一个分类按钮
        target_name = self.brand.get_text_from_content('list_item_card_text_a')  # 获取商品名字
        self.brand.click_one('list_item_card_text_a')  # 点击第一个商品卡片
        item_name_element = self.brand.open_url_get_element('list_item_card_text_a', 'item_name')  # 打开新网页
        expect_name = self.brand.get_strip_text(item_name_element)  # 获取打开链接后的商品名字
        return self.assertTrue(expect_name == target_name, "测试失败")

# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(ListPageItem('test01_list_item_card'))
#     suite.addTest(ListPageItem('test02_list_item_text'))
#     unittest.TextTestRunner().run(suite)
