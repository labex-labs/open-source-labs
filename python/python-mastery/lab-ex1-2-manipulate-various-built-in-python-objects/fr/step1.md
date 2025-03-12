# Travailler avec les nombres en Python

Python offre un support robuste pour les opérations numériques. En programmation, les nombres sont des types de données fondamentaux utilisés pour les calculs et la représentation de quantités. Cette étape vous présentera la manipulation de base des nombres en Python, ce qui est essentiel pour effectuer diverses opérations mathématiques dans vos programmes.

## Opérations arithmétiques de base

Pour commencer à travailler avec les nombres en Python, vous devez d'abord ouvrir un shell interactif Python. Vous pouvez le faire en tapant `python3` dans votre terminal. Le shell interactif Python vous permet d'écrire et d'exécuter du code Python ligne par ligne, ce qui est idéal pour tester et apprendre.

```bash
python3
```

Une fois que vous êtes dans le shell interactif Python, vous pouvez essayer quelques opérations arithmétiques de base. Python suit les règles mathématiques standard pour l'arithmétique, telles que l'ordre des opérations (PEMDAS : Parentheses, Exponents, Multiplication et Division, Addition et Soustraction).

```python
>>> 3 + 4*5    # La multiplication a une priorité supérieure à l'addition, donc 4*5 est calculé en premier, puis ajouté à 3
23
>>> 23.45 / 1e-02    # La notation scientifique pour 0.01 est utilisée ici. La division est effectuée pour obtenir le résultat
2345.0
```

## Division entière

Python 3 gère la division différemment de Python 2. Comprendre ces différences est crucial pour éviter des résultats inattendus dans votre code.

```python
>>> 7 / 4    # En Python 3, la division normale retourne un nombre à virgule flottante (float), même si le résultat pourrait être un entier
1.75
>>> 7 // 4   # La division entière (troncature de la partie décimale) vous donne le quotient sous forme d'entier
1
```

## Méthodes des nombres

Les nombres en Python ont plusieurs méthodes utiles qui sont souvent négligées. Ces méthodes peuvent simplifier les opérations numériques complexes et les conversions. Explorons-en quelques-unes :

```python
>>> x = 1172.5
>>> x.as_integer_ratio()    # Cette méthode représente le nombre à virgule flottante sous forme de fraction, ce qui peut être utile pour certains calculs mathématiques
(2345, 2)
>>> x.is_integer()    # Vérifie si le nombre à virgule flottante est une valeur entière. Dans ce cas, 1172.5 n'est pas un entier, donc elle retourne False
False

>>> y = 12345
>>> y.numerator    # Pour les entiers, le numérateur est le nombre lui-même
12345
>>> y.denominator    # Pour les entiers, le dénominateur est toujours 1
1
>>> y.bit_length()    # Cette méthode vous indique le nombre de bits nécessaires pour représenter le nombre en binaire, ce qui peut être utile dans les opérations au niveau des bits
14
```

Ces méthodes sont particulièrement utiles lorsque vous devez effectuer des opérations numériques spécifiques ou des conversions. Elles peuvent vous faire gagner du temps et rendre votre code plus efficace.

Lorsque vous avez terminé d'explorer le shell interactif Python, vous pouvez le quitter en tapant :

```python
>>> exit()
```
