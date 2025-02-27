# `Option` & `unwrap`

Im letzten Beispiel haben wir gezeigt, dass wir das Programm willkürlich zum Absturz bringen können. Wir haben unserem Programm befohlen, `panic` zu erzeugen, wenn wir eine süße Limonade trinken. Aber was passiert, wenn wir _irgend_ einen Drink erwarten, aber keinen erhalten? Dieser Fall wäre genauso schlimm, also muss er behandelt werden!

Wir _könnten_ dies gegen die leere Zeichenkette (`""`) testen, wie wir es bei einer Limonade tun. Da wir Rust verwenden, lassen wir stattdessen den Compiler Fälle aufzeigen, in denen kein Drink vorhanden ist.

Eine `enum` namens `Option<T>` in der `std`-Bibliothek wird verwendet, wenn das Fehlen möglich ist. Sie manifestiert sich als eine von zwei "Optionen":

- `Some(T)`: Ein Element vom Typ `T` wurde gefunden
- `None`: Kein Element wurde gefunden

Diese Fälle können entweder explizit über `match` behandelt oder implizit mit `unwrap` behandelt werden. Die implizite Behandlung wird entweder das innere Element zurückgeben oder `panic` auslösen.

Beachten Sie, dass es möglich ist, `panic` manuell mit `expect` anzupassen, aber `unwrap` liefert uns sonst einen weniger sinnvollen Output als die explizite Behandlung. Im folgenden Beispiel liefert die explizite Behandlung ein kontrollierteres Ergebnis, während die Möglichkeit besteht, `panic` zu erzeugen, wenn gewünscht.

```rust
// Der Erwachsene hat alles gesehen und kann jeden Drink gut behandeln.
// Alle Drinks werden explizit mit `match` behandelt.
fn give_adult(drink: Option<&str>) {
    // Legen Sie für jeden Fall eine Aktion fest.
    match drink {
        Some("lemonade") => println!("Yuck! Zu süß."),
        Some(inner)   => println!("{}? Wie nett.", inner),
        None          => println!("Kein Drink? Oh, gut."),
    }
}

// Andere werden vor dem Trinken von süßen Drinks in Panik geraten.
// Alle Drinks werden implizit mit `unwrap` behandelt.
fn drink(drink: Option<&str>) {
    // `unwrap` gibt einen `panic` zurück, wenn es ein `None` erhält.
    let inside = drink.unwrap();
    if inside == "lemonade" { panic!("AAAaaaaa!!!!"); }

    println!("Ich liebe {}s!!!!!", inside);
}

fn main() {
    let water  = Some("water");
    let lemonade = Some("lemonade");
    let void  = None;

    give_adult(water);
    give_adult(lemonade);
    give_adult(void);

    let coffee = Some("coffee");
    let nothing = None;

    drink(coffee);
    drink(nothing);
}
```
