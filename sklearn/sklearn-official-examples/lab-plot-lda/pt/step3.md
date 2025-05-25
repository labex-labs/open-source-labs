# Treinar e Testar Classificadores

Vamos treinar e testar cada classificador para ver como eles se comportam nos dados gerados. Repetimos este processo várias vezes para obter uma pontuação média de precisão.

```python
n_train = 20  # amostras para treino
n_test = 200  # amostras para teste
n_averages = 50  # quantas vezes repetir a classificação
n_features_max = 75  # número máximo de recursos
step = 4  # tamanho do passo para o cálculo

acc_clf1, acc_clf2, acc_clf3 = [], [], []
n_features_range = range(1, n_features_max + 1, step)

for n_features in n_features_range:
    score_clf1, score_clf2, score_clf3 = 0, 0, 0
    for _ in range(n_averages):
        X, y = generate_data(n_train, n_features)

        clf1.fit(X, y)
        clf2.fit(X, y)
        clf3.fit(X, y)

        X, y = generate_data(n_test, n_features)
        score_clf1 += clf1.score(X, y)
        score_clf2 += clf2.score(X, y)
        score_clf3 += clf3.score(X, y)

    acc_clf1.append(score_clf1 / n_averages)
    acc_clf2.append(score_clf2 / n_averages)
    acc_clf3.append(score_clf3 / n_averages)
```
