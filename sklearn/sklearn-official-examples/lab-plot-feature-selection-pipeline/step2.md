# Build the Pipeline

We will now build a pipeline that consists of two steps: feature selection and SVM classification. We will use Scikit-learn's `SelectKBest` function for feature selection, and Scikit-learn's `LinearSVC` function for SVM classification. The `SelectKBest` function selects the `k` most informative features based on the `f_classif` method, which computes the ANOVA F-value between each feature and the target variable. We will set `k=3` in this example.

```python
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC

anova_filter = SelectKBest(f_classif, k=3)
clf = LinearSVC(dual="auto")
anova_svm = make_pipeline(anova_filter, clf)
```
