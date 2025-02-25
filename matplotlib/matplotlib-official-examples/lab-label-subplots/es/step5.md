# Etiquetar con título

Si queremos que la etiqueta quede alineada con el título, podemos incorporarla al título o usar el argumento de palabras clave `loc`.

```python
for label, ax in axs.items():
    ax.set_title('Normal Title', fontstyle='italic')
    ax.set_title(label, fontfamily='serif', loc='left', fontsize='medium')
```
