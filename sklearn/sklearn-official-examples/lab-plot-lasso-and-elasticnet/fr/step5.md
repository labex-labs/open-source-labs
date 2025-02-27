# Représentation graphique et analyse des résultats

Dans cette étape, nous utilisons une heatmap pour visualiser la rareté des coefficients réels et estimés des modèles linéaires respectifs.

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.colors import SymLogNorm

df = pd.DataFrame(
    {
        "Vraies coefficients": true_coef,
        "Lasso": lasso.coef_,
        "ARDRegression": ard.coef_,
        "ElasticNet": enet.coef_,
    }
)

plt.figure(figsize=(10, 6))
ax = sns.heatmap(
    df.T,
    norm=SymLogNorm(linthresh=10e-4, vmin=-1, vmax=1),
    cbar_kws={"label": "Valeurs des coefficients"},
    cmap="seismic_r",
)
plt.ylabel("Modèle linéaire")
plt.xlabel("Coefficients")
plt.title(
    f"Coefficients des modèles\nLasso $R^2$: {r2_score_lasso:.3f}, "
    f"ARD $R^2$: {r2_score_ard:.3f}, "
    f"ElasticNet $R^2$: {r2_score_enet:.3f}"
)
plt.tight_layout()
```
