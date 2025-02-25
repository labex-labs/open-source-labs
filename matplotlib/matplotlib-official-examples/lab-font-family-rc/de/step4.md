# Einen bestimmten Monospaced-Schriftart auswählen

Wenn wir eine bestimmte Monospaced-Schriftart verwenden möchten, können wir den Parameter `font.monospace` auf eine Liste von Schriftnamen setzen. Matplotlib wird versuchen, die erste Schrift in der Liste zu verwenden, die auf dem System des Benutzers verfügbar ist. Dazu können wir folgenden Code verwenden:

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "monospace"
plt.rcParams["font.monospace"] = ["FreeMono"]
```
