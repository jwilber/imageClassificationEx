# Image Classification POC 

 

Example demonstrating a simple image classification algorithm trained to predict ground ('pad-mounted') transformers vs pole-mounted transformers.

 

## Getting Started

 

Running either the flask app or the notebook requires a few libraries to be installed locally. I've included a `requirements.txt` file to make this as easy as possible. See instructions below for more details:

 

### Prerequisites

 
 The project was written with `python 3.6.2`

To view a list of required dependencies, view the `requirements.txt` file.

To use the notebook or the flask app, you must first download the model.

This is available for download <a href="https://drive.google.com/file/d/1Zs6uN-8zlG7NOqIyan5_z9_53txC2ilj/view?usp=sharing">here</a>.

Once you've downloaded the model, move it into `imageClassificationEx/flask_apps/`



### Installing

 

If you need to install libraries, it's best to do so in an environment specific to the project, so you don't pollute your global `python` environment.

 

Once you've set up a local environment, installing the libraries is as easy as a simple `pip` call:
 

```
pip install -r requirements.txt
```

Note, if you run into an issue regarding `tensorflow`, try running the following command (inside your project environment):

```
pip install --ignore-installed tensorflow
```
 
To obtain the notebook and required files, simply clone the repo into the desired directory:


```
git clone https://github.com/jwilber/imageClassificationEx.git
```


## Running the flask app

To run the flask app, navigate to the root of the project directory and run the following commands:

```
cd imageClassificationEX/flask_apps
export FLASK_APP=predict_app.py
flask run --host=0.0.0.0
```

Then, open a web-browser and navigate to `http://localhost:5000/static/predict.html`


## Running the notebook


To run the notebook, `cd` into the cloned repo, and run `jupyter notebook`:
 

```
cd imageClassificationEx
jupyter notebook
```

The browser should open a directory; open the `.ipynb` file. Otherwise, copy and paste the specified link into your web-browser.

