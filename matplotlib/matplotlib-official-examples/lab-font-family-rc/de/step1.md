# Standard-Schriftart ohne Serifen auswählen

Die Standard-Schriftfamilie in Matplotlib ist die Schriftart ohne Serifen. Wir können die Standard-Schriftfamilie verwenden, indem wir den Parameter `font.family` auf `'sans-serif'` setzen. Dazu können wir folgenden Code verwenden:

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
```
