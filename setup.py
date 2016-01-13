from setuptools import setup, find_packages
from os import path
import codecs


def readfile(file_path):
    return codecs.open(file_path, 'r', 'utf-8').read()


setup(
    name='djangohitcounter',
    version='0.1.5',

    author='Anton Kuzmichev',
    author_email='assargin@gmail.com',
    license='Apache 2.0',

    packages=find_packages(exclude=("tests",)),

    description='Pretty simple hit counter for Django ORM objects',
    long_description=readfile(path.join(path.dirname(__file__), 'README.rst')),

    url='https://github.com/DirectlineDev/django-hitcounter',
    download_url='https://github.com/DirectlineDev/django-hitcounter/archive/master.zip',

    keywords=['django', 'hits', 'counter', 'hits counter', 'hitcounter'],
    classifiers=[
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable', - coming soon
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
