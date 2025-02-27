# Usar LassoCV para comprobar la selección de alfa

Finalmente, usaremos LassoCV para ver cuánto podemos confiar en la selección de alfa. Usaremos KFold con 3 pliegues.

```python
from sklearn.linear_model import LassoCV
from sklearn.model_selection import KFold

lasso_cv = LassoCV(alphas=alphas, random_state=0, max_iter=10000)
k_fold = KFold(3)

print("Respuesta a la pregunta extra:","¿hasta qué punto puedes confiar en la selección de alfa?")
print()
print("Parámetros de alfa que maximizan la puntuación de generalización en diferentes")
print("subconjuntos de los datos:")
for k, (train, test) in enumerate(k_fold.split(X, y)):
    lasso_cv.fit(X[train], y[train])
    print(
        "[pliegue {0}] alfa: {1:.5f}, puntuación: {2:.5f}".format(
            k, lasso_cv.alpha_, lasso_cv.score(X[test], y[test])
        )
    )

print()
print("Respuesta: No mucho, ya que obtuvimos diferentes valores de alfa para diferentes")
print("subconjuntos de los datos y, además, las puntuaciones para estos alfas difieren")
print("bastante sustancialmente.")
```
