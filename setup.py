#!/usr/bin/env python
from setuptools import setup
from inlinestyle import __version__
setup(
    name="inlinestyle",
    version=__version__,
    include_package_data=True,
    packages=('inlinestyle',),
    install_requires=('cssutils','BeautifulSoup','requests'),
    description="converts <style> blocks to inline styles",
    license = "BSD",
    author="Matt George",
    author_email="mgeorge@gmail.com",
    url="http://github.com/binarydud/inlinestyler",
)

