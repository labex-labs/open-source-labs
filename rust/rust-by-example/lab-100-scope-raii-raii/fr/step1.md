# RAII

Les variables en Rust font plus que simplement stocker des données sur la pile : elles _possèdent_ également des ressources, par exemple `Box<T>` possède de la mémoire dans le tas. Rust impose l'RAII (Resource Acquisition Is Initialization), donc chaque fois qu'un objet sort de portée, son destructeur est appelé et ses ressources possédées sont libérées.

Ce comportement protège contre les bugs de _fuite de ressources_, donc vous n'aurez jamais plus à libérer manuellement la mémoire ou à vous inquiéter des fuites de mémoire! Voici un aperçu rapide :

```rust
// raii.rs
fn create_box() {
    // Alloue un entier dans le tas
    let _box1 = Box::new(3i32);

    // `_box1` est détruit ici, et la mémoire est libérée
}

fn main() {
    // Alloue un entier dans le tas
    let _box2 = Box::new(5i32);

    // Un scope imbriqué :
    {
        // Alloue un entier dans le tas
        let _box3 = Box::new(4i32);

        // `_box3` est détruit ici, et la mémoire est libérée
    }

    // Création de nombreux boîtes juste pour le plaisir
    // Il n'est pas nécessaire de libérer manuellement la mémoire!
    for _ in 0u32..1_000 {
        create_box();
    }

    // `_box2` est détruit ici, et la mémoire est libérée
}
```

Bien sûr, nous pouvons double vérifier les erreurs de mémoire en utilisant `valgrind` :

```{=html}
<!-- REUSE-IgnoreStart -->
```

```{=html}
<!-- Empêche REUSE d'analyser la déclaration de copyright dans le code d'échantillonnage -->
```

```shell
$ rustc raii.rs && valgrind./raii
==26873== Memcheck, un détecteur d'erreurs de mémoire
==26873== Copyright (C) 2002-2013, et GNU GPL'd, par Julian Seward et al.
==26873== Utilisation de Valgrind-3.9.0 et LibVEX ; relancez avec -h pour les informations sur le copyright
==26873== Commande :./raii
==26873==
==26873==
==26873== SOMMAIRE DU TAS :
==26873==     en cours d'utilisation à la fin : 0 octets dans 0 blocs
==26873==   utilisation totale du tas : 1 013 allouations, 1 013 libérations, 8 696 octets alloués
==26873==
==26873== Tous les blocs de tas ont été libérés -- aucune fuite n'est possible
==26873==
==26873== Pour les comptes des erreurs détectées et supprimées, relancez avec : -v
==26873== SOMMAIRE DES ERREURS : 0 erreurs provenant de 0 contextes (supprimées : 2 provenant de 2)
```

```{=html}
<!-- REUSE-IgnoreEnd -->
```

Pas de fuites ici!

## Destructeur

La notion de destructeur en Rust est fournie par le trait \[`Drop`\]. Le destructeur est appelé lorsque la ressource sort de portée. Ce trait n'est pas requis pour être implémenté pour chaque type, implémentez-le seulement pour votre type si vous en avez besoin pour sa propre logique de destructeur.

Exécutez l'exemple ci-dessous pour voir comment le trait \[`Drop`\] fonctionne. Lorsque la variable dans la fonction `main` sort de portée, le destructeur personnalisé sera invoqué.

```rust
struct ToDrop;

impl Drop for ToDrop {
    fn drop(&mut self) {
        println!("ToDrop est en train d'être supprimé");
    }
}

fn main() {
    let x = ToDrop;
    println!("A créé un ToDrop!");
}
```
