# Matplotlib Tutorial Lab

## Introduction

This tutorial lab will guide you through using Matplotlib in a Flask web application server. You will learn how to create figures using the `.Figure` constructor and save them to in-memory buffers, embed the resulting figures in HTML output, and run the Flask application using the `flask` command-line tool.

## Steps

### Step 1: Install Dependencies

Before we get started, make sure you have the necessary packages installed. You can install them using pip.

```python
pip install matplotlib flask
```

### Step 2: Import Dependencies

In this step, we will import the necessary dependencies. We will use `base64` to encode the image data, `BytesIO` to store the image data in memory, `Flask` to create the web application server, and `Figure` to create the figures.

```python
import base64
from io import BytesIO

from flask import Flask

from matplotlib.figure import Figure
```

### Step 3: Create the Flask Application

In this step, we will create the Flask application. We will define a route for the home page (`"/"`) and a function to generate and embed the Matplotlib figure.

```python
app = Flask(__name__)

@app.route("/")
def home():
    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"
```

### Step 4: Run the Flask Application

In this step, we will run the Flask application using the `flask` command-line tool. Assuming that the working directory contains this script, run the following command to start the server:

```console
FLASK_APP=matplot_lib_tutorial_lab flask run
```

### Step 5: View the Output

In this step, we will view the output of the Flask application by navigating to `http://localhost:5000/` in a web browser. The Matplotlib figure should be displayed on the page.

## Summary

In this tutorial lab, we learned how to use Matplotlib in a Flask web application server. We created a Flask application, generated a Matplotlib figure, embedded the figure in the HTML output, and ran the Flask application using the `flask` command-line tool.
