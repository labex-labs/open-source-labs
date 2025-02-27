# HashMap

Während Vektoren Werte anhand eines ganzzahligen Index speichern, speichern `HashMap`s Werte nach Schlüssel. `HashMap`-Schlüssel können Booleans, Integer, Strings oder jeder andere Typ sein, der das `Eq`- und `Hash`-Trait implementiert. Mehr dazu im nächsten Abschnitt.

Wie Vektoren sind `HashMap`s wächstbar, aber HashMaps können sich auch selbst verkleinern, wenn sie zu viel Speicherplatz haben. Sie können ein HashMap mit einer bestimmten Anfangskapazität mit `HashMap::with_capacity(uint)` erstellen oder `HashMap::new()` verwenden, um ein HashMap mit einer standardmäßigen Anfangskapazität zu erhalten (empfohlen).

```rust
use std::collections::HashMap;

fn call(number: &str) -> &str {
    match number {
        "798-1364" => "Wir bitten um Entschuldigung, der Anruf kann nicht wie gewählt durchgeführt werden. Bitten Sie, aufzuhängen und erneut zu versuchen.",
        "645-7689" => "Hallo, das ist Mr. Awesome's Pizza. Mein Name ist Fred. Was kann ich für Sie tun?",
        _ => "Hi! Wer ist das nochmal?"
    }
}

fn main() {
    let mut contacts = HashMap::new();

    contacts.insert("Daniel", "798-1364");
    contacts.insert("Ashley", "645-7689");
    contacts.insert("Katie", "435-8291");
    contacts.insert("Robert", "956-1745");

    // Nimmt eine Referenz und gibt Option<&V> zurück
    match contacts.get(&"Daniel") {
        Some(&number) => println!("Rufe Daniel an: {}", call(number)),
        _ => println!("Habe Daniels Nummer nicht."),
    }

    // `HashMap::insert()` gibt `None` zurück,
    // wenn der eingefügte Wert neu ist, `Some(value)` andernfalls
    contacts.insert("Daniel", "164-6743");

    match contacts.get(&"Ashley") {
        Some(&number) => println!("Rufe Ashley an: {}", call(number)),
        _ => println!("Habe Ashleys Nummer nicht."),
    }

    contacts.remove(&"Ashley");

    // `HashMap::iter()` gibt einen Iterator zurück, der
    // (&'a Schlüssel, &'a Wert)-Paare in beliebiger Reihenfolge liefert.
    for (contact, &number) in contacts.iter() {
        println!("Rufe {} an: {}", contact, call(number));
    }
}
```

Weitere Informationen darüber, wie Hashing und Hash Maps (manchmal auch Hash Tabellen genannt) funktionieren, finden Sie auf der Wikipedia-Seite zu Hash Tabellen.
