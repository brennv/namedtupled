from setuptools import setup


def readme(text=''):
    with open('README.rst', 'r') as f:
        for line in f:
            if '---' in line or '~~~' in line:
                line = line.replace('-', '=')
                line = line.replace('~', '=')
            text += line
        return text


setup(
    name='namedtupled',
    packages=['namedtupled'],
    version='0.1.3',
    description='Lightweight wrapper for creating namedtuples.',
    # from nested dicts, lists, json and yaml
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    author='brennv',
    author_email='brennan@beta.build',
    license='MIT',
    url='https://github.com/brennv/namedtupled',
    docs_url='https://github.com/brennv/namedtupled#readme',
    download_url='https://github.com/brennv/namedtupled/tarball/0.1.3',
    keywords='namedtupled namedtuple json yaml',
    install_requires=[
        'future',
        'pyyaml',
    ],
    include_package_data=True,
    zip_safe=False)
