# Fixer les limites et les étiquettes

Dans cette étape, nous fixons les limites et les étiquettes pour les axes principaux du graphique.

```python
main_ax.set_xlim(0, 1)
main_ax.set_ylim(1.1 * np.min(s), 2 * np.max(s))
main_ax.set_xlabel('time (s)')
main_ax.set_ylabel('current (nA)')
main_ax.set_title('Gaussian colored noise')
```
