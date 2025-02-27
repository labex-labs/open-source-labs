# パイプラインの構築

ここでは、特徴選択と SVM 分類の 2 つのステップからなるパイプラインを構築します。特徴選択には Scikit-learn の `SelectKBest` 関数を、SVM 分類には Scikit-learn の `LinearSVC` 関数を使用します。`SelectKBest` 関数は、各特徴と目的変数の間の ANOVA F 値を計算する `f_classif` メソッドに基づいて、最も情報量の多い `k` 個の特徴を選択します。この例では `k=3` と設定します。

```python
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC

anova_filter = SelectKBest(f_classif, k=3)
clf = LinearSVC(dual="auto")
anova_svm = make_pipeline(anova_filter, clf)
```
