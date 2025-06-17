# Using Box`<T>` Like a Reference

Nous pouvons réécrire le code de la Liste 15-6 pour utiliser un `Box<T>` au lieu d'une référence ; l'opérateur de déréférence utilisé sur le `Box<T>` dans la Liste 15-7 fonctionne de la même manière que l'opérateur de déréférence utilisé sur la référence dans la Liste 15-6.

Nom du fichier : `src/main.rs`

```rust
fn main() {
    let x = 5;
  1 let y = Box::new(x);

    assert_eq!(5, x);
  2 assert_eq!(5, *y);
}
```

Liste 15-7 : Utilisation de l'opérateur de déréférence sur un `Box<i32>`

La principale différence entre la Liste 15-7 et la Liste 15-6 est que ici, nous définissons `y` comme une instance d'un box pointant vers une valeur copiée de `x` plutôt qu'une référence pointant vers la valeur de `x` \[1\]. Dans la dernière assertion \[2\], nous pouvons utiliser l'opérateur de déréférence pour suivre le pointeur du box de la même manière que lorsque `y` était une référence. Ensuite, nous explorerons ce qui est spécial à propos de `Box<T>` qui nous permet d'utiliser l'opérateur de déréférence en définissant notre propre type de box.
