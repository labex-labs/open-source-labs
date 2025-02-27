# Inspeccionar la Canalización

Podemos inspeccionar la canalización para entender mejor el modelo. Podemos utilizar el índice de las características seleccionadas para recuperar los nombres originales de las características.

```python
anova_svm[:-1].inverse_transform(anova_svm[-1].coef_)
```
