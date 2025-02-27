# Dépendre d'un package externe dans un espace de travail

Remarquez que l'espace de travail n'a qu'un seul fichier _Cargo.lock_ au niveau supérieur, plutôt que d'avoir un _Cargo.lock_ dans le répertoire de chaque crâne. Cela garantit que tous les crânes utilisent la même version de toutes les dépendances. Si nous ajoutons le package `rand` aux fichiers _adder/Cargo.toml_ et _add_one/Cargo.toml_, Cargo résoudra les deux vers une version de `rand` et enregistrera cela dans le seul _Cargo.lock_. Faire en sorte que tous les crânes dans l'espace de travail utilisent les mêmes dépendances signifie que les crânes seront toujours compatibles les uns avec les autres. Ajoutons le crâne `rand` à la section `[dependencies]` dans le fichier _add_one/Cargo.toml_ afin que nous puissions utiliser le crâne `rand` dans le crâne `add_one` :

Nom du fichier : `add_one/Cargo.toml`

```tomlrust
[dependencies]
rand = "0.8.5"
```

Nous pouvons maintenant ajouter `use rand;` au fichier `add_one/src/lib.rs`, et construire l'espace de travail complet en exécutant `cargo build` dans le répertoire `add` fera entrer et compiler le crâne `rand`. Nous obtiendrons un avertissement car nous ne faisons pas référence au `rand` que nous avons mis dans la portée :

```bash
$ cargo build
    Updating crates.io index
  Downloaded rand v0.8.5
   --snip--
   Compiling rand v0.8.5
   Compiling add_one v0.1.0 (file:///projects/add/add_one)
   Compiling adder v0.1.0 (file:///projects/add/adder)
    Finished dev [unoptimized + debuginfo] target(s) in 10.18s
```

Le _Cargo.lock_ de niveau supérieur contient maintenant des informations sur la dépendance de `add_one` sur `rand`. Cependant, même si `rand` est utilisé quelque part dans l'espace de travail, nous ne pouvons pas l'utiliser dans d'autres crânes de l'espace de travail à moins d'ajouter `rand` à leurs fichiers `Cargo.toml` également. Par exemple, si nous ajoutons `use rand;` au fichier `adder/src/main.rs` pour le package `adder`, nous obtiendrons une erreur :

```bash
$ cargo build
   --snip--
   Compiling adder v0.1.0 (file:///projects/add/adder)
error[E0432]: unresolved import `rand`
 --> adder/src/main.rs:2:5
  |
2 | use rand;
  |     ^^^^ no external crate `rand`
```

Pour corriger cela, éditez le fichier `Cargo.toml` pour le package `adder` et indiquez que `rand` est également une dépendance pour lui. Construire le package `adder` ajoutera `rand` à la liste des dépendances pour `adder` dans _Cargo.lock_, mais aucune copie supplémentaire de `rand` ne sera téléchargée. Cargo a veillé à ce que chaque crâne dans chaque package de l'espace de travail utilisant le package `rand` utilise la même version, nous économisant de l'espace et garantissant que les crânes dans l'espace de travail seront compatibles les uns avec les autres.
