# Kombinatoren: `map`

`match` ist eine gültige Methode zur Behandlung von `Option`s. Allerdings können Sie sich schließlich daran gewöhnen, dass häufige Verwendung lästig ist, insbesondere bei Operationen, die nur mit einer Eingabe gültig sind. In diesen Fällen können Kombinatoren verwendet werden, um die Kontrollstruktur auf modulare Weise zu verwalten.

`Option` hat eine integrierte Methode namens `map()`, ein Kombinator zur einfachen Zuordnung von `Some -> Some` und `None -> None`. Mehrere `map()`-Aufrufe können miteinander verkettet werden, um noch mehr Flexibilität zu erzielen.

Im folgenden Beispiel ersetzt `process()` alle vorherigen Funktionen, bleibt dabei aber kompakt.

```rust
#![allow(dead_code)]

#[derive(Debug)] enum Food { Apple, Carrot, Potato }

#[derive(Debug)] struct Peeled(Food);
#[derive(Debug)] struct Chopped(Food);
#[derive(Debug)] struct Cooked(Food);

// Das Entschälen von Lebensmitteln. Wenn es keines gibt, dann geben wir `None` zurück.
// Andernfalls geben wir das entschälte Lebensmittel zurück.
fn peel(food: Option<Food>) -> Option<Peeled> {
    match food {
        Some(food) => Some(Peeled(food)),
        None       => None,
    }
}

// Das Zerkleinern von Lebensmitteln. Wenn es keines gibt, dann geben wir `None` zurück.
// Andernfalls geben wir das zerkleinerte Lebensmittel zurück.
fn chop(peeled: Option<Peeled>) -> Option<Chopped> {
    match peeled {
        Some(Peeled(food)) => Some(Chopped(food)),
        None               => None,
    }
}

// Das Kochen von Lebensmitteln. Hier demonstrieren wir `map()` anstelle von `match` für den Fallunterschied.
fn cook(chopped: Option<Chopped>) -> Option<Cooked> {
    chopped.map(|Chopped(food)| Cooked(food))
}

// Eine Funktion, um Lebensmittel nacheinander zu schälen, zu zerkleinern und zu kochen.
// Wir verkettieren mehrere Verwendung von `map()`, um den Code zu vereinfachen.
fn process(food: Option<Food>) -> Option<Cooked> {
    food.map(|f| Peeled(f))
     .map(|Peeled(f)| Chopped(f))
     .map(|Chopped(f)| Cooked(f))
}

// Überprüfen, ob es Lebensmittel gibt, bevor wir es versuchen zu essen!
fn eat(food: Option<Cooked>) {
    match food {
        Some(food) => println!("Mmm. I love {:?}", food),
        None       => println!("Oh no! It wasn't edible."),
    }
}

fn main() {
    let apple = Some(Food::Apple);
    let carrot = Some(Food::Carrot);
    let potato = None;

    let cooked_apple = cook(chop(peel(apple)));
    let cooked_carrot = cook(chop(peel(carrot)));
    // Probieren wir jetzt die einfacher aussehende `process()` aus.
    let cooked_potato = process(potato);

    eat(cooked_apple);
    eat(cooked_carrot);
    eat(cooked_potato);
}
```
