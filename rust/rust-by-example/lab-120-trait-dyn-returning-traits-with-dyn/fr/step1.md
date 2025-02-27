# Retourner des traits avec `dyn`

Le compilateur Rust doit savoir combien d'espace le type de retour de chaque fonction nécessite. Cela signifie que toutes vos fonctions doivent retourner un type concret. Contrairement à d'autres langages, si vous avez un trait comme `Animal`, vous ne pouvez pas écrire une fonction qui retourne `Animal`, car ses différentes implémentations nécessiteront des quantités de mémoire différentes.

Cependant, il existe un contournement simple. Au lieu de retourner directement un objet de trait, nos fonctions retournent un `Box` qui _contient_ un certain `Animal`. Un `box` n'est qu'une référence à une certaine mémoire dans le tas. Étant donné qu'une référence a une taille connue statiquement et que le compilateur peut garantir qu'elle pointe vers un `Animal` alloué sur le tas, nous pouvons retourner un trait à partir de notre fonction!

Rust essaie d'être le plus explicite possible chaque fois qu'il alloue de la mémoire sur le tas. Donc, si votre fonction retourne un pointeur-trait-sur-tas de cette manière, vous devez écrire le type de retour avec le mot clé `dyn`, par exemple `Box<dyn Animal>`.

```rust
struct Sheep {}
struct Cow {}

trait Animal {
    // Signature de la méthode d'instance
    fn noise(&self) -> &'static str;
}

// Implémentez le trait `Animal` pour `Sheep`.
impl Animal for Sheep {
    fn noise(&self) -> &'static str {
        "baaaaah!"
    }
}

// Implémentez le trait `Animal` pour `Cow`.
impl Animal for Cow {
    fn noise(&self) -> &'static str {
        "moooooo!"
    }
}

// Retourne une certaine structure qui implémente Animal, mais nous ne savons pas laquelle au moment de la compilation.
fn random_animal(random_number: f64) -> Box<dyn Animal> {
    if random_number < 0.5 {
        Box::new(Sheep {})
    } else {
        Box::new(Cow {})
    }
}

fn main() {
    let random_number = 0.234;
    let animal = random_animal(random_number);
    println!("You've randomly chosen an animal, and it says {}", animal.noise());
}
```
