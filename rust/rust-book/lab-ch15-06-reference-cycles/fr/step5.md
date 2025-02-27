# Ajout d'une référence d'un enfant à son parent

Pour que le nœud enfant soit conscient de son parent, nous devons ajouter un champ `parent` à notre définition de la structure `Node`. Le problème est de décider quel devrait être le type de `parent`. Nous savons qu'il ne peut pas contenir un `Rc<T>` car cela créerait un cycle de référence avec `leaf.parent` qui pointerait vers `branch` et `branch.children` qui pointerait vers `leaf`, ce qui ferait en sorte que leurs valeurs `strong_count` ne soient jamais égales à 0.

En considérant les relations d'une autre manière, un nœud parent devrait posséder ses enfants : si un nœud parent est supprimé, ses nœuds enfants devraient également être supprimés. Cependant, un enfant ne devrait pas posséder son parent : si nous supprimons un nœud enfant, le parent devrait toujours exister. C'est un cas pour les références faibles!

Donc, au lieu de `Rc<T>`, nous ferons en sorte que le type de `parent` utilise `Weak<T>`, plus précisément un `RefCell<Weak<Node>>`. Maintenant, notre définition de la structure `Node` ressemble à ceci :

Nom de fichier : `src/main.rs`

```rust
use std::cell::RefCell;
use std::rc::{Rc, Weak};

#[derive(Debug)]
struct Node {
    value: i32,
    parent: RefCell<Weak<Node>>,
    children: RefCell<Vec<Rc<Node>>>,
}
```

Un nœud sera capable de se référer à son nœud parent mais ne possède pas son parent. Dans la liste 15-28, nous mettons à jour `main` pour utiliser cette nouvelle définition de sorte que le nœud `leaf` ait un moyen de se référer à son parent, `branch`.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let leaf = Rc::new(Node {
        value: 3,
      1 parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![]),
    });

  2 println!(
        "leaf parent = {:?}",
        leaf.parent.borrow().upgrade()
    );

    let branch = Rc::new(Node {
        value: 5,
      3 parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![Rc::clone(&leaf)]),
    });

  4 *leaf.parent.borrow_mut() = Rc::downgrade(&branch);

  5 println!(
        "leaf parent = {:?}",
        leaf.parent.borrow().upgrade()
    );
}
```

Liste 15-28 : Un nœud `leaf` avec une référence faible à son nœud parent, `branch`

La création du nœud `leaf` ressemble à la liste 15-27 avec la différence du champ `parent` : `leaf` commence sans parent, donc nous créons une nouvelle instance de référence `Weak<Node>` vide \[1\].

À ce stade, lorsque nous essayons d'obtenir une référence au parent de `leaf` en utilisant la méthode `upgrade`, nous obtenons une valeur `None`. Nous le voyons dans la sortie de la première instruction `println!` \[2\] :

```rust
leaf parent = None
```

Lorsque nous créons le nœud `branch`, il aura également une nouvelle référence `Weak<Node>` dans le champ `parent` \[3\] car `branch` n'a pas de nœud parent. Nous avons toujours `leaf` comme l'un des enfants de `branch`. Une fois que nous avons l'instance `Node` dans `branch`, nous pouvons modifier `leaf` pour lui donner une référence `Weak<Node>` à son parent \[4\]. Nous utilisons la méthode `borrow_mut` sur le `RefCell<Weak<Node>>` dans le champ `parent` de `leaf`, puis nous utilisons la fonction `Rc::downgrade` pour créer une référence `Weak<Node>` à `branch` à partir de l'`Rc<Node>` dans `branch`.

Lorsque nous affichons à nouveau le parent de `leaf` \[5\], cette fois-ci nous obtiendrons un variant `Some` contenant `branch` : maintenant `leaf` peut accéder à son parent! Lorsque nous affichons `leaf`, nous évitons également le cycle qui aboutissait finalement à un débordement de pile comme dans la liste 15-26 ; les références `Weak<Node>` sont affichées comme `(Weak)` :

    leaf parent = Some(Node { value: 5, parent: RefCell { value: (Weak) },
    children: RefCell { value: [Node { value: 3, parent: RefCell { value: (Weak) },
    children: RefCell { value: [] } }] } })

Le manque de sortie infinie indique que ce code n'a pas créé de cycle de référence. Nous pouvons également le constater en examinant les valeurs que nous obtenons en appelant `Rc::strong_count` et `Rc::weak_count`.
