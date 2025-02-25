# Zeichnen eines Kreises mit gleichem Achsenverhältnis

Um das gleiche Achsenverhältnis einzustellen, können wir die Funktion `axis('equal')` verwenden.

```python
axs[0, 1].plot(3 * np.cos(an), 3 * np.sin(an))
axs[0, 1].axis('equal')
axs[0, 1].set_title('gleich, sieht aus wie Kreis', fontsize=10)
```

Das resultierende Diagramm wird einen proportionalen und visuell ansprechenden Kreis zeigen.
