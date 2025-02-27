# Pipeline untersuchen

Wir können die Pipeline untersuchen, um das Modell besser zu verstehen. Wir können den Index der ausgewählten Features verwenden, um die ursprünglichen Feature-Namen abzurufen.

```python
anova_svm[:-1].inverse_transform(anova_svm[-1].coef_)
```
