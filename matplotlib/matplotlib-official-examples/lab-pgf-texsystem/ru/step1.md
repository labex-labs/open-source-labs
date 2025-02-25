# Импортируем Matplotlib и настраиваем параметр pgf.texsystem

Сначала вам нужно импортировать библиотеку Matplotlib и установить параметр `pgf.texsystem` на `pdflatex`. Этот параметр позволяет использовать LaTeX для настройки семейства шрифтов в вашем графике.

```python
import matplotlib.pyplot as plt

plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
})
```
