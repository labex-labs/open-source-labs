# Testcase: liste chaînée

Un moyen courant d'implémenter une liste chaînée est via des `enums` :

```rust
use crate::List::*;

enum List {
    // Cons : Struct tuple qui encapsule un élément et un pointeur vers le nœud suivant
    Cons(u32, Box<List>),
    // Nil : Un nœud qui signifie la fin de la liste chaînée
    Nil,
}

// Les méthodes peuvent être attachées à un enum
impl List {
    // Crée une liste vide
    fn new() -> List {
        // `Nil` a le type `List`
        Nil
    }

    // Consomme une liste et renvoie la même liste avec un nouvel élément au début
    fn prepend(self, elem: u32) -> List {
        // `Cons` a également le type List
        Cons(elem, Box::new(self))
    }

    // Renvoie la longueur de la liste
    fn len(&self) -> u32 {
        // `self` doit être comparé, car le comportement de cette méthode
        // dépend de la variante de `self`
        // `self` a le type `&List`, et `*self` a le type `List`, comparer sur un
        // type concret `T` est préférable à une comparaison sur une référence `&T`
        // Après Rust 2018, vous pouvez également utiliser `self` ici et `tail` (sans `ref`) ci-dessous,
        // Rust inferera les `&` et `ref tail`.
        // Voir https://doc.rust-lang.org/edition-guide/rust-2018/ownership-and-lifetimes/default-match-bindings.html
        match *self {
            // Ne peut pas prendre la propriété de la queue, car `self` est emprunté ;
            // au lieu de cela, prenez une référence à la queue
            Cons(_, ref tail) => 1 + tail.len(),
            // Cas de base : Une liste vide a une longueur de zéro
            Nil => 0
        }
    }

    // Renvoie la représentation de la liste sous forme d'une chaîne (allouée sur le tas)
    fn stringify(&self) -> String {
        match *self {
            Cons(head, ref tail) => {
                // `format!` est similaire à `print!`, mais renvoie une chaîne
                // allouée sur le tas au lieu d'afficher dans la console
                format!("{}, {}", head, tail.stringify())
            },
            Nil => {
                format!("Nil")
            },
        }
    }
}

fn main() {
    // Crée une liste chaînée vide
    let mut list = List::new();

    // Ajoute quelques éléments au début
    list = list.prepend(1);
    list = list.prepend(2);
    list = list.prepend(3);

    // Affiche l'état final de la liste
    println!("la liste chaînée a une longueur : {}", list.len());
    println!("{}", list.stringify());
}
```
