# Création d'un espace de travail

Un _espace de travail_ est un ensemble de packages qui partagent le même fichier _Cargo.lock_ et le même répertoire de sortie. Créons un projet utilisant un espace de travail - nous utiliserons du code trivial pour nous concentrer sur la structure de l'espace de travail. Il existe plusieurs façons de structurer un espace de travail, nous montrerons juste une façon commune. Nous aurons un espace de travail contenant un binaire et deux bibliothèques. Le binaire, qui fournira la fonctionnalité principale, dépendra des deux bibliothèques. Une bibliothèque fournira une fonction `add_one` et l'autre bibliothèque une fonction `add_two`. Ces trois crânes feront partie du même espace de travail. Commençons par créer un nouveau répertoire pour l'espace de travail :

```bash
mkdir add
cd add
```

Ensuite, dans le répertoire `add`, nous créons le fichier `Cargo.toml` qui configurera tout l'espace de travail. Ce fichier n'aura pas de section `[package]`. Au lieu de cela, il commencera par une section `[workspace]` qui nous permettra d'ajouter des membres à l'espace de travail en spécifiant le chemin vers le package avec notre crâne binaire ; dans ce cas, ce chemin est _adder_ :

Nom du fichier : `Cargo.toml`

```toml
[workspace]

members = [
    "adder",
]
```

Ensuite, nous créerons le crâne binaire `adder` en exécutant `cargo new` dans le répertoire `add` :

```bash
$ cargo new adder
     Created binary (application) `adder` package
```

À ce stade, nous pouvons construire l'espace de travail en exécutant `cargo build`. Les fichiers dans votre répertoire `add` devraient ressembler à ceci :

    ├── Cargo.lock
    ├── Cargo.toml
    ├── adder
    │   ├── Cargo.toml
    │   └── src
    │       └── main.rs
    └── target

L'espace de travail a un répertoire `target` au niveau supérieur dans lequel les artefacts compilés seront placés ; le package `adder` n'a pas son propre répertoire `target`. Même si nous exécutons `cargo build` à l'intérieur du répertoire `adder`, les artefacts compilés finiront toujours dans _add/target_ plutôt que dans `add/adder/target`. Cargo structure le répertoire `target` dans un espace de travail de cette manière car les crânes dans un espace de travail sont supposés dépendre les uns des autres. Si chaque crâne avait son propre répertoire `target`, chaque crâne devrait recompiler chacun des autres crânes dans l'espace de travail pour placer les artefacts dans son propre répertoire `target`. En partageant un seul répertoire `target`, les crânes peuvent éviter de recompiler inutilement.
