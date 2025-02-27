# Construire le pipeline

Nous allons maintenant construire un pipeline qui consiste en deux étapes : la sélection de caractéristiques et la classification SVM. Nous utiliserons la fonction `SelectKBest` de Scikit-learn pour la sélection de caractéristiques, et la fonction `LinearSVC` de Scikit-learn pour la classification SVM. La fonction `SelectKBest` sélectionne les `k` caractéristiques les plus informatives sur la base de la méthode `f_classif`, qui calcule la valeur F de l'ANOVA entre chaque caractéristique et la variable cible. Nous définirons `k = 3` dans cet exemple.

```python
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.pipeline import make_pipeline
from sklearn.svm import LinearSVC

anova_filter = SelectKBest(f_classif, k=3)
clf = LinearSVC(dual="auto")
anova_svm = make_pipeline(anova_filter, clf)
```
