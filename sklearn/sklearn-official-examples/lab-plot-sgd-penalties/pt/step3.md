# Aplicando Penalidade L1

Agora aplicaremos a penalidade L1 aos nossos dados usando o `SGDClassifier`.

```python
# Criar um classificador com penalidade L1
clf = SGDClassifier(loss='hinge', penalty='l1', alpha=0.05, max_iter=1000, tol=1e-3)

# Ajustar o modelo
clf.fit(X, y)

# Plotar o limite de decisão
plt.scatter(X[:, 0], X[:, 1], c=y)
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()
xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], 201), np.linspace(ylim[0], ylim[1], 201))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
ax.contour(xx, yy, Z, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])
ax.set_xlim(xlim)
ax.set_ylim(ylim)
plt.title('Penalidade L1')
plt.show()
```
