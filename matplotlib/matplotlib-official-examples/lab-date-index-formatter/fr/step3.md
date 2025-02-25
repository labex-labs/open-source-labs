# Création d'un formateur d'index personnalisé

Pour tracer les données en fonction d'un index allant de 0, 1,... len(data), nous allons créer un formateur d'index personnalisé. Ce formateur formatera les repères d'échelle en tant que dates au lieu d'entiers.

```python
# Créer un formateur d'index personnalisé
fig, ax2 = plt.subplots(figsize=(6, 3))
ax2.plot(r.adj_close, 'o-')

# Formater l'axe x en tant que dates
def format_date(x, _):
    try:
        # convertir datetime64 en datetime, et utiliser la méthode strftime de datetime :
        return r.date[round(x)].item().strftime('%a')
    except IndexError:
        pass

ax2.set_title("Creating Custom Index Formatter")
ax2.xaxis.set_major_formatter(format_date)  # crée internement un FuncFormatter
```
