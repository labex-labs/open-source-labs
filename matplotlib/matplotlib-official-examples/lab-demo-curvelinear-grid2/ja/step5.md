# グラフを作成する

最後のステップは、`plt.figure`関数を使ってグラフを作成することです。グラフのサイズを(7, 4)に設定し、2 - 4のステップで作成した`curvelinear_test1`関数を呼び出します。

```python
if __name__ == "__main__":
    fig = plt.figure(figsize=(7, 4))
    curvelinear_test1(fig)
    plt.show()
```
