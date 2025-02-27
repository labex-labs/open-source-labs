# `super` und `self`

Die Schlüsselwörter `super` und `self` können im Pfad verwendet werden, um Mehrdeutigkeiten beim Zugriff auf Elemente zu vermeiden und unnötiges Hardcodieren von Pfaden zu verhindern.

```rust
fn function() {
    println!("called `function()`");
}

mod cool {
    pub fn function() {
        println!("called `cool::function()`");
    }
}

mod my {
    fn function() {
        println!("called `my::function()`");
    }

    mod cool {
        pub fn function() {
            println!("called `my::cool::function()`");
        }
    }

    pub fn indirect_call() {
        // Lassen Sie uns alle Funktionen mit dem Namen `function` aus diesem Bereich aufrufen!
        print!("called `my::indirect_call()`, that\n> ");

        // Das Schlüsselwort `self` bezieht sich auf den aktuellen Modulbereich - in diesem Fall `my`.
        // Aufrufen von `self::function()` und direktem Aufrufen von `function()` liefert
        // das gleiche Ergebnis, da beide auf die gleiche Funktion verweisen.
        self::function();
        function();

        // Wir können auch `self` verwenden, um auf ein anderes Modul innerhalb von `my` zuzugreifen:
        self::cool::function();

        // Das Schlüsselwort `super` bezieht sich auf den übergeordneten Bereich (außerhalb des `my`-Moduls).
        super::function();

        // Dies wird an die `cool::function` im *Kasten*-Bereich gebunden.
        // Im Falle eines Kastenbereichs ist dies der äußerste Bereich.
        {
            use crate::cool::function as root_function;
            root_function();
        }
    }
}

fn main() {
    my::indirect_call();
}
```
