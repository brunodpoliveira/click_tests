from setuptools import setup, find_packages

setup(
    name='package',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        script=yourpackage.scripts.script:cli
    ''',
)

# test the script
# $ virtualenv venv
# $ . venv/bin/activate
# $ pip install --editable .
# $ script --count=3

