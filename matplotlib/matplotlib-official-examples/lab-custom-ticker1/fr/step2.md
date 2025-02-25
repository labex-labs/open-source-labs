# Définir la fonction d'indicateur personnalisé

Ensuite, nous devons définir la fonction d'indicateur personnalisé. La fonction d'indicateur personnalisé prend deux arguments - la valeur et la position de la graduation - et renvoie l'étiquette de graduation formatée. Dans ce cas, nous allons formater l'étiquette de graduation en dollars en millions.

```python
def millions(x, pos):
    """Les deux arguments sont la valeur et la position de la graduation."""
    return f'${x*1e-6:1.1f}M'
```
