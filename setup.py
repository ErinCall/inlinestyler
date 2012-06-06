from setuptools import setup

setup(name="inlinestyle",
      version="0.2",
      description="convert html style blocks to inline style statements",
      author="Matt George",
      author_email="mgeorge@gmail.com",
      install_requires=["beautifulsoup", "nose", "cssutils"])
