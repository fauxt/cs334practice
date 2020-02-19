# cs334practice
# Capstone Project

## Developer Setup

1. Create a virtual environment

    `python3 -m venv .venv`

2. Activate the virtual environment

    `source .venv/bin/activate`
    
3. Install required libraries

    `pip install -r requirements.txt`
    
4. Install source as an editable package

    `pip install -e .`
    
5. Create the file `.env` containing our sensitive data (that should never go in the repo)

    `secret=42`
    
Once you have completed these steps you should be able to:

* Run `pytest` from the root of the project
* Run `pytest` from `tests/`
* Run `main.py` from anywhere (e.g. `python src/python_structure/main.py`)
* Run `pylint` from anywhere in the project


## Files and Directories

* `requirements.txt` - The list of required libraries.  
* `setup.py` - The script the `pip` runs to install the package.  The current version is bare-bones.  Many
   other options should be set for a production system.
* `src/python_structure/__init__.py` - Establishes the `python_structure` directory as a package. This file is empty 
   by default.


## Pylint

* Command to run pylint: `pylint mymodule.py`
* Pylint config file name is `.pylintrc`
