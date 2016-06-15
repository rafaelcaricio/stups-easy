from setuptools import setup, find_packages


setup(
    name='stups-easy',
    packages=find_packages(),
    version='0.0.1',
    description='Easy to never forget STUPS commands.',
    author='Zalando SE',
    url='https://github.com/zalando-incubator/stups-easy',
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
