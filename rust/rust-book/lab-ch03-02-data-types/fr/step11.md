# Accès aux éléments d'un tableau

Un tableau est un bloc unique de mémoire d'une taille connue et fixe qui peut être alloué sur la pile. Vous pouvez accéder aux éléments d'un tableau en utilisant l'indexation, comme ceci :

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let a = [1, 2, 3, 4, 5];

    let first = a[0];
    let second = a[1];
}
```

Dans cet exemple, la variable nommée `first` obtiendra la valeur `1` car c'est la valeur à l'index `[0]` dans le tableau. La variable nommée `second` obtiendra la valeur `2` à partir de l'index `[1]` dans le tableau.
