# Entschärfung von überlappenden Merkmalen

Ein Typ kann viele verschiedene Merkmale implementieren. Was ist, wenn zwei Merkmale denselben Namen erfordern? Beispielsweise könnten viele Merkmale eine Methode namens `get()` haben. Sie könnten sogar unterschiedliche Rückgabetypen haben!

Gute Nachricht: Da jede Merkmalsimplementierung ihren eigenen `impl`-Block erhält, ist klar, welches Merkmals-`get`-Methode Sie implementieren.

Was ist, wenn es darum geht, diese Methoden _aufzurufen_? Um zwischen ihnen zu entscheiden, müssen wir die vollqualifizierte Syntax verwenden.

```rust
trait UsernameWidget {
    // Holen Sie sich den ausgewählten Benutzernamen aus diesem Widget
    fn get(&self) -> String;
}

trait AgeWidget {
    // Holen Sie sich das ausgewählte Alter aus diesem Widget
    fn get(&self) -> u8;
}

// Ein Formular mit sowohl einem UsernameWidget als auch einem AgeWidget
struct Form {
    username: String,
    age: u8,
}

impl UsernameWidget for Form {
    fn get(&self) -> String {
        self.username.clone()
    }
}

impl AgeWidget for Form {
    fn get(&self) -> u8 {
        self.age
    }
}

fn main() {
    let form = Form {
        username: "rustacean".to_owned(),
        age: 28,
    };

    // Wenn Sie diese Zeile entschärfen, erhalten Sie einen Fehler, der besagt,
    // dass "mehrere `get` gefunden wurden". Denn schließlich gibt es mehrere Methoden
    // mit dem Namen `get`.
    // println!("{}", form.get());

    let username = <Form as UsernameWidget>::get(&form);
    assert_eq!("rustacean".to_owned(), username);
    let age = <Form as AgeWidget>::get(&form);
    assert_eq!(28, age);
}
```
