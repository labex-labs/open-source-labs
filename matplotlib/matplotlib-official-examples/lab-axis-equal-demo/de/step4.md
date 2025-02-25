# Anpassen der Diagrammbegrenzungen unter Beibehaltung des gleichen Achsenverhältnisses

Wir können auch die Diagrammbegrenzungen anpassen, während das gleiche Achsenverhältnis beibehalten wird.

```python
axs[1, 0].plot(3 * np.cos(an), 3 * np.sin(an))
axs[1, 0].axis('equal')
axs[1, 0].set(xlim=(-3, 3), ylim=(-3, 3))
axs[1, 0].set_title('noch ein Kreis, auch nach Änderung der Begrenzungen', fontsize=10)
```

Das resultierende Diagramm wird einen Kreis zeigen, der auch nach der Änderung der Begrenzungen immer noch proportional ist.
