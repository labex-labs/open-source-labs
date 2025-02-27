# Pfade in den Gültigkeitsbereich mit dem `use`-Schlüsselwort bringen

Es kann unbequem und repetitiv vorkommen, die Pfade zum Aufrufen von Funktionen auszuschreiben. In Listing 7-7 mussten wir unabhängig davon, ob wir den absoluten oder relativen Pfad zur `add_to_waitlist`-Funktion gewählt haben, jedes Mal, wenn wir `add_to_waitlist` aufrufen wollten, auch `front_of_house` und `hosting` angeben. Glücklicherweise gibt es einen Weg, diesen Prozess zu vereinfachen: Wir können einmal einen Kurzschluss für einen Pfad mit dem `use`-Schlüsselwort erstellen und dann den kürzeren Namen überall im Gültigkeitsbereich verwenden.

In Listing 7-11 bringen wir das `crate::front_of_house::hosting`-Modul in den Gültigkeitsbereich der `eat_at_restaurant`-Funktion, sodass wir nur `hosting::add_to_waitlist` angeben müssen, um die `add_to_waitlist`-Funktion in `eat_at_restaurant` aufzurufen.

Dateiname: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}
```

Listing 7-11: Ein Modul in den Gültigkeitsbereich mit `use` bringen

Das Hinzufügen von `use` und eines Pfads in einem Gültigkeitsbereich ähnelt dem Erstellen eines Symbolischen Links im Dateisystem. Indem wir `use crate::front_of_house::hosting` im Crate-Root hinzufügen, ist `hosting` jetzt ein gültiger Name in diesem Gültigkeitsbereich, genau so, als wäre das `hosting`-Modul im Crate-Root definiert worden. Pfade, die mit `use` in den Gültigkeitsbereich gebracht werden, überprüfen auch die Privatsphäre, wie alle anderen Pfade.

Beachten Sie, dass `use` nur den Kurzschluss für den bestimmten Gültigkeitsbereich erstellt, in dem der `use`-Ausdruck vorkommt. Listing 7-12 verschiebt die `eat_at_restaurant`-Funktion in ein neues Kind-Modul namens `customer`, was dann ein anderer Gültigkeitsbereich als der `use`-Statement ist, sodass der Funktionskörper nicht kompilieren wird.

Dateiname: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting;

mod customer {
    pub fn eat_at_restaurant() {
        hosting::add_to_waitlist();
    }
}
```

Listing 7-12: Ein `use`-Statement gilt nur im Gültigkeitsbereich, in dem es steht.

Der Compilerfehler zeigt, dass der Kurzschluss innerhalb des `customer`-Moduls nicht mehr gilt:

```bash
error[E0433]: failed to resolve: use of undeclared crate or module `hosting`
  --> src/lib.rs:11:9
   |
11 |         hosting::add_to_waitlist();
   |         ^^^^^^^ use of undeclared crate or module `hosting`

warning: unused import: `crate::front_of_house::hosting`
 --> src/lib.rs:7:5
  |
7 | use crate::front_of_house::hosting;
  |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  |
  = note: `#[warn(unused_imports)]` on by default
```

Beachten Sie, dass es auch eine Warnung gibt, dass der `use` in seinem Gültigkeitsbereich nicht mehr verwendet wird! Um dieses Problem zu beheben, verschieben Sie den `use` ebenfalls innerhalb des `customer`-Moduls oder verweisen Sie auf den Kurzschluss im Elternmodul mit `super::hosting` innerhalb des Kind-Moduls `customer`.
