# Visualisiere die Segmentierung

Wir werden die resultierenden Regionen visualisieren, indem wir das ursprüngliche Bild plotten und die Konturen der segmentierten Regionen darüber legen.

```python
plt.figure(figsize=(5, 5))
plt.imshow(rescaled_coins, cmap=plt.cm.gray)
plt.xticks(())
plt.yticks(())
title = "Spectral clustering: %s, %.2fs" % (assign_labels, (t1 - t0))
print(title)
plt.title(title)
for l in range(n_regions):
    colors = [plt.cm.nipy_spectral((l + 4) / float(n_regions + 4))]
    plt.contour(labels == l, colors=colors)
plt.show()
```
