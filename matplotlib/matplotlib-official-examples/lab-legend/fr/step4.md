# Ajout de la légende

Pour ajouter la légende à notre graphique, nous utilisons la fonction `legend` de Matplotlib. Nous passons le paramètre `loc` pour spécifier l'emplacement de la légende et le paramètre `shadow` pour ajouter un effet d'ombre à la légende. Nous utilisons également le paramètre `fontsize` pour définir la taille de police de la légende.

```python
legend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')
```
