# Text im Diagramm setzen

Als nächstes werden wir den Text im Diagramm mit der `text()`-Funktion setzen. Wir werden das `math_fontfamily`-Parameter verwenden, um die Schriftfamilie für jedes einzelne Textelement zu ändern.

```python
# Ein Text, der normalen Text und mathematischen Text mischt.
msg = (r"Normaler Text. $Text\ in\ math\ mode:\ "
       r"\int_{0}^{\infty } x^2 dx$")

# Setzen Sie den Text im Diagramm.
ax.text(1, 7, msg, size=12, math_fontfamily='cm')

# Setzen Sie eine andere Schriftart für den nächsten Text.
ax.text(1, 3, msg, size=12, math_fontfamily='dejavuserif')
```
