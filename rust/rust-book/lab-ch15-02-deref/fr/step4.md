# Defining Our Own Smart Pointer

Construisons un pointeur intelligent similaire au type `Box<T>` fourni par la bibliothèque standard pour découvrir comment les pointeurs intelligents se comportent différemment des références par défaut. Ensuite, nous examinerons comment ajouter la capacité d'utiliser l'opérateur de déréférence.

Le type `Box<T>` est finalement défini comme une struct tuple avec un élément, donc la Liste 15-8 définit un type `MyBox<T>` de la même manière. Nous définirons également une fonction `new` pour correspondre à la fonction `new` définie sur `Box<T>`.

Nom du fichier : `src/main.rs`

```rust
 1 struct MyBox<T>(T);

impl<T> MyBox<T> {
  2 fn new(x: T) -> MyBox<T> {
      3 MyBox(x)
    }
}
```

Liste 15-8 : Définition d'un type `MyBox<T>`

Nous définissons une struct nommée `MyBox` et déclarons un paramètre générique `T` \[1\] car nous voulons que notre type puisse stocker des valeurs de tout type. Le type `MyBox` est une struct tuple avec un élément de type `T`. La fonction `MyBox::new` prend un paramètre de type `T` \[2\] et renvoie une instance de `MyBox` qui contient la valeur passée en paramètre \[3\].

Essayons d'ajouter la fonction `main` de la Liste 15-7 à la Liste 15-8 et de la modifier pour utiliser le type `MyBox<T>` que nous avons défini au lieu de `Box<T>`. Le code de la Liste 15-9 ne compilera pas car Rust ne sait pas comment déréférencer `MyBox`.

Nom du fichier : `src/main.rs`

```rust
fn main() {
    let x = 5;
    let y = MyBox::new(x);

    assert_eq!(5, x);
    assert_eq!(5, *y);
}
```

Liste 15-9 : Tentative d'utilisation de `MyBox<T>` de la même manière que les références et `Box<T>`

Voici l'erreur de compilation résultante :

```bash
error[E0614]: type `MyBox<{integer}>` cannot be dereferenced
  --> src/main.rs:14:19
   |
14 |     assert_eq!(5, *y);
   |                   ^^
```

Notre type `MyBox<T>` ne peut pas être déréférencé car nous n'avons pas implémenté cette capacité sur notre type. Pour autoriser le déréférencement avec l'opérateur `*`, nous implémentons le trait `Deref`.
