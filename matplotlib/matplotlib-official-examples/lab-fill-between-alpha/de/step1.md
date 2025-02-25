# Das Verbessern eines Liniendiagramms mit `fill_between`

Das erste Beispiel zeigt, wie man ein Liniendiagramm mit `fill_between` verbessert. Wir werden Finanzdaten von Google verwenden, um zwei Teilgraphen zu erstellen, einen mit einem einfachen Liniendiagramm und einen mit einem gefüllten Liniendiagramm.

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook as cbook

# ladet einige Beispiel-Finanzdaten
r = cbook.get_sample_data('goog.npz')['price_data'].view(np.recarray)

# erstellt zwei Teilgraphen mit den geteilten x- und y-Achsen
fig, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)

pricemin = r.close.min()

ax1.plot(r.date, r.close, lw=2)
ax2.fill_between(r.date, pricemin, r.close, alpha=0.7)

for ax in ax1, ax2:
    ax.grid(True)
    ax.label_outer()

ax1.set_ylabel('price')
fig.suptitle('Google (GOOG) daily closing price')
fig.autofmt_xdate()
```
