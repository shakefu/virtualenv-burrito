# encoding: utf-8
import os
import csv
import hashlib

try:
    from urllib2 import urlopen, HTTPError
except:
    from urllib.request import urlopen
    from urllib.error import HTTPError


PYPI_MD5_URL = 'https://pypi.python.org/pypi?:action=show_md5&digest='

PYPI_DOWNLOADS = {
    # filename: md5sum
    'setuptools-28.8.0.tar.gz': '43d6eb25f60e8a2682a8f826ce9e3f42',
    'setuptools-39.0.1.zip': '75310b72ca0ab4e673bf7679f69d7a62',
    'pip-9.0.1.tar.gz': '35f01da33009719497f01a4ba69d63c9',
    'pip-9.0.3.tar.gz': 'b15b33f9aad61f88d0f8c866d16c55d8',
    'virtualenv-15.1.0.tar.gz': '44e19f4134906fe2d75124427dc9b716',
    'virtualenv-15.2.0.tar.gz': 'b5f6b473140cc627d19d0d203f3b63cc',
    'virtualenvwrapper-4.7.2.tar.gz': '584fff776a63ae9d8722f4cd5c867da9',
    'virtualenvwrapper-4.8.2.tar.gz': '8e3af0e0d42733f15c5e36df484a952e',
}


def eq_(a, b, msg=None):
    if not a == b:
        raise AssertionError(msg or "%r != %r" % (a, b))


def test_tarball_names():
    tarballs = set()
    with open('versions.csv', 'r') as fo:
        reader = csv.reader(fo)
        for name, version, url, digest in reader:
            if name.startswith('_'):
                continue
            tarballs.add(os.path.basename(url))

    eq_(tarballs, set(PYPI_DOWNLOADS.keys()))


def test_shasum():
    with open('versions.csv', 'r') as fo:
        reader = csv.reader(fo)
        for name, version, url, digest in reader:
            if name.startswith('_'):
                continue
            sha1 = hashlib.sha1()
            sha1.update(urlopen(url).read())
            eq_(digest, sha1.hexdigest())


def test_md5_url_exists():
    for ball, md5sum in _items(PYPI_DOWNLOADS):
        url = PYPI_MD5_URL + md5sum
        try:
            urlopen(url)
        except HTTPError as e:
            assert False, "Failed to open %s: %s %s" % (url, type(e), e)


def _items(obj):
    try:
        func = obj.iteritems
    except:
        func = obj.items

    return func()
