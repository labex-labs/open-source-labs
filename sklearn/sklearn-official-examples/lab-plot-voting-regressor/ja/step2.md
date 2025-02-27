# 糖尿病データセットの読み込み

次に、scikit-learnが提供する`load_diabetes()`関数を使って、糖尿病データセットをプログラムに読み込みます。この関数は、2つの配列のタプルとしてデータセットを返します。1つは特徴データを含み、もう1つは目的変数データを含みます。これらの配列をそれぞれ`X`と`y`に割り当てます。

```python
# Load the diabetes dataset
X, y = load_diabetes(return_X_y=True)
```
