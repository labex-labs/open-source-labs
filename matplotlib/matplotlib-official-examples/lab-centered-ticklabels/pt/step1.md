# Carregar os Dados Financeiros

Primeiramente, precisamos carregar alguns dados financeiros do preço das ações do Google usando a função `cbook.get_sample_data()` do Matplotlib. Usaremos os últimos 250 dias de dados.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# Carrega alguns dados financeiros; preço das ações do Google
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
r = r[-250:]  # obtém os últimos 250 dias
```
