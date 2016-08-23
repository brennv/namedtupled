from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='namedtupled',
    packages=['namedtupled'],
    version='0.1.2',
    description='Lightweight wrapper for creating namedtuples.',
    # from nested dicts, lists, json and yaml
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Intended Audience :: Developers',
    ],
    author='brennv',
    author_email='brennan@beta.build',
    license='MIT',
    url='https://github.com/brennv/namedtupled',
    download_url='https://github.com/brennv/namedtupled/tarball/0.1.2',
    keywords='namedtupled namedtuple json yaml',
    install_requires=[
        'future',
        'pyyaml',
    ],
    include_package_data=True,
    zip_safe=False)
