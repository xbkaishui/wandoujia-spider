# -*- coding: UTF-8 -*-
import csv

class BankSpider(object):

    def crawl(self, banks_url, out_file):
        kline_writer = csv.writer(out_file, delimiter=',',
                                  quotechar='|', quoting=csv.QUOTE_MINIMAL)
        pass
