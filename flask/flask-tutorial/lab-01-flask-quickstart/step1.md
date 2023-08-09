# Setting up Flask

To get started with Flask, you need to install it and set up a new project. Follow the instructions below:

1. Install Flask by running the following command in your terminal or command prompt:

   ```bash
   pip install flask
   ```

2. Open a new file and save it as `app.py`.

   ```bash
   cd ~/project
   touch app.py
   ```

3. Import the Flask module and create an instance of the Flask class:

   ```python
   from flask import Flask

   app = Flask(__name__)
   ```
