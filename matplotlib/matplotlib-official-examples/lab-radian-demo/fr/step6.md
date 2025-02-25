# Ajoutez des étiquettes et ajustez la mise en page

Ajoutez un titre et des étiquettes d'axe aux sous-graphiques à l'aide des fonctions title, xlabel et ylabel de matplotlib.pyplot. Ajustez la mise en page des sous-graphiques à l'aide de la fonction tight_layout.

```python
axs[0].set_title('Cosine with Radian X-Axis')
axs[0].set_xlabel('Radians')
axs[0].set_ylabel('Cosine')
axs[1].set_title('Cosine with Degree X-Axis')
axs[1].set_xlabel('Degrees')
axs[1].set_ylabel('Cosine')
fig.tight_layout()
```
