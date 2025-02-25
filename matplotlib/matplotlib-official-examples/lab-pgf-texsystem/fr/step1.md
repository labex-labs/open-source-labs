# Import Matplotlib et définir le paramètre pgf.texsystem

Tout d'abord, vous devez importer la bibliothèque Matplotlib et définir le paramètre `pgf.texsystem` sur `pdflatex`. Ce paramètre vous permet d'utiliser LaTeX pour personnaliser la famille de polices de votre graphique.

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
})
```
