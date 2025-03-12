# Exécution de tests sélectionnés et utilisation de la découverte de tests

Le module `unittest` en Python est un outil puissant qui vous permet de tester efficacement votre code. Il propose plusieurs méthodes pour exécuter des tests spécifiques ou découvrir et exécuter automatiquement tous les tests de votre projet. Cela est très utile car il vous aide à vous concentrer sur des parties spécifiques de votre code lors des tests ou à vérifier rapidement l'ensemble des tests du projet.

## Exécution de tests spécifiques

Parfois, vous pouvez souhaiter exécuter seulement des méthodes de test ou des classes de test spécifiques au lieu de l'ensemble des tests. Vous pouvez y parvenir en utilisant l'option de modèle (pattern) avec le module `unittest`. Cela vous donne plus de contrôle sur les tests qui sont exécutés, ce qui peut être pratique lorsque vous déboguez une partie particulière de votre code.

1. Pour exécuter seulement les tests liés à la création d'un objet Stock :

```bash
python3 -m unittest teststock.TestStock.test_create
```

Dans cette commande, `python3 -m unittest` indique à Python d'exécuter le module `unittest`. `teststock` est le nom du fichier de test, `TestStock` est le nom de la classe de test, et `test_create` est la méthode de test spécifique que nous voulons exécuter. En exécutant cette commande, vous pouvez rapidement vérifier si le code lié à la création d'un objet `Stock` fonctionne comme prévu.

2. Pour exécuter tous les tests de la classe `TestStock` :

```bash
python3 -m unittest teststock.TestStock
```

Ici, nous omettons le nom de la méthode de test spécifique. Ainsi, cette commande exécutera toutes les méthodes de test de la classe `TestStock` dans le fichier `teststock`. Cela est utile lorsque vous voulez vérifier la fonctionnalité globale des cas de test de l'objet `Stock`.

## Utilisation de la découverte de tests

Le module `unittest` peut découvrir et exécuter automatiquement tous les fichiers de test de votre projet. Cela vous évite le détail de spécifier manuellement chaque fichier de test à exécuter, en particulier dans les projets plus grands avec de nombreux fichiers de test.

1. Renommez le fichier actuel pour qu'il suive le modèle de nommage de la découverte de tests :

```bash
mv teststock.py test_stock.py
```

Le mécanisme de découverte de tests dans `unittest` recherche les fichiers qui suivent le modèle de nommage `test_*.py`. En renommant le fichier en `test_stock.py`, nous facilitons la tâche du module `unittest` pour trouver et exécuter les tests de ce fichier.

2. Exécutez la découverte de tests :

```bash
python3 -m unittest discover
```

Cette commande indique au module `unittest` de découvrir et d'exécuter automatiquement tous les fichiers de test qui correspondent au modèle `test_*.py` dans le répertoire actuel. Il parcourra le répertoire et exécutera tous les cas de test trouvés dans les fichiers correspondants.

3. Vous pouvez également spécifier un répertoire dans lequel rechercher les tests :

```bash
python3 -m unittest discover -s . -p "test_*.py"
```

Où :

- `-s .` spécifie le répertoire de départ pour la découverte (le répertoire actuel dans ce cas). Le point (`.`) représente le répertoire actuel. Vous pouvez le changer pour un autre chemin de répertoire si vous voulez rechercher des tests dans un autre emplacement.
- `-p "test_*.py"` est le modèle pour correspondre aux fichiers de test. Cela garantit que seuls les fichiers dont le nom commence par `test_` et ayant l'extension `.py` sont considérés comme des fichiers de test.

Vous devriez voir tous les 12 tests s'exécuter et réussir, comme précédemment.

4. Renommez le fichier en son nom d'origine pour assurer la cohérence avec le laboratoire :

```bash
mv test_stock.py teststock.py
```

Après avoir exécuté la découverte de tests, nous renommons le fichier en son nom d'origine pour maintenir la cohérence de l'environnement de laboratoire.

En utilisant la découverte de tests, vous pouvez facilement exécuter tous les tests d'un projet sans avoir à spécifier chaque fichier de test individuellement. Cela rend le processus de test plus efficace et moins sujet aux erreurs.
