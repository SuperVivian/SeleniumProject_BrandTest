# coding=utf-8
from selenium import webdriver
from util.find_element import my_get_element
import unittest, time, os
from business.brand_business import BrandBusiness

class SepcialPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'e:\webdrivers\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.get('https://www.zhe800.com')
        self.brand=BrandBusiness(self.driver)

    def tearDown(self):
        # time.sleep(2)
        self.driver.quit()

    # 品牌专场入口测试
    def test01_special_recommend_name(self):
        self.brand.click_one('brand_btn')# 点击品牌团
        self.brand.click_one('pop_brand_a')# 点击热卖品牌第一个品牌图标
        recommend_element = self.brand.open_url_get_element('pop_brand_a', 'sepcial_recommend_a')
        recommend_element.click()  # 点击第一个推荐品牌专场
        target_name = self.brand.get_text_from_content('sepcial_recommend_a')#获取品牌专场的名字
        expect_name = self.brand.get_brand_expect_name('sepcial_recommend_a')#获取点开链接后的专场名字
        return self.assertTrue(expect_name == target_name, "测试失败")#判断两个名字是否相同

    def test02_special_recommend_more(self):
        self.brand.click_one('brand_btn')# 点击品牌团
        self.brand.click_one('pop_brand_a')# 点击热卖品牌第一个品牌图标
        recommend_element= self.brand.open_url_get_element('pop_brand_a','special_recommend_more')
        recommend_element.click()  # 点击第一个推荐品牌专场的查看更多
        target_name = self.brand.get_text_from_content('sepcial_recommend_a')#获取品牌专场的名字
        expect_name = self.brand.get_brand_expect_name('special_recommend_more')#获取点开链接后的专场名字
        return self.assertTrue(expect_name == target_name, "测试失败")#判断两个名字是否相同

# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTest(SepcialPage('test01_special_recommend_name'))
#     suite.addTest(SepcialPage('test02_special_recommend_more'))
#     unittest.TextTestRunner().run(suite)

