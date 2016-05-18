from setuptools import setup, find_packages
from easy.version import VERSION

setup(
    name='stups-easy',
    packages=find_packages(),
    version=VERSION,
    description='Easy to never forget STUPS commands.',
    author='Zalando SE',
    url='https://github.bus.zalan.do/rcaricio/stups-easy',
    license='Apache License Version 2.0',
    install_requires=['stups'],
    tests_require=['pytest', 'pytest-cov'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    long_description='Easy to never forget STUPS commands.',
    entry_points={'console_scripts': ['easy = easy.run:main']},
)
