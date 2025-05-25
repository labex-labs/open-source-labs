# Escolha da Fonte Monospace Padrão

A fonte monospace padrão no Matplotlib é determinada pelo sistema operacional. Podemos optar por usar a fonte monospace padrão definindo o parâmetro `font.family` como `'monospace'`. Para fazer isso, podemos usar o seguinte código:

```python
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "monospace"
```
