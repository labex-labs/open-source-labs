# `Rc`

Lorsque la propriété multiple est nécessaire, on peut utiliser `Rc` (Compte de Références). `Rc` garde une trace du nombre de références, ce qui signifie le nombre de propriétaires de la valeur encapsulée dans un `Rc`.

Le compte de références d'un `Rc` augmente de 1 chaque fois qu'un `Rc` est cloné, et diminue de 1 chaque fois qu'un `Rc` cloné sort de portée. Lorsque le compte de références d'un `Rc` atteint zéro (ce qui signifie qu'il n'y a plus de propriétaires), à la fois le `Rc` et la valeur sont supprimés.

Le clonage d'un `Rc` ne réalise jamais une copie profonde. Le clonage crée simplement un autre pointeur vers la valeur encapsulée, et incrémente le compte.

```rust
use std::rc::Rc;

fn main() {
    let rc_examples = "Rc examples".to_string();
    {
        println!("--- rc_a est créé ---");

        let rc_a: Rc<String> = Rc::new(rc_examples);
        println!("Compte de Références de rc_a: {}", Rc::strong_count(&rc_a));

        {
            println!("--- rc_a est cloné en rc_b ---");

            let rc_b: Rc<String> = Rc::clone(&rc_a);
            println!("Compte de Références de rc_b: {}", Rc::strong_count(&rc_b));
            println!("Compte de Références de rc_a: {}", Rc::strong_count(&rc_a));

            // Deux `Rc` sont égaux si leurs valeurs internes sont égales
            println!("rc_a et rc_b sont égaux: {}", rc_a.eq(&rc_b));

            // On peut utiliser directement les méthodes d'une valeur
            println!("Longueur de la valeur dans rc_a: {}", rc_a.len());
            println!("Valeur de rc_b: {}", rc_b);

            println!("--- rc_b sort de portée ---");
        }

        println!("Compte de Références de rc_a: {}", Rc::strong_count(&rc_a));

        println!("--- rc_a sort de portée ---");
    }

    // Erreur! `rc_examples` a déjà été déplacé dans `rc_a`
    // Et lorsque `rc_a` est supprimé, `rc_examples` est supprimé avec
    // println!("rc_examples: {}", rc_examples);
    // TODO ^ Essayez de décommenter cette ligne
}
```
