from HTMLTestRunner import HTMLTestRunner  # 导入生成HTML报告的包

def export_report(suite):
    """生成测试报告"""
    file_path = "E:\\Python3.7\\PythonStudy\\SeleniumProject\\report\\report.html"
    f = open(file_path, 'wb')
    runner = HTMLTestRunner(stream=f, title="品牌专场功能测试报告",
                            description=u"在不同入口查看品牌专场及商品的测试",
                            verbosity=2)
    runner.run(suite)
    f.close()