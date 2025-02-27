# Utilisation d'une bibliothèque

Pour lier une boîte à cette nouvelle bibliothèque, vous pouvez utiliser le drapeau `--extern` de `rustc`. Tous ses éléments seront ensuite importés dans un module ayant le même nom que la bibliothèque. Ce module se comporte généralement de la même manière que tout autre module.

```rust
// extern crate rary; // Peut être nécessaire pour la version 2015 d'édition de Rust ou antérieure

fn main() {
    rary::public_function();

    // Erreur! `private_function` est privé
    //rary::private_function();

    rary::indirect_access();
}
```

```txt
# Où library.rlib est le chemin vers la bibliothèque compilée, supposé qu'elle soit
# dans le même répertoire ici :
$ rustc executable.rs --extern rary=library.rlib &&./executable
appelé `public_function()` de rary
appelé `indirect_access()` de rary, qui
> appelé `private_function()` de rary
```
