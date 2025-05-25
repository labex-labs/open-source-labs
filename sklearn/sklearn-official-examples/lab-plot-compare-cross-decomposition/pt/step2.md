# PLS Canônico

Utilizamos o algoritmo PLS Canônico para transformar os dados. Em seguida, criamos um gráfico de dispersão das pontuações.

```python
from sklearn.cross_decomposition import PLSCanonical

plsca = PLSCanonical(n_components=2)
plsca.fit(X_train, Y_train)
X_train_r, Y_train_r = plsca.transform(X_train, Y_train)
X_test_r, Y_test_r = plsca.transform(X_test, Y_test)

import matplotlib.pyplot as plt

# No gráfico diagonal, plotamos as pontuações de X vs Y em cada componente
plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.scatter(X_train_r[:, 0], Y_train_r[:, 0], label="treino", marker="o", s=25)
plt.scatter(X_test_r[:, 0], Y_test_r[:, 0], label="teste", marker="o", s=25)
plt.xlabel("Pontuações x")
plt.ylabel("Pontuações y")
plt.title(
    "Comp. 1: X vs Y (corr. teste = %.2f)"
    % np.corrcoef(X_test_r[:, 0], Y_test_r[:, 0])[0, 1]
)
plt.xticks(())
plt.yticks(())
plt.legend(loc="best")

plt.subplot(224)
plt.scatter(X_train_r[:, 1], Y_train_r[:, 1], label="treino", marker="o", s=25)
plt.scatter(X_test_r[:, 1], Y_test_r[:, 1], label="teste", marker="o", s=25)
plt.xlabel("Pontuações x")
plt.ylabel("Pontuações y")
plt.title(
    "Comp. 2: X vs Y (corr. teste = %.2f)"
    % np.corrcoef(X_test_r[:, 1], Y_test_r[:, 1])[0, 1]
)
plt.xticks(())
plt.yticks(())
plt.legend(loc="best")

# Gráfico fora da diagonal, plotando os componentes 1 vs 2 para X e Y
plt.subplot(222)
plt.scatter(X_train_r[:, 0], X_train_r[:, 1], label="treino", marker="*", s=50)
plt.scatter(X_test_r[:, 0], X_test_r[:, 1], label="teste", marker="*", s=50)
plt.xlabel("Comp. 1 de X")
plt.ylabel("Comp. 2 de X")
plt.title(
    "Comp. 1 de X vs Comp. 2 de X (corr. teste = %.2f)"
    % np.corrcoef(X_test_r[:, 0], X_test_r[:, 1])[0, 1]
)
plt.legend(loc="best")
plt.xticks(())
plt.yticks(())

plt.subplot(223)
plt.scatter(Y_train_r[:, 0], Y_train_r[:, 1], label="treino", marker="*", s=50)
plt.scatter(Y_test_r[:, 0], Y_test_r[:, 1], label="teste", marker="*", s=50)
plt.xlabel("Comp. 1 de Y")
plt.ylabel("Comp. 2 de Y")
plt.title(
    "Comp. 1 de Y vs Comp. 2 de Y, (corr. teste = %.2f)"
    % np.corrcoef(Y_test_r[:, 0], Y_test_r[:, 1])[0, 1]
)
plt.legend(loc="best")
plt.xticks(())
plt.yticks(())
plt.show()
```
