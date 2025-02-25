# Indexation avec l'itérateur plat

L'attribut `x.flat` renvoie un itérateur qui peut être utilisé pour itérer sur tout le tableau dans un style C-contigu. Cet itérateur peut également être indexé en utilisant une tranche de base ou une indexation avancée.

```python
x = np.arange(10)
iterator = x.flat
print(iterator[1:5])  # Sortie : [1, 2, 3, 4]
```
