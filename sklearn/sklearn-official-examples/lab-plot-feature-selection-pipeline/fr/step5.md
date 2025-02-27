# Vérifier le pipeline

Nous pouvons examiner le pipeline pour mieux comprendre le modèle. Nous pouvons utiliser l'index des caractéristiques sélectionnées pour récupérer les noms d'origine des caractéristiques.

```python
anova_svm[:-1].inverse_transform(anova_svm[-1].coef_)
```
