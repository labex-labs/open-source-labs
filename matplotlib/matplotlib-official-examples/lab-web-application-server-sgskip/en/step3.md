# Create the Flask Application

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
