# SimpleImputerを使った単変量特徴量の欠損値補完

`SimpleImputer`クラスは、単変量の方法で欠損値を補完するための基本的な戦略を提供します。欠損値を定数値で置き換えるか、各列の平均値、中央値、または最頻値を使って欠損値を補完するなど、さまざまな戦略から選ぶことができます。

まず平均戦略を考えてみましょう。`SimpleImputer`のインスタンスを作成し、データに適合させて欠損値補完戦略を学習します。その後、学習した戦略に基づいて欠損値を補完するために`transform`メソッドを使用できます。

```python
imp = SimpleImputer(strategy='mean')
X = [[1, 2], [np.nan, 3], [7, 6]]
imp.fit(X)
X_test = [[np.nan, 2], [6, np.nan], [7, 6]]
imputed_X_test = imp.transform(X_test)
```
