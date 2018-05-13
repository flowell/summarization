from urllib import request
from lxml import etree
import re
import math

if __name__ == "__main__":
    code = 600030
    root_url = "http://guba.eastmoney.com"
    base_url = "http://guba.eastmoney.com/list,"+ str(code) + ",2,f.html"
    root_response = request.urlopen(base_url)
    root_result = root_response.read().decode('utf-8')
    root_selector = etree.HTML(root_result)
    page_str = root_selector.xpath('//*[@id="articlelistnew"]/div[last()]/span/@data-pager')[0]
    print('有关页面数的字符串:', page_str)

    pattern = re.compile(r'(?<=\|)\d+')
    total_page = int(pattern.findall(page_str)[0])
    each_page = int(pattern.findall(page_str)[1])
    page_num = math.ceil(total_page / each_page)
    print('总页数:',page_num)

    visited_page = 0
    rest_page = total_page
    for page_count in range(1, int(page_num) + 1):
        url = "http://guba.eastmoney.com/list,"+ str(code) + ",2,f_" + str(page_count) + ".html"
        response = request.urlopen(url)
        result = response.read().decode('utf-8')
        selector = etree.HTML(result)
        max_num = 0
        if rest_page <= 80:
            max_num = rest_page
        else:
            max_num = 80
        for num in range(2, 2 + max_num):
            visited_page += 1
            title = selector.xpath('//*[@id="articlelistnew"]/div[' + str(num) + ']/span[3]/a/@title')[0]
            href = selector.xpath('//*[@id="articlelistnew"]/div[' + str(num) + ']/span[3]/a/@href')[0]

            detail_url = root_url + href
            detail_response = request.urlopen(detail_url)
            detail_result = detail_response.read().decode('utf=8')          #这里不加解码的话或导致下面生成乱码
            detail_selector = etree.HTML(detail_result)
            text = detail_selector.xpath('string(//*[@id="zwconbody"]/div/p[3])')
            #删除多余的信息
            tail = '[点击查看PDF原文] 今日最新研究报告'
            if text.endswith(tail):
                text = text[:-len(tail)]
            print(text)




