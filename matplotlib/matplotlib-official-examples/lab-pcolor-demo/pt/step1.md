# Demonstração Simples de `Pcolor`

O primeiro passo é criar uma demonstração simples de `Pcolor`. Isso mostrará como criar um gráfico `Pcolor` básico.

```python
Z = np.random.rand(6, 10)

fig, (ax0, ax1) = plt.subplots(2, 1)

c = ax0.pcolor(Z)
ax0.set_title('default: no edges')

c = ax1.pcolor(Z, edgecolors='k', linewidths=4)
ax1.set_title('thick edges')

fig.tight_layout()
plt.show()
```
