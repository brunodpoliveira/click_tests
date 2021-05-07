from setuptools import setup

setup(
    name='testscript',
    version='0.1',
    py_modules=['yourscript'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        yourscript=yourscript:cli
    ''',
)

# test the script
# $ virtualenv venv
# $ . venv/bin/activate
# $ pip install --editable .
# $ yourscript --count=3

