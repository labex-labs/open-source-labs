# Rückgabe von Traits mit `dyn`

Der Rust-Compiler muss wissen, wie viel Speicher der Rückgabetyp jeder Funktion benötigt. Dies bedeutet, dass alle Ihre Funktionen einen konkreten Typ zurückgeben müssen. Anders als in anderen Sprachen können Sie keine Funktion schreiben, die `Animal` zurückgibt, wenn Sie ein Trait wie `Animal` haben, da seine verschiedenen Implementierungen unterschiedliche Speicherbedarf haben werden.

Es gibt jedoch eine einfache Lösung. Anstatt einen Traitobjekt direkt zurückzugeben, geben unsere Funktionen eine `Box` zurück, die ein `Animal` _enthält_. Eine `Box` ist einfach ein Verweis auf einen Speicherbereich im Heap. Da ein Verweis eine statisch bekannte Größe hat und der Compiler gewährleisten kann, dass er auf einen auf dem Heap zugewiesenen `Animal` zeigt, können wir ein Trait aus unserer Funktion zurückgeben!

Rust versucht, so explizit wie möglich zu sein, wenn es Speicher auf dem Heap allokiert. Wenn Ihre Funktion auf diese Weise einen Zeiger auf ein Trait auf dem Heap zurückgibt, müssen Sie den Rückgabetyp mit dem Schlüsselwort `dyn` schreiben, z. B. `Box<dyn Animal>`.

```rust
struct Sheep {}
struct Cow {}

trait Animal {
    // Signatur der Instanzmethode
    fn noise(&self) -> &'static str;
}

// Implementieren Sie das `Animal`-Trait für `Sheep`.
impl Animal for Sheep {
    fn noise(&self) -> &'static str {
        "baaaaah!"
    }
}

// Implementieren Sie das `Animal`-Trait für `Cow`.
impl Animal for Cow {
    fn noise(&self) -> &'static str {
        "moooooo!"
    }
}

// Gibt eine Struktur zurück, die `Animal` implementiert, aber wir wissen bei der Kompilierung nicht, welche.
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
