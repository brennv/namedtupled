from setuptools import setup

readme = open('README.rst', 'r')
README_TEXT = readme.read()
readme.close()

setup(
  name = 'namedtupled',
  packages = ['namedtupled'],
  version = '0.1',
  description = 'Lightweight wrapper for creating namedtuples from nested dicts, lists, json and yaml.',
  long_description=README_TEXT,
  classifiers=[
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
  ],
  author = 'brennv',
  author_email = 'brennan@beta.build',
  license='MIT',
  url = 'https://github.com/brennv/namedtupled',
  download_url = 'https://github.com/brennv/namedtupled/archive/0.1.tar.gz',
  keywords = 'namedtupled namedtuple json yaml',
  install_requires=[
    'future',
    'pyyaml',
  ],
  include_package_data=True,
  zip_safe=False)
