# Importar Dependências

Nesta etapa, importaremos as dependências necessárias. Usaremos `base64` para codificar os dados da imagem, `BytesIO` para armazenar os dados da imagem na memória, `Flask` para criar o servidor da aplicação web e `Figure` para criar as figuras.

```python
import base64
from io import BytesIO

from flask import Flask

from matplotlib.figure import Figure
```
