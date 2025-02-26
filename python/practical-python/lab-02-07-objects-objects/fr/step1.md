# Affectation

Plusieurs opérations en Python sont liées à l'_affectation_ ou au _stockage_ de valeurs.

```python
a = valeur         # Affectation à une variable
s[n] = valeur      # Affectation à une liste
s.append(valeur)   # Ajout à une liste
d['clé'] = valeur  # Ajout à un dictionnaire
```

_Attention : les opérations d'affectation **ne font jamais de copie** de la valeur affectée._ Toutes les affectations ne sont que des copies de référence (ou des copies de pointeur si vous préférez).
