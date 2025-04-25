# 创建 Flask 应用程序

在这一步中，我们将创建 Flask 应用程序。我们将为主页（`"/"`）定义一个路由，并定义一个用于生成和嵌入 Matplotlib 图形的函数。

```python
app = Flask(__name__)

@app.route("/")
def home():
    # 不使用 pyplot 生成图形。
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    # 将其保存到临时缓冲区。
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # 将结果嵌入到 html 输出中。
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"
```
