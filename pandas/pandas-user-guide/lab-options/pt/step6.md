# Definindo Opções de Inicialização

Podemos criar um script de inicialização no ambiente Python/IPython para importar pandas e definir opções, o que torna o trabalho com pandas mais eficiente.

```python
# Este é um exemplo de um script de inicialização
# Coloque isso em um arquivo .py no diretório de inicialização do perfil IPython
import pandas as pd

pd.set_option("display.max_rows", 999)
pd.set_option("display.precision", 5)
```
