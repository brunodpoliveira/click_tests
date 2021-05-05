test the script by putting these instructions on the terminal:

$ virtualenv venv
$ . venv/bin/activate
$ pip install --editable .
$ yourscript say --count=3

type yourscript --help or yourscript greet --help for more deatils on what each command does

if you feel like editing or adding features, you must modify the file yourscript.py at click_tests/testpackage/scripts
or
rename setup_simple.py to setup.py (we are using setup_package.py as the default template)
