# Dataset

First, we will load the diabetes dataset using the `load_diabetes` function from `sklearn.datasets`. The dataset consists of 10 baseline variables, age, sex, body mass index, average blood pressure, and six blood serum measurements, and a quantitative measure of disease progression one year after baseline.

```python
from sklearn.datasets import load_diabetes

X, y = load_diabetes(return_X_y=True, as_frame=True)
X.head()
```
