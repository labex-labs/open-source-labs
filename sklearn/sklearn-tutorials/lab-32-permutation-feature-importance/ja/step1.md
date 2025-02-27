# データセットの読み込み

まず、予測モデルを訓練するために使用できるデータセットを読み込む必要があります。scikit - learnのDiabetesデータセットを使用します。このデータセットには糖尿病患者に関する情報が含まれています。

```python
from sklearn.datasets import load_diabetes

# Load the Diabetes dataset
diabetes = load_diabetes()

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(diabetes.data, diabetes.target, random_state=0)
```
