from setuptools import setup, find_packages
from dory.version import VERSION

setup(
    name='stups-dory',
    packages=find_packages(),
    version=VERSION,
    description='Dory to never forget STUPS commands.',
    author='Zalando SE',
    url='https://github.bus.zalan.do/rcaricio/stups-dory',
    license='Apache License Version 2.0',
    install_requires=[],
    tests_require=['pytest', 'pytest-cov'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    long_description='Dory to never forget STUPS commands.',
    entry_points={'console_scripts': ['dory = dory.run:main']},
)
