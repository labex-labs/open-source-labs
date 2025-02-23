# Fonction pour calculer la somme des puissances dans une plage donnée

Pour calculer la somme des puissances de tous les nombres dans une plage spécifiée (y compris les deux extrémités), utilisez la fonction suivante :

```js
const sumPower = (end, power = 2, start = 1) =>
  Array(end + 1 - start)
    .fill(0)
    .map((x, i) => (i + start) ** power)
    .reduce((a, b) => a + b, 0);
```

Voici comment utiliser cette fonction :

- Appelez `sumPower(end)` pour calculer la somme des carrés de tous les nombres de 1 à `end`.
- Appelez `sumPower(end, power)` pour calculer la somme des `power`ièmes puissances de tous les nombres de 1 à `end`.
- Appelez `sumPower(end, power, start)` pour calculer la somme des `power`ièmes puissances de tous les nombres de `start` à `end`.

Notez que les deuxième et troisième arguments (`power` et `start`) sont facultatifs et prennent respectivement les valeurs par défaut de `2` et `1` si ils ne sont pas fournis.

Exemple :

```js
sumPower(10); // Retourne 385 (somme des carrés des nombres de 1 à 10)
sumPower(10, 3); // Retourne 3025 (somme des cubes des nombres de 1 à 10)
sumPower(10, 3, 5); // Retourne 2925 (somme des cubes des nombres de 5 à 10)
```
