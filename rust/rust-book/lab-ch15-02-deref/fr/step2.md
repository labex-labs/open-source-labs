# Following the Pointer to the Value

Une référence normale est un type de pointeur, et une manière de concevoir un pointeur est comme une flèche vers une valeur stockée ailleurs. Dans la Liste 15-6, nous créons une référence à une valeur `i32` puis utilisons l'opérateur de déréférence pour suivre la référence jusqu'à la valeur.

Nom du fichier : `src/main.rs`

```rust
fn main() {
  1 let x = 5;
  2 let y = &x;

  3 assert_eq!(5, x);
  4 assert_eq!(5, *y);
}
```

Liste 15-6 : Utilisation de l'opérateur de déréférence pour suivre une référence vers une valeur `i32`

La variable `x` contient une valeur `i32` égale à `5` \[1\]. Nous définissons `y` égal à une référence à `x` \[2\]. Nous pouvons affirmer que `x` est égal à `5` \[3\]. Cependant, si nous voulons faire une assertion sur la valeur de `y`, nous devons utiliser `*y` pour suivre la référence jusqu'à la valeur à laquelle elle pointe (d'où le terme _déréférencement_) afin que le compilateur puisse comparer la valeur réelle \[4\]. Une fois que nous avons déréférencé `y`, nous avons accès à la valeur entière à laquelle `y` pointe que nous pouvons comparer avec `5`.

Si nous avions essayé d'écrire `assert_eq!(5, y);` à la place, nous aurions obtenu cette erreur de compilation :

```bash
error[E0277]: can't compare `{integer}` with `&{integer}`
 --> src/main.rs:6:5
  |
6 |     assert_eq!(5, y);
  |     ^^^^^^^^^^^^^^^^ no implementation for `{integer} ==
&{integer}`
  |
  = help: the trait `PartialEq<&{integer}>` is not implemented
for `{integer}`
```

Comparer un nombre et une référence à un nombre n'est pas autorisé car ce sont des types différents. Nous devons utiliser l'opérateur de déréférence pour suivre la référence jusqu'à la valeur à laquelle elle pointe.
