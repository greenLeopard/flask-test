# Flask test app

Build a basic webapp that will:
* display some drop downs in a window
* display a date picker
* display an image

## Getting started

Here are the instructions for getting up and running with the `flask-test` project.

Install miniconda and python 3.7 (or higher).

### Clone the repo 

Create a folder where you want to save the files, then clone the repo using SSH:

```
git clone git@github.com:greenLeopard/flask-test.git
```

### Create an environment

At the terminal window, navigate to the main folder for this repo.

Execute these instructions in your terminal for a conda environment:
```
conda env create --file environment.yml
conda activate flask # activate the new environment
```

### Run the app (locally)

After creating a python environment, you can run the test project:

```
$ export FLASK_APP=microblog.py
$ flask run
```

The app will be running at the local host:  `http://localhost:5000/`

## Running the tests

The tests for this system are written using `pytest` and are stored in the folder called `tests`.

To run the tests:
```python
pytest
```

## Authors

Just the leopard.

### Acknowledgments

Based on some flask tutorials:
 * [Tutorial 1](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
 


## Licenses

This is just a test.