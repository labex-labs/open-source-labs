# Projektieren von Konturprofilen

Wir werden nun die Konturprofile auf die Wände des Graphen projizieren. Dies wird mit der `contourf`-Methode durchgeführt. Wir werden den `zdir`-Parameter auf 'z', 'x' und 'y' setzen, um die Konturprofile auf die z-, x- und y-Wände respective zu projizieren. Wir werden auch den `offset`-Parameter setzen, um den passenden Achsengrenzen zu entsprechen.

```python
ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap='coolwarm')
ax.contourf(X, Y, Z, zdir='y', offset=40, cmap='coolwarm')
```
