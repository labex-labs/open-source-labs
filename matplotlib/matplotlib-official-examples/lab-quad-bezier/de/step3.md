# Das PathPatch-Objekt erstellen

Jetzt, da wir das `Path`-Objekt haben, können wir das `PathPatch`-Objekt erstellen, das zur Zeichnung der Bézier-Kurve im Diagramm verwendet werden wird. Wir werden die `facecolor` auf `'none'` setzen, sodass nur die Kurve gezeichnet und nicht ausgefüllt wird.

```python
bezier_patch = mpatches.PathPatch(bezier_path, fc="none")
```
