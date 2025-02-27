# Utilisation de Rc`<T>`{=html} pour partager des données

Revoyons notre exemple de liste cons dans la Liste 15-5. Rappelez-vous que nous l'avons défini en utilisant `Box<T>`. Cette fois, nous allons créer deux listes qui partagent toutes deux la propriété d'une troisième liste. Conceptuellement, cela ressemble à la Figure 15-3.

Figure 15-3 : Deux listes, `b` et `c`, partageant la propriété d'une troisième liste, `a`

Nous allons créer la liste `a` qui contient `5` puis `10`. Ensuite, nous allons créer deux autres listes : `b` qui commence par `3` et `c` qui commence par `4`. Les listes `b` et `c` continueront ensuite jusqu'à la première liste `a` contenant `5` et `10`. En d'autres termes, les deux listes partageront la première liste contenant `5` et `10`.

Essayons d'implémenter ce scénario en utilisant notre définition de `List` avec `Box<T>`. Cela ne fonctionnera pas, comme le montre la Liste 15-17.

Nom de fichier : `src/main.rs`

```rust
enum List {
    Cons(i32, Box<List>),
    Nil,
}

use crate::List::{Cons, Nil};

fn main() {
    let a = Cons(5, Box::new(Cons(10, Box::new(Nil))));
  1 let b = Cons(3, Box::new(a));
  2 let c = Cons(4, Box::new(a));
}
```

Liste 15-17 : Demonstration du fait que nous ne sommes pas autorisés à avoir deux listes utilisant `Box<T>` qui tentent de partager la propriété d'une troisième liste

Lorsque nous compilons ce code, nous obtenons cette erreur :

```bash
error[E0382]: use of moved value: `a`
  --> src/main.rs:11:30
   |
9  |     let a = Cons(5, Box::new(Cons(10, Box::new(Nil))));
   |         - move occurs because `a` has type `List`, which
does not implement the `Copy` trait
10 |     let b = Cons(3, Box::new(a));
   |                              - value moved here
11 |     let c = Cons(4, Box::new(a));
   |                              ^ value used here after move
```

Les variantes `Cons` possèdent les données qu'elles contiennent, donc lorsque nous créons la liste `b` \[1\], `a` est déplacé dans `b` et `b` possède `a`. Ensuite, lorsque nous essayons d'utiliser `a` à nouveau lors de la création de `c` \[2\], nous ne sommes pas autorisés car `a` a été déplacé.

Nous pourrions modifier la définition de `Cons` pour qu'elle contienne des références à la place, mais alors nous devrions spécifier des paramètres de durée de vie. En spécifiant des paramètres de durée de vie, nous spécifierions que chaque élément de la liste vivra au moins aussi longtemps que la liste entière. C'est le cas pour les éléments et les listes de la Liste 15-17, mais pas dans tous les scénarios.

Au lieu de cela, nous allons modifier notre définition de `List` pour utiliser `Rc<T>` à la place de `Box<T>`, comme le montre la Liste 15-18. Chaque variante `Cons` contiendra désormais une valeur et un `Rc<T>` pointant vers une `List`. Lorsque nous créons `b`, au lieu de prendre la propriété de `a`, nous allons cloner le `Rc<List>` que `a` contient, augmentant ainsi le nombre de références d'un à deux et laissant `a` et `b` partager la propriété des données dans ce `Rc<List>`. Nous allons également cloner `a` lors de la création de `c`, augmentant le nombre de références de deux à trois. Chaque fois que nous appelons `Rc::clone`, le compte de références des données à l'intérieur du `Rc<List>` augmentera, et les données ne seront nettoyées que s'il n'y a plus de références à elles.

Nom de fichier : `src/main.rs`

```rust
enum List {
    Cons(i32, Rc<List>),
    Nil,
}

use crate::List::{Cons, Nil};
1 use std::rc::Rc;

fn main() {
  2 let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
  3 let b = Cons(3, Rc::clone(&a));
  4 let c = Cons(4, Rc::clone(&a));
}
```

Liste 15-18 : Une définition de `List` qui utilise `Rc<T>`

Nous devons ajouter une instruction `use` pour amener `Rc<T>` dans la portée \[1\] car il n'est pas dans le préambule. Dans `main`, nous créons la liste contenant `5` et `10` et la stockons dans un nouveau `Rc<List>` dans `a` \[2\]. Ensuite, lorsque nous créons `b` \[3\] et `c` \[4\], nous appelons la fonction `Rc::clone` et passons une référence au `Rc<List>` dans `a` en tant qu'argument.

Nous aurions pu appeler `a.clone()` plutôt que `Rc::clone(&a)`, mais la convention de Rust est d'utiliser `Rc::clone` dans ce cas. L'implémentation de `Rc::clone` ne fait pas une copie profonde de toutes les données comme le font la plupart des implémentations de `clone` des types. L'appel à `Rc::clone` n'incremente que le compte de références, ce qui ne prend pas beaucoup de temps. Les copies profondes de données peuvent prendre beaucoup de temps. En utilisant `Rc::clone` pour le comptage de références, nous pouvons distinguer visuellement entre les types de clones de copie profonde et les types de clones qui augmentent le compte de références. Lorsque nous cherchons des problèmes de performance dans le code, nous n'avons besoin de considérer que les clones de copie profonde et pouvons ignorer les appels à `Rc::clone`.
