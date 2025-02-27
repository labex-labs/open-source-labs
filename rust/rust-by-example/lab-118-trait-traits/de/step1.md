# Traits

Ein `Trait` ist eine Sammlung von Methoden, die für einen unbekannten Typ definiert sind: `Self`. Sie können auf andere Methoden zugreifen, die im selben Trait deklariert sind.

Traits können für jeden Datentyp implementiert werden. Im folgenden Beispiel definieren wir `Animal`, eine Gruppe von Methoden. Anschließend wird das `Animal`-Trait für den `Sheep`-Datentyp implementiert, was die Verwendung von Methoden aus `Animal` mit einem `Sheep` ermöglicht.

```rust
struct Sheep { naked: bool, name: &'static str }

trait Animal {
    // Assoziierte Funktionssignatur; `Self` bezieht sich auf den Implementortyp.
    fn new(name: &'static str) -> Self;

    // Methodensignaturen; diese werden einen String zurückgeben.
    fn name(&self) -> &'static str;
    fn noise(&self) -> &'static str;

    // Traits können Standardmethodendefinitionen bereitstellen.
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
            // Implementormethoden können die Traitmethoden des Implementors verwenden.
            println!("{} is already naked...", self.name());
        } else {
            println!("{} gets a haircut!", self.name);

            self.naked = true;
        }
    }
}

// Implementieren Sie das `Animal`-Trait für `Sheep`.
impl Animal for Sheep {
    // `Self` ist der Implementortyp: `Sheep`.
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

    // Standardtraitmethoden können überschrieben werden.
    fn talk(&self) {
        // Beispielsweise können wir etwas ruhige Kontemplation hinzufügen.
        println!("{} pauses briefly... {}", self.name, self.noise());
    }
}

fn main() {
    // In diesem Fall ist eine Typbezeichnung erforderlich.
    let mut dolly: Sheep = Animal::new("Dolly");
    // TODO ^ Versuchen Sie, die Typbezeichnungen zu entfernen.

    dolly.talk();
    dolly.shear();
    dolly.talk();
}
```
