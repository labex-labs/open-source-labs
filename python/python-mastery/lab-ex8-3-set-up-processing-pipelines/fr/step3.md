# Amélioration du pipeline de coroutines

Maintenant que nous avons un pipeline de base opérationnel, il est temps de le rendre plus flexible. En programmation, la flexibilité est cruciale car elle permet à notre code de s'adapter à différentes exigences. Nous allons y parvenir en modifiant notre programme `coticker.py` pour prendre en charge diverses options de filtrage et de formatage.

1. Tout d'abord, ouvrez le fichier `coticker.py` dans votre éditeur de code. C'est dans l'éditeur de code que vous allez apporter toutes les modifications nécessaires au programme. Il offre un environnement pratique pour visualiser, éditer et enregistrer votre code.

2. Ensuite, nous allons ajouter une nouvelle coroutine qui filtre les données par nom d'action. Une coroutine est un type spécial de fonction qui peut suspendre et reprendre son exécution. Cela nous permet de créer un pipeline où les données peuvent traverser différentes étapes de traitement. Voici le code de la nouvelle coroutine :

```python
@consumer
def filter_by_name(name, target):
    while True:
        record = yield
        if record.name == name:
            target.send(record)
```

Dans ce code, la coroutine `filter_by_name` prend un nom d'action et une coroutine cible en paramètres. Elle attend continuellement un enregistrement en utilisant le mot - clé `yield`. Lorsqu'un enregistrement arrive, elle vérifie si le nom de l'enregistrement correspond au nom spécifié. Si c'est le cas, elle envoie l'enregistrement à la coroutine cible.

3. Maintenant, ajoutons une autre coroutine qui filtre en fonction de seuils de prix. Cette coroutine nous aidera à sélectionner les actions dans une plage de prix spécifique. Voici le code :

```python
@consumer
def price_threshold(min_price, max_price, target):
    while True:
        record = yield
        if min_price <= record.price <= max_price:
            target.send(record)
```

De même que la coroutine précédente, la coroutine `price_threshold` attend un enregistrement. Elle vérifie ensuite si le prix de l'enregistrement se trouve dans la plage de prix minimale et maximale spécifiée. Si c'est le cas, elle envoie l'enregistrement à la coroutine cible.

4. Après avoir ajouté les nouvelles coroutines, nous devons mettre à jour le programme principal pour démontrer ces filtres supplémentaires. Le programme principal est le point d'entrée de notre application, où nous configurons les pipelines de traitement et démarrons le flux de données. Voici le code mis à jour :

```python
if __name__ == '__main__':
    import sys

    # Define the field names to display
    fields = ['name', 'price', 'change', 'high', 'low']

    # Create the processing pipeline with multiple outputs

    # Pipeline 1: Show all negative changes (same as before)
    print("Stocks with negative changes:")
    t1 = ticker('text', fields)
    neg_filter = negchange(t1)
    tick_creator1 = create_ticker(neg_filter)
    csv_parser1 = to_csv(tick_creator1)

    # Start following the file with the first pipeline
    import threading
    threading.Thread(target=follow, args=('stocklog.csv', csv_parser1), daemon=True).start()

    # Wait a moment to see some results
    import time
    time.sleep(5)

    # Pipeline 2: Filter by name (AAPL)
    print("\nApple stock updates:")
    t2 = ticker('text', fields)
    name_filter = filter_by_name('AAPL', t2)
    tick_creator2 = create_ticker(name_filter)
    csv_parser2 = to_csv(tick_creator2)

    # Follow the file with the second pipeline
    threading.Thread(target=follow, args=('stocklog.csv', csv_parser2), daemon=True).start()

    # Wait a moment to see some results
    time.sleep(5)

    # Pipeline 3: Filter by price range
    print("\nStocks priced between 50 and 75:")
    t3 = ticker('text', fields)
    price_filter = price_threshold(50, 75, t3)
    tick_creator3 = create_ticker(price_filter)
    csv_parser3 = to_csv(tick_creator3)

    # Follow with the third pipeline
    follow('stocklog.csv', csv_parser3)
```

Dans ce code mis à jour, nous créons trois pipelines de traitement différents. Le premier pipeline affiche les actions avec des variations négatives, le deuxième filtre les actions par le nom 'AAPL', et le troisième filtre les actions en fonction d'une plage de prix entre 50 et 75. Nous utilisons des threads pour exécuter les deux premiers pipelines de manière concurrente, ce qui nous permet de traiter les données plus efficacement.

5. Une fois que vous avez apporté toutes les modifications, enregistrez le fichier. Enregistrer le fichier garantit que toutes vos modifications sont conservées. Ensuite, exécutez le programme mis à jour en utilisant les commandes suivantes dans votre terminal :

```bash
cd /home/labex/project
python3 coticker.py
```

La commande `cd` change le répertoire actuel pour le répertoire du projet, et la commande `python3 coticker.py` exécute le programme Python.

6. Après avoir exécuté le programme, vous devriez voir trois sorties différentes :
   - Tout d'abord, vous verrez les actions avec des variations négatives.
   - Ensuite, vous verrez toutes les mises à jour des actions AAPL.
   - Enfin, vous verrez toutes les actions dont le prix est compris entre 50 et 75.

## Comprendre le pipeline amélioré

Le programme amélioré démontre plusieurs concepts importants :

1. **Plusieurs pipelines** : Nous pouvons créer plusieurs pipelines de traitement à partir de la même source de données. Cela nous permet d'effectuer différents types d'analyses sur les mêmes données simultanément.
2. **Filtres spécialisés** : Nous pouvons créer différentes coroutines pour des tâches de filtrage spécifiques. Ces filtres nous aident à sélectionner uniquement les données qui répondent à nos critères spécifiques.
3. **Traitement concurrent** : En utilisant des threads, nous pouvons exécuter plusieurs pipelines de manière concurrente. Cela améliore l'efficacité de notre programme en lui permettant de traiter les données en parallèle.
4. **Composition de pipelines** : Les coroutines peuvent être combinées de différentes manières pour atteindre différents objectifs de traitement de données. Cela nous donne la flexibilité de personnaliser nos pipelines de traitement de données selon nos besoins.

Cette approche offre une façon flexible et modulaire de traiter les données en continu. Elle vous permet d'ajouter ou de modifier des étapes de traitement sans changer l'architecture globale du programme.
