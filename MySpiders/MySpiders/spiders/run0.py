from scrapy import cmdline

cmdline.execute("scrapy runspider TestSpider.py -o top-stackoverflow-questions.json".split())
