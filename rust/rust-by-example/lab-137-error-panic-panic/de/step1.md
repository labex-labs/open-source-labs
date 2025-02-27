# `panic`

Der einfachste Fehlerbehandlungsmechanismus, den wir betrachten werden, ist `panic`. Es druckt eine Fehlermeldung, beginnt mit dem Abwickeln des Stapels und beendet normalerweise das Programm. Hier rufen wir `panic` explizit bei unserer Fehlerbedingung auf:

```rust
fn drink(beverage: &str) {
    // Du solltest nicht zu viele süße Getränke trinken.
    if beverage == "lemonade" { panic!("AAAaaaaa!!!!"); }

    println!("Some refreshing {} is all I need.", beverage);
}

fn main() {
    drink("water");
    drink("lemonade");
}
```
