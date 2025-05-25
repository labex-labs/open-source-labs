# Imputação de recursos univariados usando SimpleImputer

A classe `SimpleImputer` fornece estratégias básicas para imputar valores ausentes de forma univariada. Podemos escolher entre diferentes estratégias, como substituir valores ausentes por um valor constante ou usar a média, mediana ou valor mais frequente de cada coluna para imputar os valores ausentes.

Vamos começar considerando a estratégia da média. Criaremos uma instância de `SimpleImputer` e a ajustaremos aos nossos dados para aprender a estratégia de imputação. Em seguida, podemos usar o método `transform` para imputar os valores ausentes com base na estratégia aprendida.

```python
imp = SimpleImputer(strategy='mean')
X = [[1, 2], [np.nan, 3], [7, 6]]
imp.fit(X)
X_test = [[np.nan, 2], [6, np.nan], [7, 6]]
imputed_X_test = imp.transform(X_test)
```
