# Définissez la règle de récurrence

Vous allez définir des repères de dates personnalisés pour chaque cinquième Pâques. Pour ce faire, vous devez définir la règle de récurrence à l'aide de la fonction `rrulewrapper`.

```python
rule = rrulewrapper(YEARLY, byeaster=1, interval=5)
```
