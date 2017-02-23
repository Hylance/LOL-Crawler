# -*- coding:utf-8 -*-
# 网页解析器
import re
from bs4 import BeautifulSoup
import urlparse


class HtmlParser(object):
    # 对html_cont的内容进行解析
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    # 获取页面上所有的url
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # 根据分析，链接的格式是：/view/12334.htm
        links = soup.find_all('li', class_='default-1-3')
        for link in links:
            new_url = link.find('a')['href']
            # url格式需要进行拼接，加上  http://baike.baidu.com
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    # 获取每一页面的数据，包括标题以及简介
    def _get_new_data(self, page_url, soup):
        # 以一个词典数据类型保存数据
        res_data = {}
        # 保存url
        res_data['url'] = page_url
        # 下面是标题的格式
        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        champion_name = soup.find('div', id="champ_header").find('h1')
        res_data['champion_name'] = champion_name.get_text()
        # 开始获取简介的内容
        # <div class="lemma-summary" label-module="lemmaSummary">
        nick_name = soup.find('div', id="champ_header").find('h3').find('em')
        res_data['nick_name'] = nick_name.get_text()
        res_data['abilities'] = []
        abilities = soup.find_all('div', class_="default-5-6")
        for ability in abilities:
            res_data['abilities'].append(ability.find('h3').get_text())
        return res_data
