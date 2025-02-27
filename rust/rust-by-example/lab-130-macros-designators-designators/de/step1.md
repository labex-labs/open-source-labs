# Bezeichner

Die Argumente eines Makros werden mit einem Dollarzeichen `$` vorangestellt und mit einem _Bezeichner_ typannotiert:

```rust
macro_rules! create_function {
    // Dieses Macro nimmt ein Argument vom Bezeichner `ident` entgegen und
    // erstellt eine Funktion mit dem Namen `$func_name`.
    // Der Bezeichner `ident` wird für Variablennamen/Funktionsnamen verwendet.
    ($func_name:ident) => {
        fn $func_name() {
            // Das Macro `stringify!` wandelt ein `ident` in einen String um.
            println!("You called {:?}()",
                     stringify!($func_name));
        }
    };
}

// Erstellen Sie Funktionen mit den Namen `foo` und `bar` mit dem obigen Macro.
create_function!(foo);
create_function!(bar);

macro_rules! print_result {
    // Dieses Macro nimmt einen Ausdruck vom Typ `expr` entgegen und druckt
    // ihn als String zusammen mit seinem Ergebnis.
    // Der Bezeichner `expr` wird für Ausdrücke verwendet.
    ($expression:expr) => {
        // `stringify!` wird den Ausdruck *so wie er ist* in einen String umwandeln.
        println!("{:?} = {:?}",
                 stringify!($expression),
                 $expression);
    };
}

fn main() {
    foo();
    bar();

    print_result!(1u32 + 1);

    // Denken Sie daran, dass Blöcke ebenfalls Ausdrücke sind!
    print_result!({
        let x = 1u32;

        x * x + 2 * x - 1
    });
}
```

Dies sind einige der verfügbaren Bezeichner:

- `block`
- `expr` wird für Ausdrücke verwendet
- `ident` wird für Variablennamen/Funktionsnamen verwendet
- `item`
- `literal` wird für literale Konstanten verwendet
- `pat` (_Muster_)
- `path`
- `stmt` (_Anweisung_)
- `tt` (_Tokenbaum_)
- `ty` (_Typ_)
- `vis` (_Sichtbarkeitsqualifizierer_)

Für eine vollständige Liste siehe die \[Rust Reference\].
