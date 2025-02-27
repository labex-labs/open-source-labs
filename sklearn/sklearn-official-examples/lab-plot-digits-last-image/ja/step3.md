# 機械学習用のデータセットの準備

データセットで機械学習モデルを学習させる前に、データを訓練用とテスト用のセットに分割することでデータを準備する必要があります。これは、scikit-learnの`train_test_split`関数を使って行うことができます。

```python
from sklearn.model_selection import train_test_split

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)
```
