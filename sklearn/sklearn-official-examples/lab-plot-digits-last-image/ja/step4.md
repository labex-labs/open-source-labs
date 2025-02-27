# 機械学習モデルの学習

これでデータセットが準備できたので、訓練用データを使って機械学習モデルを学習させることができます。この例では、サポートベクターマシン（SVM）アルゴリズムを使います。

```python
from sklearn.svm import SVC

# Create the SVM classifier
clf = SVC(kernel='linear')

# Train the classifier on the training data
clf.fit(X_train, y_train)
```
