# Beschriftungen hinzufügen und Layout anpassen

Fügen Sie einem Titel und Achsenbeschriftungen zu den Teilplots hinzu, indem Sie die Funktionen title, xlabel und ylabel aus matplotlib.pyplot verwenden. Anpassen Sie das Layout der Teilplots mit der tight_layout-Funktion.

```python
axs[0].set_title('Cosine with Radian X-Axis')
axs[0].set_xlabel('Radians')
axs[0].set_ylabel('Cosine')
axs[1].set_title('Cosine with Degree X-Axis')
axs[1].set_xlabel('Degrees')
axs[1].set_ylabel('Cosine')
fig.tight_layout()
```
