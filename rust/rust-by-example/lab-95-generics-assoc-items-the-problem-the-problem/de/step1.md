# Das Problem

Ein `trait`, der über seinen Containertyp generisch ist, hat Typangabevoraussetzungen - die Benutzer des `traits` _müssen_ alle seine generischen Typen angeben.

Im folgenden Beispiel erlaubt das `Contains`-`trait` die Verwendung der generischen Typen `A` und `B`. Anschließend wird das `trait` für den `Container`-Typ implementiert, wobei `i32` für `A` und `B` angegeben wird, damit es mit `fn difference()` verwendet werden kann.

Da `Contains` generisch ist, müssen wir alle generischen Typen für `fn difference()` explizit angeben. Im praktischen Einsatz möchten wir eine Möglichkeit haben, auszudrücken, dass `A` und `B` durch die _Eingabe_ `C` bestimmt werden. Wie Sie im nächsten Abschnitt sehen werden, bieten assoziierte Typen genau diese Möglichkeit.

```rust
struct Container(i32, i32);

// Ein trait, das überprüft, ob 2 Elemente im Container gespeichert sind.
// Ruft auch den ersten oder letzten Wert ab.
trait Contains<A, B> {
    fn contains(&self, _: &A, _: &B) -> bool; // Erfordert explizit `A` und `B`.
    fn first(&self) -> i32; // Erfordert nicht explizit `A` oder `B`.
    fn last(&self) -> i32;  // Erfordert nicht explizit `A` oder `B`.
}

impl Contains<i32, i32> for Container {
    // True, wenn die gespeicherten Zahlen gleich sind.
    fn contains(&self, number_1: &i32, number_2: &i32) -> bool {
        (&self.0 == number_1) && (&self.1 == number_2)
    }

    // Holt die erste Zahl.
    fn first(&self) -> i32 { self.0 }

    // Holt die letzte Zahl.
    fn last(&self) -> i32 { self.1 }
}

// `C` enthält `A` und `B`. In Anbetracht dessen ist es lästig, `A` und
// `B` erneut auszudrücken.
fn difference<A, B, C>(container: &C) -> i32 where
    C: Contains<A, B> {
    container.last() - container.first()
}

fn main() {
    let number_1 = 3;
    let number_2 = 10;

    let container = Container(number_1, number_2);

    println!("Enthält der Container {} und {}: {}",
        &number_1, &number_2,
        container.contains(&number_1, &number_2));
    println!("Erste Zahl: {}", container.first());
    println!("Letzte Zahl: {}", container.last());

    println!("Der Unterschied ist: {}", difference(&container));
}
```
