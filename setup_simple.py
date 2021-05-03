from setuptools import setup

setup(
    name='script',
    version='0.1',
    py_modules=['script'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        script=script:cli
    ''',
)

# test the script
# $ virtualenv venv
# $ . venv/bin/activate
# $ pip install --editable .
# $ script --count=3

