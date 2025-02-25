# Tracez un cercle avec un rapport d'aspect d'axes inégal

Nous allons tout d'abord tracer un cercle avec un rapport d'aspect d'axes inégal pour démontrer l'importance de définir des rapports d'aspect d'axes égaux.

```python
an = np.linspace(0, 2 * np.pi, 100)
fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(3 * np.cos(an), 3 * np.sin(an))
axs[0, 0].set_title('not equal, looks like ellipse', fontsize=10)
```

La courbe résultante montrera un cercle qui semble allongé en raison du rapport d'aspect d'axes inégal.
