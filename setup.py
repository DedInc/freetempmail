from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='freetempmail',
    version='1.0.1',
    author='Maehdakvan',
    author_email='visitanimation@google.com',
    description='Temp-Mail.org API wrapper.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DedInc/freetempmail',
    project_urls={
        'Bug Tracker': 'https://github.com/DedInc/freetempmail/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data = True,
    install_requires = ['undetected-chromedriver', 'requests >= 2.9.2', 'requests_toolbelt >= 0.9.1', 'pyparsing >= 2.4.7'],
    python_requires='>=3.6'
)