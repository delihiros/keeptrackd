from setuptools import setup, find_packages


setup(
    name='keeptrackd',

    version='1.0.0',

    description='always keep tracked to your interest',

    url='https://github.com/delihiros/keeptrackd',

    author='delihiros',
    author_email='delihiros@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Utilities',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.7',
    ],

    keywords='web crawler utilities tracker checker',


    install_requires=['selenium', 'chromedriver-binary'],

    packages=['keeptrackd'],

    entry_points={
        'console_scripts': ['keeptrackd=keeptrackd:main']
        }
)
