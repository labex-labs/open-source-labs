# Retourner plusieurs valeurs à partir de fonctions

En Python, lorsque vous avez besoin qu'une fonction retourne plus d'une valeur, il existe une solution pratique : retourner un tuple. Un tuple est un type de structure de données en Python. C'est une séquence immuable, ce qui signifie qu'une fois que vous avez créé un tuple, vous ne pouvez pas modifier ses éléments. Les tuples sont utiles car ils peuvent contenir plusieurs valeurs de différents types en un seul endroit.

Créons une fonction pour analyser les lignes de configuration au format `nom=valeur`. Le but de cette fonction est de prendre une ligne dans ce format et de retourner à la fois le nom et la valeur comme éléments distincts.

1. Tout d'abord, vous devez créer un nouveau fichier Python. Ce fichier contiendra le code de notre fonction et le code de test. Dans le répertoire du projet, créez un fichier nommé `return_values.py`. Vous pouvez utiliser la commande suivante dans le terminal pour créer ce fichier :

```
touch ~/project/return_values.py
```

2. Maintenant, ouvrez le fichier `return_values.py` dans votre éditeur de code. À l'intérieur de ce fichier, nous allons écrire la fonction `parse_line`. Cette fonction prend une ligne en entrée, la divise au niveau du premier signe '=' et retourne le nom et la valeur sous forme de tuple.

```python
def parse_line(line):
    """
    Parse a line in the format 'name=value' and return both the name and value.

    Args:
        line (str): Input line to parse in the format 'name=value'

    Returns:
        tuple: A tuple containing (name, value)
    """
    parts = line.split('=', 1)  # Split at the first equals sign
    if len(parts) == 2:
        name = parts[0]
        value = parts[1]
        return (name, value)  # Return as a tuple
```

Dans cette fonction, la méthode `split` est utilisée pour diviser la ligne d'entrée en deux parties au niveau du premier signe '='. Si la ligne est au bon format `nom=valeur`, nous extrayons le nom et la valeur et les retournons sous forme de tuple.

3. Après avoir défini la fonction, nous devons ajouter un peu de code de test pour voir si la fonction fonctionne comme prévu. Le code de test appellera la fonction `parse_line` avec une entrée d'exemple et affichera les résultats.

```python
# Test the parse_line function
if __name__ == "__main__":
    result = parse_line('email=guido@python.org')
    print(f"Result as tuple: {result}")

    # Unpacking the tuple into separate variables
    name, value = parse_line('email=guido@python.org')
    print(f"Unpacked name: {name}")
    print(f"Unpacked value: {value}")
```

Dans le code de test, nous appelons d'abord la fonction `parse_line` et stockons le tuple retourné dans la variable `result`. Ensuite, nous affichons ce tuple. Ensuite, nous utilisons le déballage de tuple pour assigner directement les éléments du tuple aux variables `name` et `value` et les affichons séparément.

4. Une fois que vous avez écrit la fonction et le code de test, enregistrez le fichier `return_values.py`. Ensuite, ouvrez le terminal et exécutez la commande suivante pour exécuter le script Python :

```
python ~/project/return_values.py
```

Vous devriez voir une sortie similaire à :

```
Result as tuple: ('email', 'guido@python.org')
Unpacked name: email
Unpacked value: guido@python.org
```

**Explication :**

- La fonction `parse_line` divise la chaîne d'entrée au niveau du caractère '=' en utilisant la méthode `split`. Cette méthode divise la chaîne en parties en fonction du séparateur spécifié.
- Elle retourne les deux parties sous forme de tuple en utilisant la syntaxe `return (name, value)`. Un tuple est un moyen de regrouper plusieurs valeurs ensemble.
- Lorsque vous appelez la fonction, vous avez deux options. Vous pouvez soit stocker l'ensemble du tuple dans une seule variable, comme nous l'avons fait avec la variable `result`. Ou vous pouvez "déballer" le tuple directement dans des variables distinctes en utilisant la syntaxe `name, value = parse_line(...)`. Cela facilite la manipulation des valeurs individuelles.

Ce modèle de retour de plusieurs valeurs sous forme de tuple est très courant en Python. Il rend les fonctions plus polyvalentes car elles peuvent fournir plus d'une information au code qui les appelle.
