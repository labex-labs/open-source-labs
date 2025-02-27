# Tracez les distributions des cibles

Nous traçons les fonctions de densité de probabilité de la cible avant et après avoir appliqué les fonctions logarithmiques.

```python
f, (ax0, ax1) = plt.subplots(1, 2)

ax0.hist(y, bins=100, density=True)
ax0.set_xlim([0, 2000])
ax0.set_ylabel("Probabilité")
ax0.set_xlabel("Cible")
ax0.set_title("Distribution de la cible")

ax1.hist(y_trans, bins=100, density=True)
ax1.set_ylabel("Probabilité")
ax1.set_xlabel("Cible")
ax1.set_title("Distribution de la cible transformée")

f.suptitle("Données synthétiques", y=1.05)
plt.tight_layout()
```
