# Indentation

L'indentation est utilisée pour désigner des groupes d'instructions qui appartiennent ensemble. Considérez l'exemple précédent :

```python
while num_bills * bill_thickness < sears_height:
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2

print('Number of days', day)
```

L'indentation regroupe les instructions suivantes comme les opérations qui se répètent :

```python
    print(day, num_bills, num_bills * bill_thickness)
    day = day + 1
    num_bills = num_bills * 2
```

Comme l'instruction `print()` à la fin n'est pas indentée, elle n'appartient pas à la boucle. La ligne vide n'est là que pour la lisibilité. Elle n'affecte pas l'exécution.
