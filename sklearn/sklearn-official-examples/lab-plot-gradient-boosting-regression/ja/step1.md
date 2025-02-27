# データの読み込み

まず、糖尿病データセットを読み込みます。

```python
diabetes = datasets.load_diabetes()
X, y = diabetes.data, diabetes.target
```
