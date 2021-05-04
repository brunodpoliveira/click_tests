from setuptools import setup, find_packages

setup(
    name='testpackage',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        yourscript=testpackage.scripts.yourscript:cli
    ''',
)

# test the script
# $ virtualenv venv
# $ . venv/bin/activate
# $ pip install --editable .
# $ yourscript --count=3
