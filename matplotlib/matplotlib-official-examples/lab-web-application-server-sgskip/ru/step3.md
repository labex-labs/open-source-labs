# Создание веб-приложения Flask

В этом шаге мы создадим веб-приложение Flask. Мы определим маршрут для главной страницы (`"/"`) и функцию для генерации и встраивания графика Matplotlib.

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
