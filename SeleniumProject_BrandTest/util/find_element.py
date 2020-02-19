#coding=utf-8
from util.read_ini import ReadIni


class FindElement(object):
    def __init__(self,driver):
        self.driver = driver
    def get_element(self,key):
        read_ini = ReadIni()
        value = read_ini.get_value(key)
        try:
            return self.driver.find_element_by_xpath(value)
        except:
            return None

def my_get_element(driver, key):
    """定位element"""
    find_element = FindElement(driver)
    element = find_element.get_element(key)
    return element