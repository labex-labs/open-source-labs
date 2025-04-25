# データセットを分割する

決定木（Decision Tree）分類器を訓練する前に、データセットを訓練データセットとテストデータセットに分割する必要があります。データの 70% を訓練に、30% をテストに使用します。

```python
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
```
