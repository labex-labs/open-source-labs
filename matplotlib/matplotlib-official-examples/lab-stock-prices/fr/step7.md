# Tracez chaque action séparément avec sa propre couleur

```python
for nn, column in enumerate(stocks_ticker):
    # Tracez chaque ligne séparément avec sa propre couleur.
    # Ne pas inclure de données avec des valeurs NaN.
    good = np.nonzero(np.isfinite(stock_data[column]))
    line, = ax.plot(stock_data['Date'][good], stock_data[column][good], lw=2.5)

    # Ajoutez une étiquette de texte à l'extrémité droite de chaque ligne. La plupart du code ci-dessous
    # consiste à ajouter des décalages de position verticale car certaines étiquettes se chevauchaient.
    y_pos = stock_data[column][-1]

    # Utilisez une transformation de décalage, en points, pour tout texte qui doit être déplacé
    # vers le haut ou le bas.
    offset = y_offsets[column] / 72
    trans = mtransforms.ScaledTranslation(0, offset, fig.dpi_scale_trans)
    trans = ax.transData + trans

    # Encore une fois, assurez-vous que toutes les étiquettes sont suffisamment grandes pour être aisément lues
    # par le spectateur.
    ax.text(np.datetime64('2022-10-01'), y_pos, stocks_name[nn],
            color=line.get_color(), transform=trans)
```
