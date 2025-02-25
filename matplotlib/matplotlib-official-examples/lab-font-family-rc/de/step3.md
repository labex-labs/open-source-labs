# Standard-Monospaced-Schriftart auswählen

Die Standard-Monospaced-Schriftart in Matplotlib wird vom Betriebssystem bestimmt. Wir können die Standard-Monospaced-Schriftart verwenden, indem wir den Parameter `font.family` auf `'monospace'` setzen. Dazu können wir folgenden Code verwenden:

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "monospace"
```
