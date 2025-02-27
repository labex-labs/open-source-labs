# 分類器の定義

ROC 曲線と DET 曲線を使用して閾値にわたる統計的性能を比較するために、2 つの異なる分類器を定義します。scikit-learn の `make_pipeline` 関数を使用して、`StandardScaler` を使用してデータをスケーリングし、`LinearSVC` 分類器を訓練するパイプラインを作成します。また、scikit-learn の `RandomForestClassifier` クラスを使用して、最大深さが 5、推定器が 10 個、最大特徴数が 1 個のランダムフォレスト分類器を訓練します。

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC

classifiers = {
    "Linear SVM": make_pipeline(StandardScaler(), LinearSVC(C=0.025, dual="auto")),
    "Random Forest": RandomForestClassifier(
        max_depth=5, n_estimators=10, max_features=1
    ),
}
```
