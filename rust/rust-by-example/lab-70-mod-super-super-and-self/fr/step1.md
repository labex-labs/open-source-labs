# `super` et `self`

Les mots clés `super` et `self` peuvent être utilisés dans le chemin pour éliminer l'ambiguité lors de l'accès à des éléments et pour éviter le codage en dur inutile des chemins.

```rust
fn function() {
    println!("appelé `function()`");
}

mod cool {
    pub fn function() {
        println!("appelé `cool::function()`");
    }
}

mod my {
    fn function() {
        println!("appelé `my::function()`");
    }

    mod cool {
        pub fn function() {
            println!("appelé `my::cool::function()`");
        }
    }

    pub fn indirect_call() {
        // Essayons d'accéder à toutes les fonctions nommées `function` à partir de ce scope!
        print!("appelé `my::indirect_call()`, qui\n> ");

        // Le mot clé `self` fait référence au scope du module actuel - dans ce cas `my`.
        // Appeler `self::function()` et appeler `function()` directement donnent
        // le même résultat, car ils font référence à la même fonction.
        self::function();
        function();

        // Nous pouvons également utiliser `self` pour accéder à un autre module à l'intérieur de `my`:
        self::cool::function();

        // Le mot clé `super` fait référence au scope parent (en dehors du module `my`).
        super::function();

        // Cela se lira à la `cool::function` dans le scope de la *crate*.
        // Dans ce cas, le scope de la crate est le scope le plus externe.
        {
            use crate::cool::function as root_function;
            root_function();
        }
    }
}

fn main() {
    my::indirect_call();
}
```
