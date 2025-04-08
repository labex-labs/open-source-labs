# Filtrer pour exécuter plusieurs tests

Nous pouvons spécifier une partie du nom d'un test, et tout test dont le nom correspond à cette valeur sera exécuté. Par exemple, puisque deux de nos noms de test contiennent `add`, nous pouvons exécuter ces deux tests en exécutant `cargo test add` :

```bash

```

Cette commande a exécuté tous les tests dont le nom contient `add` et a filtré le test nommé `one_hundred`. Notez également que le module dans lequel un test apparaît devient une partie du nom du test, de sorte que nous pouvons exécuter tous les tests d'un module en filtrant sur le nom du module.
