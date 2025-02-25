# Meilleures pratiques en matière d'indentation

- Utilisez des espaces au lieu de tabulations.
- Utilisez 4 espaces par niveau.
- Utilisez un éditeur compatible Python.

La seule exigence de Python est que l'indentation au sein d'un même bloc soit cohérente. Par exemple, voici une erreur :

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
        day = day + 1 # ERREUR
    num_bills = num_bills * 2
```
