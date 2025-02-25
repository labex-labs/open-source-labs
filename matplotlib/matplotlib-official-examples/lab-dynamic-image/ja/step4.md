# データを生成する

アニメーション用のデータを生成するために、Numpy ライブラリの `linspace` メソッドを使用します。2 セットのデータ、すなわち x と y を生成し、その後 y データを整形して 2 次元配列を作成します。

```python
x = np.linspace(0, 2 * np.pi, 120)
y = np.linspace(0, 2 * np.pi, 100).reshape(-1, 1)
```
