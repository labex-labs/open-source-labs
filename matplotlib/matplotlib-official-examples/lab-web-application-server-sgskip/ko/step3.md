# Flask 애플리케이션 생성

이 단계에서는 Flask 애플리케이션을 생성합니다. 홈 페이지 (`"/"`) 에 대한 라우트와 Matplotlib 그림을 생성하고 임베드하는 함수를 정의합니다.

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
