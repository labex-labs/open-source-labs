# Bewerten der Merkmalswichtigkeit

Wir bewerten die Merkmalswichtigkeit basierend auf der durchschnittlichen Abnahme der Unreinheit (MDI). Die Merkmalswichtigkeiten werden durch das angepasste Attribut `feature_importances_` bereitgestellt und berechnet sich als Mittelwert und Standardabweichung der Akkumulation der Unreinheitsabnahme innerhalb jedes Baumes.

```python
import time
import matplotlib.pyplot as plt

start_time = time.time()
img_shape = data.images[0].shape
importances = forest.feature_importances_
elapsed_time = time.time() - start_time

print(f"Elapsed time to compute the importances: {elapsed_time:.3f} seconds")
imp_reshaped = importances.reshape(img_shape)
plt.matshow(imp_reshaped, cmap=plt.cm.hot)
plt.title("Pixel importances using impurity values")
plt.colorbar()
plt.show()
```
