# Flask アプリケーションの作成

このステップでは、Flask アプリケーションを作成します。ホームページ (`"/"`) 用のルートと、Matplotlib のグラフを生成して埋め込む関数を定義します。

```python
app = Flask(__name__)

@app.route("/")
def home():
    # pyplot を使わずにグラフを生成します。
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])
    # 一時的なバッファに保存します。
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # 結果を html 出力に埋め込みます。
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64,{data}'/>"
```
