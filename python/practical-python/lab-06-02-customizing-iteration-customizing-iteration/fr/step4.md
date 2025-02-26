# Exercice 6.5 : Surveiller une source de données en continu

Les générateurs peuvent être un moyen intéressant de surveiller des sources de données en temps réel telles que des fichiers de journalisation ou des flux de marché boursier. Dans cette partie, nous allons explorer cette idée. Pour commencer, suivez attentivement les instructions suivantes.

Le programme `stocksim.py` est un programme qui simule des données de marché boursier. En sortie, le programme écrit constamment des données en temps réel dans un fichier `stocklog.csv`. Dans une fenêtre de commande séparée, accédez au répertoire `` et exécutez ce programme :

```bash
$ python3 stocksim.py
```

Si vous êtes sous Windows, localisez simplement le programme `stocksim.py` et double-cliquez sur lui pour l'exécuter. Maintenant, oubliez ce programme (laissez-le simplement s'exécuter). En utilisant une autre fenêtre, regardez le fichier `stocklog.csv` qui est écrit par le simulateur. Vous devriez voir de nouvelles lignes de texte ajoutées au fichier toutes les quelques secondes. Encore une fois, laissez simplement ce programme s'exécuter en arrière-plan - il s'exécutera pendant plusieurs heures (vous n'aurez pas besoin de vous en soucier).

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
        print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```

Si vous exécutez le programme, vous verrez un cotation boursière en temps réel. Sous le capot, ce code est un peu comme la commande Unix `tail -f` qui est utilisée pour surveiller un fichier de journalisation.

Remarque : L'utilisation de la méthode `readline()` dans cet exemple est un peu inhabituelle car ce n'est pas la manière habituelle de lire les lignes d'un fichier (normalement, vous utiliseriez simplement une boucle `for`). Cependant, dans ce cas, nous l'utilisons pour interroger régulièrement la fin du fichier pour voir si de nouvelles données ont été ajoutées (`readline()` renverra soit de nouvelles données soit une chaîne vide).
