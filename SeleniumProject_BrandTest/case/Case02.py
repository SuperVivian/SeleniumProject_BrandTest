# coding=utf-8
from selenium import webdriver
from util.find_element import my_get_element
import unittest, time, os
from business.brand_business import BrandBusiness

class ListPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'e:\webdrivers\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.get('https://www.zhe800.com/')
        self.brand=BrandBusiness(self.driver)

    def tearDown(self):
        # time.sleep(2)
        self.driver.quit()

    # 品牌专场入口测试
    def test01_list_pop(self):
        self.brand.click_one('brand_btn')# 点击品牌团
        self.brand.click_one('list_a')# 点击第一个分类按钮
        self.brand.click_one('list_pop_img')  # 点击第一个热卖品牌图标
        target_name = self.brand.get_text_from_img('list_pop_img')#获取品牌专场的名字
        expect_name = self.brand.get_brand_expect_name('list_pop_a')#获取点开链接后的专场名字
        return self.assertTrue(expect_name == target_name, "测试失败")#判断两个名字是否相同

    def test02_list_brand_text(self):
        self.brand.click_one('brand_btn')# 点击品牌团
        self.brand.click_one('list_a')  # 点击第一个分类按钮
        self.brand.click_one('list_brand_text_a')  # 点击第一个专场名字链接
        target_name = self.brand.get_text_from_content('list_brand_text_span')# 获取品牌专场的名字
        expect_name = self.brand.get_brand_expect_name('list_brand_text_a')#获取点开链接后的专场名字
        return self.assertTrue(expect_name == target_name, "测试失败")#判断两个名字是否相同

    def test03_list_brand_all(self):
        self.brand.click_one('brand_btn')# 点击品牌团
        self.brand.click_one('list_a')  # 点击第一个分类按钮
        self.brand.click_one('list_brand_all')  # 点击第一个专场的品牌全部商品
        target_name = self.brand.get_text_from_content('list_brand_text_span')# 获取品牌专场的名字
        expect_name = self.brand.get_brand_expect_name('list_brand_all')#获取点开链接后的专场名字
        return self.assertTrue(expect_name == target_name, "测试失败")#判断两个名字是否相同

    def test04_list_gray_brand(self):
        self.brand.click_one('brand_btn')# 点击品牌团
        self.brand.click_one('list_a')  # 点击第一个分类按钮
        self.brand.click_one('list_pop_last_page')  # 点击热卖的上一页
        self.brand.click_one('list_last_gray_pop_a')  # 点击第一个灰色的品牌图标
        target_name = self.brand.get_text_from_img('list_last_gray_pop_img')# 获取品牌专场的名字
        expect_name = self.brand.get_brand_expect_name('list_last_gray_pop_a')#获取点开链接后的专场名字
        return self.assertTrue(expect_name == target_name, "测试失败")#判断两个名字是否相同

# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(ListPage('test03_list_brand_all'))
#     suite.addTest(ListPage('test04_list_gray_brand'))
#     unittest.TextTestRunner().run(suite)


