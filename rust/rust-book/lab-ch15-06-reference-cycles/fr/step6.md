# Visualisation des modifications de strong_count et weak_count

Regardons comment les valeurs de `strong_count` et `weak_count` des instances `Rc<Node>` changent en créant un nouveau scope interne et en déplaçant la création de `branch` dans ce scope. En faisant ainsi, nous pouvons voir ce qui se passe lorsque `branch` est créée puis supprimée lorsqu'elle sort de portée. Les modifications sont montrées dans la liste 15-29.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let leaf = Rc::new(Node {
        value: 3,
        parent: RefCell::new(Weak::new()),
        children: RefCell::new(vec![]),
    });

  1 println!(
        "leaf strong = {}, weak = {}",
        Rc::strong_count(&leaf),
        Rc::weak_count(&leaf),
    );

  2 {
        let branch = Rc::new(Node {
            value: 5,
            parent: RefCell::new(Weak::new()),
            children: RefCell::new(vec![Rc::clone(&leaf)]),
        });

        *leaf.parent.borrow_mut() = Rc::downgrade(&branch);

      3 println!(
            "branch strong = {}, weak = {}",
            Rc::strong_count(&branch),
            Rc::weak_count(&branch),
        );

      4 println!(
            "leaf strong = {}, weak = {}",
            Rc::strong_count(&leaf),
            Rc::weak_count(&leaf),
        );
  5 }

  6 println!(
        "leaf parent = {:?}",
        leaf.parent.borrow().upgrade()
    );
  7 println!(
        "leaf strong = {}, weak = {}",
        Rc::strong_count(&leaf),
        Rc::weak_count(&leaf),
    );
}
```

Liste 15-29 : Création de `branch` dans un scope interne et examen des comptages de références fortes et faibles

Après la création de `leaf`, son `Rc<Node>` a un comptage fort de 1 et un comptage faible de 0 \[1\]. Dans le scope interne \[2\], nous créons `branch` et le associons à `leaf`, auquel moment lorsque nous affichons les comptages \[3\], l'`Rc<Node>` dans `branch` aura un comptage fort de 1 et un comptage faible de 1 (pour `leaf.parent` qui pointe vers `branch` avec un `Weak<Node>`). Lorsque nous affichons les comptages dans `leaf` \[4\], nous verrons qu'il aura un comptage fort de 2 car `branch` a maintenant une copie de l'`Rc<Node>` de `leaf` stockée dans `branch.children`, mais aura toujours un comptage faible de 0.

Lorsque le scope interne se termine \[5\], `branch` sort de portée et le comptage fort de l'`Rc<Node>` diminue à 0, donc son `Node` est supprimé. Le comptage faible de 1 de `leaf.parent` n'a pas d'incidence sur la suppression ou non de `Node`, donc nous n'avons pas de fuites mémoire!

Si nous essayons d'accéder au parent de `leaf` après la fin du scope, nous obtiendrons `None` à nouveau \[6\]. À la fin du programme \[7\], l'`Rc<Node>` dans `leaf` a un comptage fort de 1 et un comptage faible de 0 car la variable `leaf` est maintenant la seule référence à l'`Rc<Node>` à nouveau.

Toute la logique qui gère les comptages et la suppression des valeurs est intégrée dans `Rc<T>` et `Weak<T>` et leurs implémentations du trait `Drop`. En spécifiant que la relation d'un enfant à son parent devrait être une référence `Weak<T>` dans la définition de `Node`, vous êtes capable d'avoir des nœuds parents qui pointent vers des nœuds enfants et vice versa sans créer de cycle de référence et de fuites mémoire.
