from setuptools import setup

setup(
    name='rakuten_api',
    version='0.1.0',
    author='Daniel Perez',
    author_email='daniel@claudetech.com',
    packages=['rakuten_api'],
    url='https://github.com/claudetech/python_rakuten_api',
    license='LICENSE',
    description='Rakuten API client.',
    long_description=open('README.md').read(),
    install_requires=[
         'requests >= 2.3.0'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries'
    ],
)
