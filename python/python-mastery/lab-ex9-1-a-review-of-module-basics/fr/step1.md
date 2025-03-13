# Création d'un module simple

Commençons notre exploration des modules Python en créant un module simple. En Python, un module est essentiellement un fichier avec une extension `.py` qui contient du code Python. Imaginez - le comme un conteneur dans lequel vous pouvez regrouper des fonctions, des classes et des variables liées. Cela rend votre code plus organisé et plus facile à gérer, surtout à mesure que vos projets augmentent en taille.

1. Tout d'abord, ouvrez le WebIDE. Une fois qu'il est ouvert, vous devrez créer un nouveau fichier. Pour ce faire, cliquez sur "File" dans la barre de menu, puis sélectionnez "New File". Nommez ce nouveau fichier `simplemod.py` et enregistrez - le dans le répertoire `/home/labex/project`. C'est dans ce répertoire que nous allons conserver tous les fichiers liés à cette expérience.

2. Maintenant, ajoutons du code à notre fichier `simplemod.py` nouvellement créé. Le code ci - dessous définit quelques éléments de base que vous trouverez souvent dans un module Python.

```python
# simplemod.py

x = 42        # Une variable globale

# Une fonction simple
def foo():
    print('x is', x)

# Une classe simple
class Spam:
    def yow(self):
        print('Yow!')

# Une instruction de script
print('Loaded simplemod')
```

Dans ce code :

- `x = 42` crée une variable globale nommée `x` et lui assigne la valeur `42`. Les variables globales peuvent être accédées depuis n'importe où dans le module.
- La fonction `foo()` est définie pour afficher la valeur de la variable globale `x`. Les fonctions sont des blocs de code réutilisables qui effectuent une tâche spécifique.
- La classe `Spam` est un modèle pour créer des objets. Elle a une méthode appelée `yow()`, qui affiche simplement la chaîne de caractères 'Yow!'. Les méthodes sont des fonctions appartenant à une classe.
- L'instruction `print('Loaded simplemod')` est une instruction de script. Elle s'exécutera dès que le module sera chargé, ce qui nous aide à confirmer que le module a été chargé avec succès.

3. Après avoir ajouté le code, enregistrez le fichier. Vous pouvez le faire en appuyant sur `Ctrl+S` sur votre clavier ou en sélectionnant "File" > "Save" dans le menu. Enregistrer le fichier garantit que toutes les modifications que vous avez apportées sont conservées.

Regardons de plus près ce que contient ce module :

- Une variable globale `x` avec la valeur `42`. Cette variable peut être utilisée dans tout le module et même accédée depuis d'autres modules si elle est correctement importée.
- Une fonction `foo()` qui affiche la valeur de `x`. Les fonctions sont utiles pour effectuer des tâches répétitives sans avoir à écrire le même code plusieurs fois.
- Une classe `Spam` avec une méthode `yow()`. Les classes et les méthodes sont des concepts fondamentaux en programmation orientée objet, qui vous permettent de créer des structures de données et des comportements complexes.
- Une instruction `print` qui s'exécute lorsque le module est chargé. Cette instruction sert d'indicateur visuel que le module a été chargé avec succès dans l'environnement Python.

L'instruction `print` en bas nous aidera à observer quand le module est chargé, ce qui est important pour le débogage et la compréhension du fonctionnement des modules en Python.
