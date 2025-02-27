# `abort` und `unwind`

Der vorherige Abschnitt veranschaulicht den Fehlerbehandlungsmechanismus `panic`. Verschiedene Codepfade können bedingt kompiliert werden, basierend auf der Panik-Einstellung. Die derzeit verfügbaren Werte sind `unwind` und `abort`.

Aufbauend auf dem vorherigen Limonadenbeispiel verwenden wir die Panik-Strategie explizit, um verschiedene Codezeilen zu testen.

```rust
fn drink(beverage: &str) {
   // Du solltest nicht zu viele süße Getränke trinken.
    if beverage == "lemonade" {
        if cfg!(panic="abort"){ println!("Dies ist nicht deine Party. Lauf!!!!");}
        else{ println!("Spuck es aus!!!!");}
    }
    else{ println!("Ein bisschen erfrischendes {} ist alles, was ich brauche.", beverage); }
}

fn main() {
    drink("water");
    drink("lemonade");
}
```

Hier ist ein weiteres Beispiel, das sich auf die Umformulierung von `drink()` konzentriert und das `unwind`-Schlüsselwort explizit verwendet.

```rust
#[cfg(panic = "unwind")]
fn ah(){ println!("Spuck es aus!!!!");}

#[cfg(not(panic="unwind"))]
fn ah(){ println!("Dies ist nicht deine Party. Lauf!!!!");}

fn drink(beverage: &str){
    if beverage == "lemonade"{ ah();}
    else{println!("Ein bisschen erfrischendes {} ist alles, was ich brauche.", beverage);}
}

fn main() {
    drink("water");
    drink("lemonade");
}
```

Die Panik-Strategie kann von der Befehlszeile aus mit `abort` oder `unwind` festgelegt werden.

```console
rustc lemonade.rs -C panic=abort
```
