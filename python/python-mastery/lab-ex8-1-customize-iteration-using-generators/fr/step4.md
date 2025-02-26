# Surveiller une source de données en continu

Les générateurs peuvent également être un moyen utile de simplement produire un flux de données. Dans cette partie, nous allons explorer cette idée en écrivant un générateur pour surveiller un fichier de journal. Pour commencer, suivez attentivement les instructions suivantes.

Le programme `stocksim.py` est un programme qui simule les données du marché boursier. En tant que sortie, le programme écrit constamment des données en temps réel dans un fichier `stocklog.csv`. Dans une fenêtre de commande (pas IDLE), accédez au répertoire `\` et exécutez ce programme :

    % python3 stocksim.py

Si vous êtes sous Windows, localisez simplement le programme `stocksim.py` et double-cliquez dessus pour l'exécuter. Maintenant, oubliez ce programme (laissez-le simplement s'exécuter). Encore une fois, laissez simplement ce programme s'exécuter en arrière-plan - il fonctionnera pendant plusieurs heures (vous n'aurez pas besoin de vous en soucier).

Une fois le programme ci-dessus en cours d'exécution, écrivons un petit programme pour ouvrir le fichier, aller à la fin et surveiller de nouveaux résultats. Créez un fichier `follow.py` et mettez ce code dedans :

```python
# follow.py
import os
import time
f = open('stocklog.csv')
f.seek(0, os.SEEK_END)   # Décale le pointeur du fichier de 0 octets depuis la fin du fichier

while True:
    line = f.readline()
    if line == '':
        time.sleep(0.1)   # Dodo brièvement et réessayez
        continue
    fields = line.split(',')
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print('%10s %10.2f %10.2f' % (name, price, change))
```

Si vous exécutez le programme, vous verrez un cotation boursière en temps réel. Sous les couvertures, ce code est un peu comme la commande Unix `tail -f` utilisée pour surveiller un fichier de journal.

**Remarque** : L'utilisation de la méthode `readline()` dans cet exemple est un peu inhabituelle car ce n'est pas la manière habituelle de lire les lignes d'un fichier (normalement, vous utiliseriez simplement une boucle `for`). Cependant, dans ce cas, nous l'utilisons pour interroger régulièrement la fin du fichier pour voir si de nouvelles données ont été ajoutées (`readline()` renverra soit de nouvelles données soit une chaîne vide).

Si vous examinez attentivement le code, la première partie du code produit des lignes de données tandis que les instructions à la fin de la boucle `while` consomment les données. Une caractéristique importante des fonctions génératrices est que vous pouvez déplacer tout le code de production de données dans une fonction réutilisable.

Modifiez le code de sorte que la lecture du fichier soit effectuée par une fonction génératrice `follow(filename)`. Assurez-vous que le code suivant fonctionne :

```python
>>> for line in follow('stocklog.csv'):
          print(line, end='')

... Devriez voir des lignes de sortie produites ici...
```

Modifiez le code de la cotation boursière de sorte qu'il ressemble à ceci :

```python
for line in follow('stocklog.csv'):
    fields = line.split(',')
    name = fields[0].strip('"')
    price = float(fields[1])
    change = float(fields[4])
    if change < 0:
        print('%10s %10.2f %10.2f' % (name, price, change))
```

**Discussion**

Quelque chose de très puissant vient de se produire ici. Vous avez déplacé un modèle d'itération intéressant (lire les lignes à la fin d'un fichier) dans sa propre petite fonction. La fonction `follow()` est maintenant cette utilité complètement générique que vous pouvez utiliser dans n'importe quel programme. Par exemple, vous pourriez l'utiliser pour surveiller les journaux de serveur, les journaux de débogage et d'autres sources de données similaires. C'est assez cool.
