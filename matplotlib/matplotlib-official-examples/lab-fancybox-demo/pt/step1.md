# Importar bibliotecas e obter estilos de caixa

Nesta etapa, importaremos as bibliotecas necessárias e obteremos os estilos de caixa que usaremos para a plotagem.

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatch
from matplotlib.patches import FancyBboxPatch
import matplotlib.transforms as mtransforms
import inspect

styles = mpatch.BoxStyle.get_styles()
```
