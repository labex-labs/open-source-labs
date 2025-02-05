# 线性回归

在这一步中，我们将探索线性回归的概念，以及如何使用scikit-learn来实现它。我们将使用糖尿病数据集，该数据集包含患者的生理变量以及他们一年后的疾病进展情况。

#### 加载糖尿病数据集

```python
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]
```

#### 创建并拟合线性回归模型

```python
from sklearn import linear_model

regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)
```

#### 进行预测并计算性能指标

```python
predictions = regr.predict(diabetes_X_test)
mse = np.mean((predictions - diabetes_y_test)**2)
variance_score = regr.score(diabetes_X_test, diabetes_y_test)
```
