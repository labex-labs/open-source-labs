# Habilitando Copy-On-Write

Primeiramente, vamos habilitar o CoW no pandas. Isso pode ser feito usando a opção de configuração `copy_on_write` no pandas. Aqui estão duas maneiras de habilitar o CoW globalmente.

```python
# Importing the pandas and numpy libraries
import pandas as pd

# Enable CoW using set_option
pd.set_option("mode.copy_on_write", True)

# Or using direct assignment
pd.options.mode.copy_on_write = True
```
