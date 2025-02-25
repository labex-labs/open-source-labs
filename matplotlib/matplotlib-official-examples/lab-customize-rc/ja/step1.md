# デフォルトパラメータを設定する関数を作成する

グラフのデフォルトパラメータを設定する関数を作成するには、`rcParams.update()` メソッドを使用できます。このメソッドは、パラメータ名と値の辞書を受け取り、新しい値で現在のデフォルト値を更新します。以下は、出版物用のグラフにいくつかのデフォルトパラメータを設定する関数の例です：

```python
def set_pub():
    rcParams.update({
        "font.weight": "bold",  # 太字のフォント
        "tick.labelsize": 15,   # 大きな目盛りのラベル
        "lines.linewidth": 1,   # 太い線
        "lines.color": "k",     # 黒い線
        "grid.color": "0.5",    # 灰色のグリッド線
        "grid.linestyle": "-",  # 実線のグリッド線
        "grid.linewidth": 0.5,  # 細いグリッド線
        "savefig.dpi": 300,     # 解像度の高い出力。
    })
```
