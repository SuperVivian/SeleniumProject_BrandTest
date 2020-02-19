# coding=utf-8
import unittest
import os
from util.export_report import export_report

class RunCase(unittest.TestCase):
    def test_case(self):
        case_path = os.path.join(os.getcwd(), 'case')
        suite = unittest.defaultTestLoader.discover(case_path, 'Case*.py')
        # 生成报告
        export_report(suite)


if __name__ == '__main__':
    unittest.main()