# Lade die Finanzdaten

Zunächst müssen wir einige Finanzdaten zum Aktienpreis von Google mithilfe der Matplotlib-Funktion `cbook.get_sample_data()` laden. Wir werden die Daten der letzten 250 Tage verwenden.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# Lade einige Finanzdaten; Google's Aktienpreis
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)
r = r[-250:]  # bekomme die letzten 250 Tage
```
