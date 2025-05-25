# Utilizar LassoCV para verificar a seleção de alfa

Finalmente, utilizaremos LassoCV para avaliar a confiabilidade da seleção de alfa. Usaremos KFold com 3 dobras.

```python
from sklearn.linear_model import LassoCV
from sklearn.model_selection import KFold

lasso_cv = LassoCV(alphas=alphas, random_state=0, max_iter=10000)
k_fold = KFold(3)

print("Resposta à pergunta bônus:", "quanto você pode confiar na seleção de alfa?")
print()
print("Parâmetros Alfa maximizando a pontuação de generalização em diferentes")
print("subconjuntos dos dados:")
for k, (train, test) in enumerate(k_fold.split(X, y)):
    lasso_cv.fit(X[train], y[train])
    print(
        "[dobra {0}] alfa: {1:.5f}, pontuação: {2:.5f}".format(
            k, lasso_cv.alpha_, lasso_cv.score(X[test], y[test])
        )
    )

print()
print("Resposta: Não muito, pois obtivemos alfas diferentes para diferentes")
print("subconjuntos dos dados e, além disso, as pontuações para esses alfas diferem")
print("consideravelmente.")
```
