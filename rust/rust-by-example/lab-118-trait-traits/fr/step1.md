# Traits

Un `trait` est une collection de méthodes définies pour un type inconnu : `Self`. Elles peuvent accéder à d'autres méthodes déclarées dans le même trait.

Les traits peuvent être implémentés pour n'importe quel type de données. Dans l'exemple ci-dessous, nous définissons `Animal`, un groupe de méthodes. Le trait `Animal` est ensuite implémenté pour le type de données `Sheep`, permettant d'utiliser les méthodes de `Animal` avec un `Sheep`.

```rust
struct Sheep { naked: bool, name: &'static str }

trait Animal {
    // Signature de fonction associée ; `Self` fait référence au type d'implémentation.
    fn new(name: &'static str) -> Self;

    // Signatures de méthodes ; ces méthodes retourneront une chaîne de caractères.
    fn name(&self) -> &'static str;
    fn noise(&self) -> &'static str;

    // Les traits peuvent fournir des définitions de méthodes par défaut.
    fn talk(&self) {
        println!("{} says {}", self.name(), self.noise());
    }
}

impl Sheep {
    fn is_naked(&self) -> bool {
        self.naked
    }

    fn shear(&mut self) {
        if self.is_naked() {
            // Les méthodes de l'implémentation peuvent utiliser les méthodes de trait de l'implémentation.
            println!("{} is already naked...", self.name());
        } else {
            println!("{} gets a haircut!", self.name);

            self.naked = true;
        }
    }
}

// Implémentez le trait `Animal` pour `Sheep`.
impl Animal for Sheep {
    // `Self` est le type d'implémentation : `Sheep`.
    fn new(name: &'static str) -> Sheep {
        Sheep { name: name, naked: false }
    }

    fn name(&self) -> &'static str {
        self.name
    }

    fn noise(&self) -> &'static str {
        if self.is_naked() {
            "baaaaah?"
        } else {
            "baaaaah!"
        }
    }

    // Les méthodes de trait par défaut peuvent être remplacées.
    fn talk(&self) {
        // Par exemple, nous pouvons ajouter une réflexion silencieuse.
        println!("{} pauses briefly... {}", self.name, self.noise());
    }
}

fn main() {
    // L'annotation de type est nécessaire dans ce cas.
    let mut dolly: Sheep = Animal::new("Dolly");
    // TODO ^ Essayez d'enlever les annotations de type.

    dolly.talk();
    dolly.shear();
    dolly.talk();
}
```
