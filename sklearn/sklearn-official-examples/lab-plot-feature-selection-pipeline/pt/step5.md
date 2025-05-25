# Inspecionar o Pipeline

Podemos inspecionar o pipeline para melhor compreender o modelo. Podemos usar o índice dos recursos selecionados para recuperar os nomes dos recursos originais.

```python
anova_svm[:-1].inverse_transform(anova_svm[-1].coef_)
```
