### How to Create a spider from scratch ###
0. python 2.7
1. 终端执行以下命令，创建一个爬虫工程 
    scrapy startproject MySpiders
2. 运行第一个爬虫
    scrapy runspider TestSpider.py -o top-stackoverflow-questions.json
2. 构造选择器
    我们打开shell:
    scrapy shell http://doc.scrapy.org/en/latest/_static/selectors-sample1.html
    接着，当shell载入后，您将获得名为response
    的shell变量，其为响应的response， 并且在其 response.selector属性上绑定了一个 selector。
    因为我们处理的是HTML，选择器将自动使用HTML语法分析。
    （具体xpath和css的语法：https://www.jianshu.com/p/489c5d21cdc7）
