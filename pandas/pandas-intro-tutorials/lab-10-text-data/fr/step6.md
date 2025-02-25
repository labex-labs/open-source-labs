# Remplacez des valeurs dans une colonne

Enfin, remplaçons les valeurs dans la colonne `Sex` :'male' par 'M' et 'female' par 'F'. Nous utiliserons la méthode `replace()` pour cela.

```python
# Remplacez'male' par 'M' et 'female' par 'F' dans la colonne 'Sex'
titanic["Sex_short"] = titanic["Sex"].replace({"male": "M", "female": "F"})
```
