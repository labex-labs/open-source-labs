# Connectez le graphique camembert et le graphique en barres

Enfin, nous connectons le graphique camembert et le graphique en barres en utilisant `ConnectionPatch` :

```python
# utilisez ConnectionPatch pour tracer des lignes entre les deux graphiques
theta1, theta2 = tranchees[0].theta1, tranchees[0].theta2
centre, r = tranchees[0].centre, tranchees[0].r
hauteur_barre = sum(rapports_âge)

# tracez la ligne de connexion supérieure
x = r * np.cos(np.pi / 180 * theta2) + centre[0]
y = r * np.sin(np.pi / 180 * theta2) + centre[1]
con = ConnectionPatch(xyA=(-largeur / 2, hauteur_barre), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
con.set_color([0, 0, 0])
con.set_linewidth(4)
ax2.add_artist(con)

# tracez la ligne de connexion inférieure
x = r * np.cos(np.pi / 180 * theta1) + centre[0]
y = r * np.sin(np.pi / 180 * theta1) + centre[1]
con = ConnectionPatch(xyA=(-largeur / 2, 0), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
con.set_color([0, 0, 0])
ax2.add_artist(con)
con.set_linewidth(4)
```
