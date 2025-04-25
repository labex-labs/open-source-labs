# Self-training 分類器をセットアップする

異なる割合のラベル付きデータ（30％と 50％）を持つ 2 つの Self-training 分類器をセットアップします。Self-training は、半教師あり学習アルゴリズムであり、ラベル付きデータ上で分類器を訓練し、その後、それを使って非ラベル付きデータのラベルを予測します。最も確信度の高い予測結果をラベル付きデータに追加し、収束するまでこのプロセスを繰り返します。

```python
from sklearn.semi_supervised import SelfTrainingClassifier
from sklearn.svm import SVC

# Set up the Self-training classifiers
base_classifier = SVC(kernel="rbf", gamma=0.5, probability=True)
st30 = (
    SelfTrainingClassifier(base_classifier).fit(X, y_30),
    y_30,
    "Self-training 30% data",
)
st50 = (
    SelfTrainingClassifier(base_classifier).fit(X, y_50),
    y_50,
    "Self-training 50% data",
)
```
