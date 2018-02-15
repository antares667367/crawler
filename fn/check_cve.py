import asyncio

import bs4 as BeautifulSoup
import requests

from .debug import Debug
from .info import Info


class Cve:
    """
    thanks to RICO kevin
    """

    def __init__(self):
        """
        init Cve
        """
        self.info = Info(enabled=True)  # set info -(line number for debug)
        self.debug = Debug(internal_debug=True, color_output=True)  # set debug class
        self.debug.setLogger("check_cve.py")  # set logger with file name
        self.url = "https://www.cvedetails.com"
        self.url_search = "https://www.cvedetails.com/version-search.php",
        self.params = {
            'vendor': '',
            'product': '',
            'version': ''
        }

    def search(self, bin, version=None):
        self.params['product'] = bin
        if version:
            self.params['version'] = version
        try:
            cve_list = self.__make_search()
            self.debug.log(cve_list,"cve list",self.info.line())
        except Exception as e:
            self.debug.log(e.args, "ERR", self.info.line())
        self.params = {
            'vendor': '',
            'product': '',
            'version': ''
        }
        return cve_list

    def __make_search(self):
        """
        Make a search
        :return:
        """
        page = requests.get(self.url_search[0], self.params)
        page.encoding = 'utf-8'
        parser = BeautifulSoup.BeautifulSoup(page.content, "lxml")
        table = parser.find("table", attrs={'class': "searchresults"})
        if table:
            if table.has_attr('id') and table.get('id') == "vulnslisttable":
                return self.__parse_cve_list(table)
            else:
                return self.__parse_vendor_list(table)
        else:
            return []

    def __parse_cve_list(self, cve_parser):
        """
        parse cve list
        :param cve_parser:
        :return:
        """
        cve_from_url = cve_parser.select("td[nowrap] a")
        cve_list = []
        for cve in cve_from_url:
            cve_list.append(cve.text)
        return cve_list

    def __parse_vendor_list(self, vendor_parser):
        """
        parse vendor
        :param vendor_parser:
        :return:
        """
        vendors_list = vendor_parser.select('tr')[1:]
        cve_list = []
        for vendor in vendors_list:
            nbr_vuln = vendor.select('td.num')
            if nbr_vuln:
                nbr_vuln = int(nbr_vuln.pop().text)
            else:
                nbr_vuln = 0
            if nbr_vuln > 0:
                link = vendor.select('td a').pop()
                page.encoding = 'utf-8'
                page = requests.get(self.url + link.get('href'))
                cve_parser = BeautifulSoup.BeautifulSoup(page.content, 'lxml')
                cve_list += self.__parse_cve_list(cve_parser.find('table', attrs={'id': 'vulnslisttable'}))
        return cve_list
