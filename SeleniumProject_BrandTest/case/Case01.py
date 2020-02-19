# coding=utf-8
from selenium import webdriver
from util.find_element import my_get_element
import unittest, time, os
from business.brand_business import BrandBusiness

class HomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'e:\webdrivers\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.get('https://www.zhe800.com')
        self.driver.maximize_window()
        self.brand=BrandBusiness(self.driver)

    def tearDown(self):
        # time.sleep(2)
        self.driver.quit()

    # 品牌专场入口测试

    def test01_brand_pop(self):
        self.brand.click_one('brand_btn')# 点击品牌团
        self.brand.click_one('pop_brand_a')# 点击热卖品牌第一个品牌图标
        target_name = self.brand.get_text_from_img('pop_brand_img')#获取品牌专场的名字
        expect_name = self.brand.get_brand_expect_name('pop_brand_a')#获取点开链接后的专场名字
        return self.assertTrue(expect_name == target_name, "测试失败")#判断两个名字是否相同

    def test02_brand_card(self):
        self.brand.click_one('brand_btn')# 点击品牌团
        self.brand.click_one('brand_card_a')  # 点击第一个品牌卡片
        target_name = self.brand.get_text_from_content('brand_card_text_a')# 获取品牌专场的名字
        expect_name = self.brand.get_brand_expect_name('brand_card_a')#获取点开链接后的专场名字
        return self.assertTrue(expect_name == target_name, "测试失败")#判断两个名字是否相同

    def test03_brand_card_text(self):
        self.brand.click_one('brand_btn')# 点击品牌团
        self.brand.click_one('brand_card_text_a')  # 点击第一个品牌卡片
        target_name = self.brand.get_text_from_content('brand_card_text_a')# 获取品牌专场的名字
        expect_name = self.brand.get_brand_expect_name('brand_card_text_a')#获取点开链接后的专场名字
        return self.assertTrue(expect_name == target_name, "测试失败")#判断两个名字是否相同

    def test04_brand_next_page_card(self):
        self.brand.click_one('brand_btn')# 点击品牌团
        js = "window.scrollTo(0,document.body.scrollHeight)"#滑动到底部
        self.driver.execute_script(js)
        self.brand.click_one('next_page_btn')  # 点击下一页按钮
        self.brand.click_one('brand_card_text_a')  # 点击第一个品牌卡片
        target_name = self.brand.get_text_from_content('brand_card_text_a')# 获取品牌专场的名字
        expect_name = self.brand.get_brand_expect_name('brand_card_text_a')#获取点开链接后的专场名字
        return self.assertTrue(expect_name == target_name, "测试失败")#判断两个名字是否相同