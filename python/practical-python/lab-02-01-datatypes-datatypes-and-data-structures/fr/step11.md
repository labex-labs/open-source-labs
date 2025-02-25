# Exercice 2.1 : Les tuples

Au prompt interactif, créez le tuple suivant qui représente la ligne ci-dessus, mais avec les colonnes numériques converties en nombres appropriés :

```python
>>> t = (row[0], int(row[1]), float(row[2]))
>>> t
('AA', 100, 32.2)
>>>
```

En utilisant cela, vous pouvez maintenant calculer le coût total en multipliant les actions et le prix :

```python
>>> cost = t[1] * t[2]
>>> cost
3220.0000000000005
>>>
```

Le calcul mathématique est-il cassé en Python? Qu'est-ce que le problème avec la réponse 3220.0000000000005?

C'est un artefact de la carte mémoire à virgule flottante de votre ordinateur qui n'est capable de représenter avec précision que les décimales en base-2, pas en base-10. Pour des calculs même simples impliquant des décimales en base-10, de petites erreurs sont introduites. C'est normal, bien que cela puisse paraître un peu surprenant si vous ne l'avez pas vu auparavant.

Cela se produit dans tous les langages de programmation qui utilisent les décimales à virgule flottante, mais cela est souvent caché lors de l'affichage. Par exemple :

```python
>>> print(f'{cost:0.2f}')
3220.00
>>>
```

Les tuples sont en lecture seule. Vérifiez-le en essayant de changer le nombre d'actions en 75.

```python
>>> t[1] = 75
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>>
```

Bien que vous ne puissiez pas modifier le contenu d'un tuple, vous pouvez toujours créer un nouveau tuple entièrement qui remplace l'ancien.

```python
>>> t = (t[0], 75, t[2])
>>> t
('AA', 75, 32.2)
>>>
```

Chaque fois que vous réaffectez un nom de variable existant de cette manière, l'ancienne valeur est supprimée. Bien que l'affectation ci-dessus semble que vous modifiez le tuple, vous créez en réalité un nouveau tuple et vous jetez l'ancien.

Les tuples sont souvent utilisés pour empaqueter et extraire des valeurs dans des variables. Essayez ceci :

```python
>>> name, shares, price = t
>>> name
'AA'
>>> shares
75
>>> price
32.2
>>>
```

Prenez les variables ci-dessus et les repaquetez dans un tuple

```python
>>> t = (name, 2*shares, price)
>>> t
('AA', 150, 32.2)
>>>
```
