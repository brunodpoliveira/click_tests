from setuptools import setup, find_packages

setup(
    name='tutorialgitclone',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        yourscript=tutorialgitclone.scripts.gitclone:cli

    ''',
)

# test the script
# $ virtualenv venv
# $ . venv/bin/activate
# $ pip install --editable .
# $ gitclone --count=3
