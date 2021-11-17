import unittest
from spider.bank import BankSpider


class BankTestCase(unittest.TestCase):
    def test_bank(self):
        spider = BankSpider()
        out_file = "/tmp/bank_category.csv"
        in_file = "/Users/xbkaishui/work/sources/wandoujia-spider/data/bank_list.txt"
        spider.crawl(in_file, out_file)


if __name__ == '__main__':
    unittest.main()
