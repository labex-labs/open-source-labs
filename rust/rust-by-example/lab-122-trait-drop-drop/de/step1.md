# Drop

Das `Drop`-Trait hat nur eine Methode: `drop`, die automatisch aufgerufen wird, wenn ein Objekt außer Gültigkeitsbereich gelangt. Die Hauptanwendung des `Drop`-Traits besteht darin, die Ressourcen freizugeben, die die Implementierungsinstanz besitzt.

`Box`, `Vec`, `String`, `File` und `Process` sind einige Beispiele für Typen, die das `Drop`-Trait implementieren, um Ressourcen freizugeben. Das `Drop`-Trait kann auch für beliebige benutzerdefinierte Datentypen manuell implementiert werden.

Im folgenden Beispiel wird der `drop`-Funktion eine Ausgabe in die Konsole hinzugefügt, um anzuzeigen, wann sie aufgerufen wird.

```rust
struct Droppable {
    name: &'static str,
}

// Diese triviale Implementierung von `drop` fügt eine Ausgabe in die Konsole hinzu.
impl Drop for Droppable {
    fn drop(&mut self) {
        println!("> Dropping {}", self.name);
    }
}

fn main() {
    let _a = Droppable { name: "a" };

    // Block A
    {
        let _b = Droppable { name: "b" };

        // Block B
        {
            let _c = Droppable { name: "c" };
            let _d = Droppable { name: "d" };

            println!("Exiting block B");
        }
        println!("Just exited block B");

        println!("Exiting block A");
    }
    println!("Just exited block A");

    // Variable kann manuell mit der `drop`-Funktion verworfen werden
    drop(_a);
    // TODO ^ Versuchen Sie, diese Zeile auszukommentieren

    println!("end of the main function");

    // `_a` wird hier *nicht* erneut `drop`ed, da es bereits (manuell) `drop`ed wurde
}
```
