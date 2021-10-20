"""
$ python3 install setup.py
$ python3 -m demo
"""
from setuptools import setup


setup(
    name='demo',
    version='0.2',
    long_description=__doc__,
    packages=['demo'],
    include_package_data=False,
    zip_safe=False,
    setup_requires=["pytest-runner"],
    install_requires=[
        'aiohttp',
        'multidict==4.5.2',
        'yarl==1.3.0'
    ],
    entry_points="""
    [console_scripts]
    demo = demo.main:main
    """,
    classifiers=[
        'Operating System :: OS Independent'
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)
