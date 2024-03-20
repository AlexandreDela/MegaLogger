from setuptools import setup, find_packages

setup(
    name='megalogger',
    version='0.6.2',
    author='Alexandre Delaisement',
    author_email='',
    description='A module dedicated to system engineering for object-oriented'
                ' logging of real-world items',
    long_description='A module  dedicated to system engineering '
                     'for the logging associated with real-world '
                     'items using object-oriented classes for both '
                     'handlers and items. The module also gives useful '
                     'blueprints to export to Excel, Text, SQL, ODS.',
    long_description_content_type='text/markdown',
    url='https://github.com/AlexandreDela/MegaLogger',
    packages=['megalogger'],
      package_dir={'megalogger': 'src/megalogger'},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        #'Topic :: Software Development :: Libraries :: Python Modules ::'
        #' System Engineering',
    ],
    keywords='logging system engineering',
    python_requires='>=3.8',
    install_requires=[
        "pandas >= 2.0.0",
        "openpyxl >= 3.1.2",
        "odfpy >= 1.3.2",
        "sphinx >= 7.1.0",
        "furo >= 2024.1.29",
        "pytest >= 8.1.1"
    ],
    project_urls={
        'Source': 'https://github.com/AlexandreDela/MegaLogger',
    },
)