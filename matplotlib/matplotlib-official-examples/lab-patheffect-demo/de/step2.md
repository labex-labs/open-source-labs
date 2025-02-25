# Strich-Effekt zum Text hinzufügen

Wir können einen Strich-Effekt zum Text hinzufügen, indem wir den `withStroke`-Pfadeffekt verwenden. In diesem Beispiel werden wir einen Strich-Effekt zum Text-Annotation im Graphen hinzufügen.

```python
# Create plot and add text annotation with stroke effect
fig, ax = plt.subplots()
ax.imshow(arr)
txt = ax.annotate("test", (1., 1.), (0., 0),
                   arrowprops=dict(arrowstyle="->",
                                   connectionstyle="angle3", lw=2),
                   size=20, ha="center",
                   path_effects=[patheffects.withStroke(linewidth=3,
                                                        foreground="w")])
txt.arrow_patch.set_path_effects([
    patheffects.Stroke(linewidth=5, foreground="w"),
    patheffects.Normal()])

# Add grid with stroke effect
pe = [patheffects.withStroke(linewidth=3,
                             foreground="w")]
ax.grid(True, linestyle="-", path_effects=pe)

plt.show()
```
