# Évaluer l'importance des fonctionnalités

Nous évaluons l'importance des fonctionnalités en fonction de la diminution moyenne de l'impureté (MDI). L'importance des fonctionnalités est fournie par l'attribut ajusté `feature_importances_` et elles sont calculées comme la moyenne et l'écart-type de l'accumulation de la diminution d'impureté dans chaque arbre.

```python
import time
import matplotlib.pyplot as plt

start_time = time.time()
img_shape = data.images[0].shape
importances = forest.feature_importances_
elapsed_time = time.time() - start_time

print(f"Temps écoulé pour calculer les importances : {elapsed_time:.3f} secondes")
imp_reshaped = importances.reshape(img_shape)
plt.matshow(imp_reshaped, cmap=plt.cm.hot)
plt.title("Importances des pixels en utilisant les valeurs d'impureté")
plt.colorbar()
plt.show()
```
