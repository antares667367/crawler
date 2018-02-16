import bs4 as BeautifulSoup
import requests

from .debug import Debug
from .info import Info
from .color import Colors as F


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
        self.params['product'] = bin # set product (the actual binary)
        if version:
            self.params['version'] = version # set version if any if any
        try:
            cve_list = self.__make_search() # do search
            self.debug.log(cve_list,"cve list",self.info.line()) # print for debug
        except Exception as e: # raise err if any
            self.debug.log(e.args, "ERR", self.info.line())
        self.params = {
            'vendor': '',
            'product': '',
            'version': ''
        } # params fr the api
        return cve_list # return list

    def __make_search(self):#make the actual search
        """
        Make a search
        :return:
        """
        OK = "{}{}{}".format(F.OKGREEN, "OK", F.END) # set vars for display TODO integrate in Colors
        ERR = "{}{}{}".format(F.FAIL, "ERR", F.END)
        page = requests.get(self.url_search[0], self.params) # request the api
        page.encoding = 'utf-8' # set encoding of the page
        parser = BeautifulSoup.BeautifulSoup(page.content, "lxml") # use lxml parser
        table = parser.find("table", attrs={'class': "searchresults"}) # get table if any
        try:
            if table:
                if table.has_attr('id') and table.get('id') == "vulnslisttable":
                    # if there is only one CVE or none , this function will be triggered
                    return self.__parse_cve_list(table) # return table content in both cases
                else:
                    # else that one will
                    return self.__parse_vendor_list(table)
            else:
                return []
        except Exception as e: # raise error if any
            self.debug.log("{}{} {}{}".format(F.FAIL, e, bin, F.END), ERR, self.info.line())

    def __parse_cve_list(self, cve_parser):
        """
        parse cve list, triggered if one CVE or None
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
        parse vendor, trigerred if multiple CVEs
        :param vendor_parser:
        :return:
        """
        vendors_list = vendor_parser.select('tr')[1:]
        cve_list = []
        page = ""
        for vendor in vendors_list:
            nbr_vuln = vendor.select('td.num')
            if nbr_vuln:
                nbr_vuln = int(nbr_vuln.pop().text)
            else:
                nbr_vuln = 0
            if nbr_vuln > 0:
                link = vendor.select('td a').pop()
                page = requests.get(self.url + link.get('href'))
                page.encoding = 'utf-8'
                cve_parser = BeautifulSoup.BeautifulSoup(page.content, 'lxml')
                cve_list += self.__parse_cve_list(cve_parser.find('table', attrs={'id': 'vulnslisttable'}))
        return cve_list
