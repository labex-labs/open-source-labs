# 加载数据集

首先，我们需要加载一个可用于训练预测模型的数据集。我们将使用 scikit-learn 中的糖尿病数据集，其中包含糖尿病患者的信息。

```python
from sklearn.datasets import load_diabetes

# 加载糖尿病数据集
diabetes = load_diabetes()

# 将数据拆分为训练集和验证集
X_train, X_val, y_train, y_val = train_test_split(diabetes.data, diabetes.target, random_state=0)
```
