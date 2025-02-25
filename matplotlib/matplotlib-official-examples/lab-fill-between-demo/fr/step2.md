# Bandes de confiance

Une application courante de `fill_between` est l'indication des bandes de confiance. `fill_between` utilise les couleurs du cycle de couleurs comme couleur de remplissage. Il est donc souvent une bonne pratique d'alléger la couleur en rendant la zone semi-transparente à l'aide de `alpha`.

```python
N = 21
x = np.linspace(0, 10, 11)
y = [3.9, 4.4, 10.8, 10.3, 11.2, 13.1, 14.1,  9.9, 13.9, 15.1, 12.5]

# ajuster une courbe linéaire et estimer ses valeurs de y et leur erreur.
a, b = np.polyfit(x, y, deg=1)
y_est = a * x + b
y_err = x.std() * np.sqrt(1/len(x) +
                          (x - x.mean())**2 / np.sum((x - x.mean())**2))

fig, ax = plt.subplots()
ax.plot(x, y_est, '-')
ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.2)
ax.plot(x, y, 'o', color='tab:brown')
```
