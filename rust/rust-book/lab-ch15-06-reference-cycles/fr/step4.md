# Création d'une structure de données d'arbre : Un nœud avec des nœuds enfants

Pour commencer, nous allons construire un arbre avec des nœuds qui connaissent leurs nœuds enfants. Nous allons créer une structure nommée `Node` qui contient sa propre valeur `i32` ainsi que des références à ses valeurs `Node` enfants :

Nom de fichier : `src/main.rs`

```rust
use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug)]
struct Node {
    value: i32,
    children: RefCell<Vec<Rc<Node>>>,
}
```

Nous voulons qu'un `Node` possède ses enfants, et nous voulons partager cette propriété avec des variables pour pouvoir accéder directement à chaque `Node` de l'arbre. Pour ce faire, nous définissons les éléments de `Vec<T>` comme étant des valeurs du type `Rc<Node>`. Nous voulons également modifier les nœuds qui sont les enfants d'un autre nœud, donc nous avons un `RefCell<T>` dans `children` autour de `Vec<Rc<Node>>`.

Ensuite, nous utiliserons notre définition de structure et créerons une instance `Node` nommée `leaf` avec la valeur `3` et aucun enfant, et une autre instance nommée `branch` avec la valeur `5` et `leaf` comme l'un de ses enfants, comme montré dans la liste 15-27.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let leaf = Rc::new(Node {
        value: 3,
        children: RefCell::new(vec![]),
    });

    let branch = Rc::new(Node {
        value: 5,
        children: RefCell::new(vec![Rc::clone(&leaf)]),
    });
}
```

Liste 15-27 : Création d'un nœud `leaf` sans enfant et d'un nœud `branch` avec `leaf` comme l'un de ses enfants

Nous clonons l'`Rc<Node>` dans `leaf` et le stockons dans `branch`, ce qui signifie que le `Node` dans `leaf` a maintenant deux propriétaires : `leaf` et `branch`. Nous pouvons passer de `branch` à `leaf` via `branch.children`, mais il n'y a aucun moyen de passer de `leaf` à `branch`. La raison est que `leaf` n'a pas de référence à `branch` et ne sait pas qu'ils sont liés. Nous voulons que `leaf` sache que `branch` est son parent. Nous allons le faire ensuite.
