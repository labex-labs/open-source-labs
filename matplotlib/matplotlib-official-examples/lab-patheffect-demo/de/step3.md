# Strich-Effekt zu Konturlinien hinzufügen

Wir können auch Strich-Effekte zu Konturlinien und ihren Beschriftungen hinzufügen, indem wir den `withStroke`-Pfadeffekt verwenden.

```python
# Create plot and add contour lines with stroke effect
fig, ax = plt.subplots()
ax.imshow(arr)
cntr = ax.contour(arr, colors="k")

plt.setp(cntr.collections, path_effects=[
    patheffects.withStroke(linewidth=3, foreground="w")])

clbls = ax.clabel(cntr, fmt="%2.0f", use_clabeltext=True)
plt.setp(clbls, path_effects=[
    patheffects.withStroke(linewidth=3, foreground="w")])

plt.show()
```
