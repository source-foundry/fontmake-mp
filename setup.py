import os
import re
from setuptools import setup, find_packages


setup(
    name='fontmake-mp',
    version='0.9.0',
    description='A font vertical metrics reporting and line spacing adjustment tool',
    url='https://github.com/source-foundry/fontmake-mp',
    license='MIT license',
    author='Christopher Simpkins',
    author_email='chris@sourcefoundry.org',
    platforms=['any'],
    install_requires=['fontmake']
)