# データセットを読み込む

次に、アヤメ（Iris）データセットを読み込みます。このデータセットには、3 種類のアヤメの花の 4 つの特徴に関する情報が含まれています。このデータセットを使用して、決定木（Decision Tree）分類器を訓練します。

```python
# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target
```
