# Anpassen von Legende-Elementen

Wir können die Legende-Elemente weiter anpassen, indem wir zusätzliche Argumente in der Methode `PathCollection.legend_elements` verwenden. Beispielsweise können wir die Anzahl der zu erstellenden Legende-Einträge angeben und wie sie beschriftet werden sollen.

```python
volume = np.random.rayleigh(27, size=40)
amount = np.random.poisson(10, size=40)
ranking = np.random.normal(size=40)
price = np.random.uniform(1, 10, size=40)

fig, ax = plt.subplots()

# Da der Preis zu klein ist, um als Größe für ``s`` verwendet zu werden,
# normalisieren wir ihn auf einige sinnvolle Punktgrößen, s=0.3*(price*3)**2
scatter = ax.scatter(volume, amount, c=ranking, s=0.3*(price*3)**2,
                     vmin=-3, vmax=3, cmap="Spectral")

# Erzeuge eine Legende für die Rangfolge (Farben). Auch wenn es 40 verschiedene
# Rangfolgen gibt, möchten wir nur 5 von ihnen in der Legende anzeigen.
legend1 = ax.legend(*scatter.legend_elements(num=5),
                    loc="upper left", title="Rangfolge")
ax.add_artist(legend1)

# Erzeuge eine Legende für den Preis (Größen). Da wir die Preise
# in Dollar anzeigen möchten, verwenden wir das *func*-Argument, um die Umkehrfunktion
# der Funktion bereitzustellen, die oben verwendet wurde, um die Größen zu berechnen.
# Das *fmt* stellt sicher, dass der Preis in Dollar angezeigt wird. Beachten Sie,
# wie wir hier auf 5 Elemente zielen, erhalten jedoch nur 4 in der erstellten
# Legende aufgrund der automatisch gerundeten Preise, die für uns gewählt werden.
kw = dict(prop="sizes", num=5, color=scatter.cmap(0.7), fmt="$ {x:.2f}",
          func=lambda s: np.sqrt(s/.3)/3)
legend2 = ax.legend(*scatter.legend_elements(**kw),
                    loc="lower right", title="Preis")

plt.show()
```
