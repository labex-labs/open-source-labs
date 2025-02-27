# スコアと交差検証スコア

scikit-learn の推定器は、新しいデータに対するモデルの適合度または予測の品質を評価するために使用できる `score` メソッドを公開しています。このメソッドはスコアを返し、値が高いほど性能が良いことを示します。

```python
from sklearn import datasets, svm

# 手書き数字のデータセットを読み込む
X_digits, y_digits = datasets.load_digits(return_X_y=True)

# 線形カーネルを持つ SVM 分類器を作成する
svc = svm.SVC(C=1, kernel='linear')

# 分類器を学習データに適合させ、テストデータでのスコアを計算する
score = svc.fit(X_digits[:-100], y_digits[:-100]).score(X_digits[-100:], y_digits[-100:])
```

予測精度のより良い尺度を得るために、交差検証を使用できます。交差検証では、データを複数のフォールドに分割し、各フォールドをテストセットとして、残りのフォールドを学習セットとして使用します。このプロセスを複数回繰り返し、スコアを平均化して全体的な性能を得ます。

```python
import numpy as np

# データを 3 つのフォールドに分割する
X_folds = np.array_split(X_digits, 3)
y_folds = np.array_split(y_digits, 3)

# 交差検証を実行する
scores = []
for k in range(3):
    X_train = list(X_folds)
    X_test = X_train.pop(k)
    X_train = np.concatenate(X_train)
    y_train = list(y_folds)
    y_test = y_train.pop(k)
    y_train = np.concatenate(y_train)
    scores.append(svc.fit(X_train, y_train).score(X_test, y_test))

print(scores)
```
