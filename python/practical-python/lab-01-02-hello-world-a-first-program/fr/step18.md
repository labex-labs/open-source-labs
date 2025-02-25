# Exercice 1.5 : La balle rebondissante

Une balle de caoutchouc est laissée tomber d'une hauteur de 100 mètres et chaque fois qu'elle touche le sol, elle rebondit jusqu'à 3/5 de la hauteur à laquelle elle est tombée. Écrivez un programme `bounce.py` qui imprime un tableau montrant la hauteur des 10 premiers rebonds.

Voici une solution :

```python
# bounce.py

height = 100
bounce = 1
while bounce <= 10:
    height = height * (3 / 5)
    print(bounce, round(height, 4))
    bounce += 1
```

Votre programme devrait produire un tableau ressemblant à ceci :

```code
1 60.0
2 36.0
3 21.599999999999998
4 12.959999999999999
5 7.775999999999999
6 4.6655999999999995
7 2.7993599999999996
8 1.6796159999999998
9 1.0077695999999998
10 0.6046617599999998
```

_Nota : Vous pouvez un peu nettoyer la sortie si vous utilisez la fonction round(). Essayez d'utiliser pour arrondir la sortie à 4 chiffres._

```code
1 60.0
2 36.0
3 21.6
4 12.96
5 7.776
6 4.6656
7 2.7994
8 1.6796
9 1.0078
10 0.6047
```
