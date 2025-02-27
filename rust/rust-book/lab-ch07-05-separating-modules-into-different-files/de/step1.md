# Separieren von Modulen in verschiedene Dateien

Bisher haben alle Beispiele in diesem Kapitel mehrere Module in einer Datei definiert. Wenn die Module groß werden, möchten Sie möglicherweise ihre Definitionen in eine separate Datei verschieben, um den Code leichter zu durchlaufen.

Nehmen wir beispielsweise den Code in Listing 7-17, der mehrere Restaurantmodule hatte. Wir extrahieren die Module in Dateien, anstatt alle Module in der Crate-Wurzeldatei zu definieren. In diesem Fall ist die Crate-Wurzeldatei `src/lib.rs`, aber dieses Verfahren funktioniert auch mit binären Crates, deren Crate-Wurzeldatei `src/main.rs` ist.

Zunächst extrahieren wir das `front_of_house`-Modul in seine eigene Datei. Entfernen Sie den Code innerhalb der geschweiften Klammern für das `front_of_house`-Modul, und lassen Sie nur die `mod front_of_house;`-Deklaration übrig, so dass `src/lib.rs` den in Listing 7-21 gezeigten Code enthält. Beachten Sie, dass dies erst kompiliert, wenn wir die Datei `src/front_of_house.rs` in Listing 7-22 erstellen.

Dateiname: `src/lib.rs`

```rust
mod front_of_house;

pub use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}
```

Listing 7-21: Deklarieren des `front_of_house`-Moduls, dessen Körper in `src/front_of_house.rs` sein wird

Als nächstes legen Sie den Code, der in den geschweiften Klammern war, in eine neue Datei namens `src/front_of_house.rs` ab, wie in Listing 7-22 gezeigt. Der Compiler weiß, in dieser Datei zu suchen, weil er in der Crate-Wurzel eine Moduldeklaration mit dem Namen `front_of_house` gefunden hat.

Dateiname: `src/front_of_house.rs`

```rust
pub mod hosting {
    pub fn add_to_waitlist() {}
}
```

Listing 7-22: Definitionen innerhalb des `front_of_house`-Moduls in `src/front_of_house.rs`

Beachten Sie, dass Sie eine Datei nur einmal mithilfe einer `mod`-Deklaration in Ihrem Modultree laden müssen. Sobald der Compiler weiß, dass die Datei Teil des Projekts ist (und weiß, wo im Modultree der Code liegt, weil Sie die `mod`-Anweisung platziert haben), sollten andere Dateien in Ihrem Projekt auf den geladenen Dateicode über einen Pfad zu der Stelle verweisen, an der er deklariert wurde, wie in "Pfade zur Referenz auf ein Element im Modultree" beschrieben. Mit anderen Worten, `mod` ist keine "Include"-Operation, die Sie in anderen Programmiersprachen kennenlernen könnten.

Als nächstes extrahieren wir das `hosting`-Modul in seine eigene Datei. Der Prozess ist etwas anders, da `hosting` ein Kindmodul von `front_of_house` ist, nicht des Wurzelmoduls. Wir legen die Datei für `hosting` in einem neuen Verzeichnis ab, das nach seinen Vorfahren im Modultree benannt wird, in diesem Fall _src/front_of_house_.

Um `hosting` zu verschieben, ändern wir `src/front_of_house.rs`, um nur die Deklaration des `hosting`-Moduls zu enthalten:

Dateiname: `src/front_of_house.rs`

```rust
pub mod hosting;
```

Dann erstellen wir ein `src/front_of_house`-Verzeichnis und eine `hosting.rs`-Datei, um die in dem `hosting`-Modul gemachten Definitionen zu enthalten:

Dateiname: `src/front_of_house/hosting.rs`

```rust
pub fn add_to_waitlist() {}
```

Wenn wir `hosting.rs` stattdessen im `src`-Verzeichnis ablegen, würde der Compiler erwarten, dass der `hosting.rs`-Code in einem `hosting`-Modul in der Crate-Wurzel deklariert ist, und nicht als Kindmodul von `front_of_house` deklariert ist. Die Regeln des Compilers für die Dateien, die für den Code von bestimmten Modulen überprüft werden sollen, bedeuten, dass die Verzeichnisse und Dateien dem Modultree näher entsprechen.

> **Alternative Dateipfade**
>
> Bisher haben wir die am idiomatischsten verwendeten Dateipfade behandelt, die der Rust-Compiler verwendet, aber Rust unterstützt auch einen älteren Dateipfadstil. Für ein Modul namens `front_of_house`, das in der Crate-Wurzel deklariert ist, sucht der Compiler nach dem Modulcode in:
>
> - `src/front_of_house.rs` (was wir behandelt haben)
> - `src/front_of_house/mod.rs` (älterer Stil, immer noch unterstützter Pfad)
>
> Für ein Modul namens `hosting`, das ein Untermodul von `front_of_house` ist, sucht der Compiler nach dem Modulcode in:
>
> - `src/front_of_house/hosting.rs` (was wir behandelt haben)
> - `src/front_of_house/hosting/mod.rs` (älterer Stil, immer noch unterstützter Pfad)
>
> Wenn Sie beide Stile für dasselbe Modul verwenden, erhalten Sie einen Compilerfehler. Es ist möglich, beide Stile für verschiedene Module im selben Projekt zu mischen, aber dies kann für Personen, die sich durch Ihr Projekt navigieren, verwirrend sein.
>
> Der Hauptnachteil des Stils, der Dateien namens `mod.rs` verwendet, ist, dass Ihr Projekt möglicherweise viele Dateien namens `mod.rs` enthält, was verwirrend werden kann, wenn Sie sie gleichzeitig in Ihrem Editor geöffnet haben.

Wir haben den Code jedes Moduls in eine separate Datei verschoben, und der Modultree bleibt gleich. Die Funktionsaufrufe in `eat_at_restaurant` funktionieren ohne jegliche Änderung, auch wenn die Definitionen in verschiedenen Dateien gespeichert sind. Mit dieser Technik können Sie Module zu neuen Dateien verschieben, wenn sie größer werden.

Beachten Sie, dass die `pub use crate::front_of_house::hosting`-Anweisung in `src/lib.rs` ebenfalls nicht geändert hat, und `use` hat auch keinen Einfluss auf die Dateien, die als Teil der Crate kompiliert werden. Das `mod`-Schlüsselwort deklariert Module, und Rust sucht in einer Datei mit demselben Namen wie das Modul nach dem Code, der in das Modul gehört.
