# Plus d'informations sur la liste cons

Une _liste cons_ est une structure de données issue du langage de programmation Lisp et de ses dialectes, composée de paires imbriquées, et est la version Lisp d'une liste chaînée. Son nom vient de la fonction `cons` (abrégé de _construct function_) en Lisp qui construit une nouvelle paire à partir de ses deux arguments. En appelant `cons` sur une paire composée d'une valeur et d'une autre paire, nous pouvons construire des listes cons constituées de paires récursives.

Par exemple, voici une représentation en pseudo-code d'une liste cons contenant la liste `1, 2, 3` avec chaque paire entre parenthèses :

```rust
(1, (2, (3, Nil)))
```

Chaque élément d'une liste cons contient deux éléments : la valeur de l'élément actuel et l'élément suivant. Le dernier élément de la liste ne contient que une valeur appelée `Nil` sans élément suivant. Une liste cons est produite en appelant récursivement la fonction `cons`. Le nom canonique pour désigner le cas de base de la récursion est `Nil`. Notez que ce n'est pas la même chose que le concept de "null" ou "nil" du Chapitre 6, qui est une valeur invalide ou absente.

La liste cons n'est pas une structure de données couramment utilisée en Rust. La plupart du temps, lorsque vous avez une liste d'éléments en Rust, `Vec<T>` est un meilleur choix à utiliser. D'autres types de données récursives plus complexes _sont_ utiles dans diverses situations, mais en commençant par la liste cons dans ce chapitre, nous pouvons explorer la manière dont les boîtes nous permettent de définir un type de données récursif sans trop de distractions.

Le Listing 15-2 contient une définition d'énumération pour une liste cons. Notez que ce code ne compilera pas encore car le type `List` n'a pas une taille connue, ce que nous allons démontrer.

Nom de fichier : `src/main.rs`

```rust
enum List {
    Cons(i32, List),
    Nil,
}
```

Listing 15-2 : La première tentative de définition d'un énumération pour représenter une structure de données de liste cons de valeurs `i32`

> Note : Nous implémentons une liste cons qui ne contient que des valeurs `i32` dans le cadre de cet exemple. Nous aurions pu l'implémenter à l'aide de génériques, comme nous l'avons discuté au Chapitre 10, pour définir un type de liste cons qui pourrait stocker des valeurs de tout type.

Utiliser le type `List` pour stocker la liste `1, 2, 3` ressemblerait au code du Listing 15-3.

Nom de fichier : `src/main.rs`

```rust
--snip--

use crate::List::{Cons, Nil};

fn main() {
    let list = Cons(1, Cons(2, Cons(3, Nil)));
}
```

Listing 15-3 : Utilisation de l'énumération `List` pour stocker la liste `1, 2, 3`

La première valeur `Cons` contient `1` et une autre valeur de type `List`. Cette valeur de type `List` est une autre valeur `Cons` qui contient `2` et une autre valeur de type `List`. Cette valeur de type `List` est une nouvelle valeur `Cons` qui contient `3` et une valeur de type `List`, qui est finalement `Nil`, la variante non récursive qui indique la fin de la liste.

Si nous essayons de compiler le code du Listing 15-3, nous obtenons l'erreur affichée dans le Listing 15-4.

```bash
error[E0072]: recursive type `List` has infinite size
 --> src/main.rs:1:1
  |
1 | enum List {
  | ^^^^^^^^^ recursive type has infinite size
2 |     Cons(i32, List),
  |               ---- recursive without indirection
  |
help: insert some indirection (e.g., a `Box`, `Rc`, or `&`) to make `List`
representable
  |
2 |     Cons(i32, Box<List>),
  |               ++++    +
```

Listing 15-4 : L'erreur que nous obtenons lorsqu'on essaie de définir un énumération récursive

L'erreur indique que ce type "a une taille infinie". La raison en est que nous avons défini `List` avec une variante qui est récursive : elle contient directement une autre valeur de soi-même. En conséquence, Rust ne peut pas déterminer combien d'espace il faut pour stocker une valeur de type `List`. Analysons pourquoi nous obtenons cette erreur. Tout d'abord, regardons comment Rust décide de la quantité d'espace qu'il faut pour stocker une valeur d'un type non récursif.
