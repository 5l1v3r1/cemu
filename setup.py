from setuptools import setup, find_packages
import io, pypandoc

def readme():
    try:
        long_description = pypandoc.convert('README.md', 'rst')
        long_description = long_description.replace("\r","")
    except OSError:
        print("Pandoc not found. Long_description conversion failure.")
        with io.open('README.md', encoding="utf-8") as f:
            long_description = f.read()
    return long_description


PROGNAME = 'cemu'
AUTHOR = 'hugsy'
EMAIL = 'hugsy@blah.cat'
VERSION = '0.2'
URL = 'https://github.com/{}/{}'.format(AUTHOR, PROGNAME)
RELEASE_LINK = '{}/archive/{}.tar.gz'.format(URL, VERSION)
LICENSE = 'MIT'

setup(
    name=PROGNAME,
    description='''Cemu is a basic assembly Qt-based IDE, to disassemble, assemble and emulate any assembly code (currently supports x86-{32,64}, ARM, AARCH64, MIPS, SPARC).''',
    long_description=readme(),
    url=URL,
    download_url=RELEASE_LINK,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Assemblers',
        'Natural Language :: English',
    ],
    author=AUTHOR,
    author_email=EMAIL,
    version=VERSION,
    license=LICENSE,
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'capstone>=3.0.4',
        'keystone-engine>=0.9',
        'unicorn>=1.0',
        'PyQt5',
        'enum34',
        'Pygments>=2.0'
    ],
    entry_points={
        'console_scripts': ['cemu=cemu.__main__:main'],
    },
    keywords = ['assembly', 'disassembly', 'emulation', 'x86', 'arm', 'mips', 'powerpc', 'sparc'],
)
