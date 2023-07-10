# Flask Signals

## Introduction

In this lab, you will learn how to use signals in Flask, which are a lightweight way to notify subscribers of certain events during the lifecycle of the application and each request. Signals allow you to perform actions in response to specific events without directly affecting the application code. They are useful for testing, metrics, auditing, and more.

## Steps

### Step 1: Installing Flask and Blinker

Before we begin, make sure you have Flask and Blinker installed. You can install them using pip:

```
pip install flask blinker
```

### Step 2: Importing the Required Modules

In your Flask application, import the necessary modules:

```python
from flask import Flask
from blinker import Namespace
```

### Step 3: Creating a Flask Application

Create a Flask application instance:

```python
app = Flask(__name__)
```

### Step 4: Creating a Namespace for Signals

Create a namespace for your signals using the Blinker library:

```python
my_signals = Namespace()
```

### Step 5: Creating a Signal

Create a new signal in your namespace. Give it a descriptive name to identify the event it represents:

```python
model_saved = my_signals.signal('model-saved')
```

### Step 6: Subscribing to a Signal

To subscribe to a signal, use the `connect` method of the signal. Provide a function that should be called when the signal is emitted:

```python
@model_saved.connect
def on_model_saved(sender):
    print("Model saved!")
```

### Step 7: Emitting a Signal

To emit a signal, call the `send` method of the signal. Pass the sender as the first argument:

```python
model_saved.send(app)
```

### Step 8: Running the Application

Finally, run the Flask application:

```python
if __name__ == '__main__':
    app.run()
```

### Summary

In this lab, you learned how to use signals in Flask to notify subscribers of specific events during the lifecycle of the application. You created a namespace for signals, created a signal, subscribed to the signal, and emitted the signal. Signals are a powerful tool for adding functionality to your Flask application without directly modifying the application code.
