# from url_encoding import make_url
# full url encoding

import urllib
try: # Python2 and python3 comatible code
    from urllib.parse import urlparse
except ImportError:
     from urlparse import urlparse


def make_url(string):
    '''Encode every char in percentage format'''
    return "".join("%{0:0>2}".format(format(ord(char), "x")) for char in string)


def make_plus(string):
    return "".join("+" if letter == " " else letter for letter in string)


def make_plus_encoded(string):
    return urllib.quote_plus(string)


def make_key_url(string):
    return urllib.quote(string)


