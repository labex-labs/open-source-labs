# Domain Specific Languages (DSLs)

Eine DSL ist eine kleine "Sprache", die in einem Rust-Makro eingebettet ist. Sie ist vollkommen gültiger Rust-Code, da das Makrosystem in normale Rust-Konstrukte expandiert, sieht aber wie eine kleine Sprache aus. Dies ermöglicht es Ihnen, eine präzise oder intuitive Syntax für bestimmte spezielle Funktionen (innerhalb der Grenzen) zu definieren.

Angenommen, ich möchte eine kleine Taschenrechner-API definieren. Ich möchte einen Ausdruck übergeben und das Ergebnis auf der Konsole ausgeben.

```rust
macro_rules! calculate {
    (eval $e:expr) => {
        {
            let val: usize = $e; // Zwingt die Typen zu ganzen Zahlen
            println!("{} = {}", stringify!{$e}, val);
        }
    };
}

fn main() {
    calculate! {
        eval 1 + 2 // hehehe `eval` ist _kein_ Rust-Schlüsselwort!
    }

    calculate! {
        eval (1 + 2) * (3 / 4)
    }
}
```

Ausgabe:

```txt
1 + 2 = 3
(1 + 2) * (3 / 4) = 0
```

Dies war ein sehr einfaches Beispiel.

Beachten Sie auch die zwei Paare von geschweiften Klammern im Makro. Die äußeren gehören zur Syntax von `macro_rules!` neben `()` oder `[]`.
