# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 15:28:20 2017

@author: Frank
"""

# from urllib import request
import urllib.request

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None

        return response.read()
        # response = response.decode('utf-8')