# Erstellen des Plots

Wir werden den Plot erstellen und das `PathPatch` zum Plot hinzufügen. Wir werden den Titel des Plots auf `'A Compound Path'` setzen.

```python
fig, ax = plt.subplots()
ax.add_patch(pathpatch)
ax.set_title('A Compound Path')

ax.autoscale_view()

plt.show()
```
