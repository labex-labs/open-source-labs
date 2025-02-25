# プロットの作成

次に、`LassoManager` クラスを使ってインタラクティブなプロットを作成します。`np.random.rand` 関数を使って、描画するランダムなデータポイントを生成します。

```python
if __name__ == '__main__':
    np.random.seed(19680801)
    ax = plt.figure().add_subplot(
        xlim=(0, 1), ylim=(0, 1), title='Lasso points using left mouse button')
    manager = LassoManager(ax, np.random.rand(100, 2))
    plt.show()
```
