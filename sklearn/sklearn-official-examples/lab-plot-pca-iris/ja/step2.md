# データセットを読み込む

次に、scikit-learnの`load_iris()`関数を使ってIrisデータセットを読み込みます。その後、特徴量（X）とターゲット（y）の変数を分離します。

```python
iris = datasets.load_iris()
X = iris.data
y = iris.target
```
