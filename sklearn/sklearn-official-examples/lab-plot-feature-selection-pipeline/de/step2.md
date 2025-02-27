# Pipeline erstellen

Wir werden jetzt eine Pipeline erstellen, die aus zwei Schritten besteht: Feature-Selektion und SVM-Klassifikation. Wir werden die `SelectKBest`-Funktion von Scikit-learn für die Feature-Selektion und die `LinearSVC`-Funktion von Scikit-learn für die SVM-Klassifikation verwenden. Die `SelectKBest`-Funktion wählt die `k` am besten informativen Features basierend auf der `f_classif`-Methode, die den ANOVA-F-Wert zwischen jedem Feature und der Zielvariable berechnet. Wir werden in diesem Beispiel `k = 3` setzen.

```python
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC

anova_filter = SelectKBest(f_classif, k=3)
clf = LinearSVC(dual="auto")
anova_svm = make_pipeline(anova_filter, clf)
```
