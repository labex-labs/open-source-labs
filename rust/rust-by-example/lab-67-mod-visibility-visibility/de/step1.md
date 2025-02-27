# Sichtbarkeit

Standardmäßig haben die Elemente in einem Modul private Sichtbarkeit, aber dies kann mit dem `pub`-Modifizierer überschrieben werden. Nur die öffentlichen Elemente eines Moduls können außerhalb des Modulbereichs zugegriffen werden.

```rust
// Ein Modul namens `my_mod`
mod my_mod {
    // Elemente in Modulen haben standardmäßig private Sichtbarkeit.
    fn private_function() {
        println!("aufgerufen `my_mod::private_function()`");
    }

    // Verwenden Sie den `pub`-Modifizierer, um die standardmäßige Sichtbarkeit zu überschreiben.
    pub fn function() {
        println!("aufgerufen `my_mod::function()`");
    }

    // Elemente können auf andere Elemente im selben Modul zugreifen,
    // auch wenn sie privat sind.
    pub fn indirect_access() {
        print!("aufgerufen `my_mod::indirect_access()`, das\n> ");
        private_function();
    }

    // Module können auch geschachtelt werden
    pub mod nested {
        pub fn function() {
            println!("aufgerufen `my_mod::nested::function()`");
        }

        #[allow(dead_code)]
        fn private_function() {
            println!("aufgerufen `my_mod::nested::private_function()`");
        }

        // Mit der `pub(in path)`-Syntax deklarierte Funktionen sind nur innerhalb des angegebenen Pfads sichtbar. `path` muss ein übergeordnetes oder Vorfahrenmodul sein
        pub(in crate::my_mod) fn public_function_in_my_mod() {
            print!("aufgerufen `my_mod::nested::public_function_in_my_mod()`, das\n> ");
            public_function_in_nested();
        }

        // Mit der `pub(self)`-Syntax deklarierte Funktionen sind nur innerhalb des aktuellen Moduls sichtbar, was dem Verlassen ihrer Privatsphäre gleichkommt
        pub(self) fn public_function_in_nested() {
            println!("aufgerufen `my_mod::nested::public_function_in_nested()`");
        }

        // Mit der `pub(super)`-Syntax deklarierte Funktionen sind nur innerhalb des übergeordneten Moduls sichtbar
        pub(super) fn public_function_in_super_mod() {
            println!("aufgerufen `my_mod::nested::public_function_in_super_mod()`");
        }
    }

    pub fn call_public_function_in_my_mod() {
        print!("aufgerufen `my_mod::call_public_function_in_my_mod()`, das\n> ");
        nested::public_function_in_my_mod();
        print!("> ");
        nested::public_function_in_super_mod();
    }

    // pub(crate) macht Funktionen nur innerhalb des aktuellen Kratzers sichtbar
    pub(crate) fn public_function_in_crate() {
        println!("aufgerufen `my_mod::public_function_in_crate()`");
    }

    // Geschachtelte Module folgen den gleichen Regeln für Sichtbarkeit
    mod private_nested {
        #[allow(dead_code)]
        pub fn function() {
            println!("aufgerufen `my_mod::private_nested::function()`");
        }

        // Private übergeordnete Elemente beschränken immer noch die Sichtbarkeit eines untergeordneten Elements,
        // auch wenn es als sichtbar innerhalb eines größeren Bereichs deklariert ist.
        #[allow(dead_code)]
        pub(crate) fn restricted_function() {
            println!("aufgerufen `my_mod::private_nested::restricted_function()`");
        }
    }
}

fn function() {
    println!("aufgerufen `function()`");
}

fn main() {
    // Module ermöglichen die Unterscheidung zwischen Elementen mit demselben Namen.
    function();
    my_mod::function();

    // Öffentliche Elemente, einschließlich derer in geschachtelten Modulen, können
    // von außerhalb des übergeordneten Moduls zugegriffen werden.
    my_mod::indirect_access();
    my_mod::nested::function();
    my_mod::call_public_function_in_my_mod();

    // pub(crate)-Elemente können von überall im selben Kratzer aufgerufen werden
    my_mod::public_function_in_crate();

    // pub(in path)-Elemente können nur von innerhalb des angegebenen Moduls aufgerufen werden
    // Fehler! Funktion `public_function_in_my_mod` ist privat
    //my_mod::nested::public_function_in_my_mod();
    // TODO ^ Versuchen Sie, diese Zeile zu entsperren

    // Private Elemente eines Moduls können nicht direkt zugegriffen werden, auch wenn
    // in einem öffentlichen Modul geschachtelt:

    // Fehler! `private_function` ist privat
    //my_mod::private_function();
    // TODO ^ Versuchen Sie, diese Zeile zu entsperren

    // Fehler! `private_function` ist privat
    //my_mod::nested::private_function();
    // TODO ^ Versuchen Sie, diese Zeile zu entsperren

    // Fehler! `private_nested` ist ein privates Modul
    //my_mod::private_nested::function();
    // TODO ^ Versuchen Sie, diese Zeile zu entsperren

    // Fehler! `private_nested` ist ein privates Modul
    //my_mod::private_nested::restricted_function();
    // TODO ^ Versuchen Sie, diese Zeile zu entsperren
}
```
