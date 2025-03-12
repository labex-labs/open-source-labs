# Création d'un générateur pour les données en flux

En programmation, les générateurs sont un outil puissant, surtout lorsqu'il s'agit de résoudre des problèmes réels tels que la surveillance d'une source de données en flux. Dans cette section, nous allons apprendre à appliquer ce que nous avons appris sur les générateurs à un tel scénario pratique. Nous allons créer un générateur qui surveille un fichier journal et nous fournit les nouvelles lignes au fur et à mesure qu'elles sont ajoutées au fichier.

## Configuration de la source de données

Avant de commencer à créer le générateur, nous devons configurer une source de données. Dans ce cas, nous allons utiliser un programme de simulation qui génère des données sur le marché boursier.

Tout d'abord, vous devez ouvrir un nouveau terminal dans le WebIDE. C'est là que vous exécuterez les commandes pour démarrer la simulation.

Après avoir ouvert le terminal, vous exécuterez le programme de simulation boursière. Voici les commandes que vous devez entrer :

```bash
cd ~/project
python3 stocksim.py
```

La première commande `cd ~/project` change le répertoire actuel pour le répertoire `project` dans votre répertoire personnel. La deuxième commande `python3 stocksim.py` exécute le programme de simulation boursière. Ce programme générera des données sur le marché boursier et les écrira dans un fichier nommé `stocklog.csv` dans le répertoire actuel. Laissez ce programme s'exécuter en arrière - plan tandis que nous travaillons sur le code de surveillance.

## Création d'un simple moniteur de fichier

Maintenant que nous avons configuré notre source de données, créons un programme qui surveille le fichier `stocklog.csv`. Ce programme affichera tout changement de prix négatif.

1. Tout d'abord, créez un nouveau fichier appelé `follow.py` dans le WebIDE. Pour ce faire, vous devez changer le répertoire pour le répertoire `project` en utilisant la commande suivante dans le terminal :

```bash
cd ~/project
```

2. Ensuite, ajoutez le code suivant au fichier `follow.py`. Ce code ouvre le fichier `stocklog.csv`, déplace le pointeur de fichier à la fin du fichier, puis vérifie en continu s'il y a de nouvelles lignes. Si une nouvelle ligne est trouvée et qu'elle représente un changement de prix négatif, il affiche le nom de l'action, le prix et le changement.

```python
# follow.py
import os
import time

f = open('stocklog.csv')
f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file

while True:
    line = f.readline()
    if line == '':
        time.sleep(0.1)   # Sleep briefly and retry
        continue
    fields = line.split(',')
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print('%10s %10.2f %10.2f' % (name, price, change))
```

3. Après avoir ajouté le code, enregistrez le fichier. Ensuite, exécutez le programme en utilisant la commande suivante dans le terminal :

```bash
python3 follow.py
```

Vous devriez voir une sortie qui montre les actions avec des changements de prix négatifs. Cela pourrait ressembler à ceci :

```
      AAPL     148.24      -1.76
      GOOG    2498.45      -1.55
```

Si vous souhaitez arrêter le programme, appuyez sur `Ctrl+C` dans le terminal.

## Conversion en fonction générateur

Bien que le code précédent fonctionne, nous pouvons le rendre plus réutilisable et modulaire en le convertissant en une fonction générateur. Une fonction générateur est un type spécial de fonction qui peut être mise en pause et reprise, et qui produit des valeurs une par une.

1. Ouvrez à nouveau le fichier `follow.py` et modifiez - le pour utiliser une fonction générateur. Voici le code mis à jour :

```python
# follow.py
import os
import time

def follow(filename):
    """
    Generator function that yields new lines in a file as they are added.
    Similar to the 'tail -f' Unix command.
    """
    f = open(filename)
    f.seek(0, os.SEEK_END)   # Move to the end of the file

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)   # Sleep briefly and retry
            continue
        yield line

# Example usage - monitor stocks with negative price changes
if __name__ == '__main__':
    for line in follow('stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print('%10s %10.2f %10.2f' % (name, price, change))
```

La fonction `follow` est maintenant une fonction générateur. Elle ouvre le fichier, se déplace à la fin, puis vérifie en continu s'il y a de nouvelles lignes. Lorsqu'une nouvelle ligne est trouvée, elle la produit.

2. Enregistrez le fichier et exécutez - le à nouveau en utilisant la commande :

```bash
python3 follow.py
```

La sortie devrait être la même que précédemment. Mais maintenant, la logique de surveillance de fichier est soigneusement encapsulée dans la fonction générateur `follow`. Cela signifie que nous pouvons réutiliser cette fonction dans d'autres programmes qui ont besoin de surveiller un fichier.

## Comprendre la puissance des générateurs

En convertissant notre code de lecture de fichier en une fonction générateur, nous l'avons rendu beaucoup plus flexible et réutilisable. La fonction `follow()` peut être utilisée dans n'importe quel programme qui a besoin de surveiller un fichier, pas seulement pour les données boursières.

Par exemple, vous pourriez l'utiliser pour surveiller les journaux de serveur, les journaux d'application ou tout autre fichier qui est mis à jour au fil du temps. Cela montre comment les générateurs sont un excellent moyen de gérer les sources de données en flux de manière propre et modulaire.
