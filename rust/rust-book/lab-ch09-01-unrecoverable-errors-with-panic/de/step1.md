# Unrecoverable Errors mit panic

Manchmal passieren in Ihrem Code schlimme Dinge, und es gibt nichts, was Sie dagegen tun können. In diesen Fällen hat Rust die `panic!`-Makro. Es gibt zwei Wege, um in der Praxis einen Panic auszulösen: indem Sie eine Aktion ausführen, die unseren Code zum Panikieren bringt (z. B. das Zugreifen auf ein Array außerhalb des Endes) oder indem Sie das `panic!`-Makro explizit aufrufen. In beiden Fällen verursachen wir einen Panic in unserem Programm. Standardmäßig drucken diese Panics eine Fehlermeldung, entspannen den Stack, bereinigen ihn und beenden das Programm. Über eine Umgebungsvariable können Sie auch dazu bringen, dass Rust den Funktionsstapel anzeigt, wenn ein Panic auftritt, um es einfacher zu verfolgen, wo der Panic herkommt.

> **Entspannen des Stapels oder Abbruch bei einem Panic**
>
> Standardmäßig beginnt das Programm beim Auftreten eines Panics mit dem _Entspannen_, was bedeutet, dass Rust den Stack zurückläuft und die Daten von jeder Funktion, die er trifft, bereinigt. Allerdings ist das Zurückgehen und Bereinigen sehr aufwendig. Rust erlaubt Ihnen daher, die Alternative des sofortigen _Abbruchs_ zu wählen, was das Programm beendet, ohne es zu bereinigen.
>
> Das von dem Programm verwendete Speicher muss dann vom Betriebssystem bereinigt werden. Wenn Sie in Ihrem Projekt das resultierende Binär so klein wie möglich machen müssen, können Sie von der Entspannung zum Abbruch bei einem Panic umschalten, indem Sie `panic = 'abort'` der entsprechenden `[profile]`-Abschnitte in Ihrer `Cargo.toml`-Datei hinzufügen. Beispielsweise, wenn Sie im Release-Modus bei einem Panic abbrechen möchten, fügen Sie dies hinzu:
>
> ```toml
> [profile.release]
> panic = 'abort'
> ```

Lassen Sie uns versuchen, `panic!` in einem einfachen Programm aufzurufen:

Dateiname: `src/main.rs`

```rust
fn main() {
    panic!("crash and burn");
}
```

Wenn Sie das Programm ausführen, sehen Sie etwas wie Folgendes:

    thread 'main' panicked at 'crash and burn', src/main.rs:2:5
    note: run with `RUST_BACKTRACE=1` environment variable to display
    a backtrace

Der Aufruf von `panic!` verursacht die in den letzten beiden Zeilen enthaltene Fehlermeldung. Die erste Zeile zeigt unsere Panikmeldung und den Ort in unserem Quellcode, an dem der Panic aufgetreten ist: _src/main.rs:2:5_ bedeutet, dass es die zweite Zeile, fünfte Stelle in unserer `src/main.rs`-Datei ist.

In diesem Fall ist die angegebene Zeile Teil unseres Codes, und wenn wir zu dieser Zeile gehen, sehen wir den `panic!`-Makroaufruf. In anderen Fällen kann der `panic!`-Aufruf in Code sein, den unser Code aufruft, und die Dateiname und Zeilennummer, die von der Fehlermeldung gemeldet werden, werden der Code eines anderen sein, in dem das `panic!`-Makro aufgerufen wird, nicht die Zeile unseres Codes, die letztendlich zum `panic!`-Aufruf geführt hat.

Wir können den Funktionsstapel des `panic!`-Aufrufs verwenden, um den Teil unseres Codes zu ermitteln, der das Problem verursacht. Um zu verstehen, wie man einen `panic!`-Funktionsstapel verwendet, betrachten wir ein weiteres Beispiel und sehen uns an, wie es aussieht, wenn ein `panic!`-Aufruf aufgrund eines Fehlers in unserer Bibliothek statt aus unserem Code, der das Makro direkt aufruft, erfolgt. Listing 9-1 hat einige Code, der versucht, einen Index in einem Vektor außerhalb des Bereichs gültiger Indizes zuzugreifen.

Dateiname: `src/main.rs`

```rust
fn main() {
    let v = vec![1, 2, 3];

    v[99];
}
```

Listing 9-1: Versuch, auf ein Element außerhalb des Endes eines Vektors zuzugreifen, was einen Aufruf von `panic!` verursachen wird

Hier versuchen wir, auf das 100. Element unseres Vektors zuzugreifen (was bei Index 99 ist, da der Index bei Null beginnt), aber der Vektor hat nur drei Elemente. In dieser Situation wird Rust in Panik geraten. Mit `[]` sollte ein Element zurückgegeben werden, aber wenn Sie einen ungültigen Index übergeben, gibt es kein Element, das Rust hier zurückgeben könnte, das korrekt wäre.

In C ist das Versuchen, hinter das Ende einer Datenstruktur hinauszulesen, undefiniertes Verhalten. Sie könnten das bekommen, was sich an der Stelle im Speicher befindet, die diesem Element in der Datenstruktur entsprechen würde, auch wenn der Speicher nicht zu dieser Struktur gehört. Dies wird als _Buffer-Überlesen_ bezeichnet und kann zu Sicherheitslücken führen, wenn ein Angreifer in der Lage ist, den Index so zu manipulieren, dass er Daten liest, die er nicht lesen darf, die nach der Datenstruktur gespeichert sind.

Um Ihr Programm vor dieser Art von Schwachstelle zu schützen, wird Rust bei einem Versuch, ein Element an einem Index zu lesen, der nicht existiert, die Ausführung stoppen und nicht weitermachen. Lassen Sie uns es ausprobieren und sehen:

    thread 'main' panicked at 'index out of bounds: the len is 3 but the index is
    99', src/main.rs:4:5
    note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

Dieser Fehler zeigt auf Zeile 4 unserer `main.rs`, an der wir versuchen, auf `index` zuzugreifen.

Die `note:`-Zeile sagt uns, dass wir die `RUST_BACKTRACE`-Umgebungsvariable setzen können, um einen Funktionsstapel zu erhalten, der genau zeigt, was passiert ist, um den Fehler zu verursachen. Ein _Funktionsstapel_ ist eine Liste aller Funktionen, die aufgerufen wurden, um zu diesem Punkt zu gelangen. Funktionsstapel in Rust funktionieren wie in anderen Sprachen: Der Schlüssel zum Lesen des Funktionsstapels besteht darin, von oben zu beginnen und bis Sie Dateien sehen, die Sie geschrieben haben, zu lesen. Das ist der Punkt, an dem das Problem entstanden ist. Die Zeilen über diesem Punkt sind Code, den Ihr Code aufgerufen hat; die Zeilen darunter sind Code, der Ihren Code aufgerufen hat. Diese davor- und danach-Zeilen können Code von Rust-Core, Standardbibliothekscode oder Crates umfassen, die Sie verwenden. Lassen Sie uns versuchen, einen Funktionsstapel zu erhalten, indem wir die `RUST_BACKTRACE`-Umgebungsvariable auf einen beliebigen Wert außer `0` setzen. Listing 9-2 zeigt eine Ausgabe, die ähnlich derer ist, die Sie sehen werden.

```bash
$ RUST_BACKTRACE=1 cargo run
thread 'main' panicked at 'index out of bounds: the len is 3 but the index is
99', src/main.rs:4:5
stack backtrace:
0: rust_begin_unwind
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/std
/src/panicking.rs:584:5
1: core::panicking::panic_fmt
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/panicking.rs:142:14
2: core::panicking::panic_bounds_check
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/panicking.rs:84:5
3: < usize as core::slice::index::SliceIndex < [T] >> ::index
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/slice/index.rs:242:10
4: core::slice::index:: core::ops::index::Index [T] < impl < I > for > ::index
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/slice/index.rs:18:9
5: < alloc::vec::Vec < T,A > as core::ops::index::Index < I >> ::index
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/alloc
/src/vec/mod.rs:2591:9
6: panic::main
at./src/main.rs:4:5
7: core::ops::function::FnOnce::call_once
at /rustc/e092d0b6b43f2de967af0887873151bb1c0b18d3/library/core
/src/ops/function.rs:248:5
note: Some details are omitted, run with $(RUST_BACKTRACE=full) for a verbose
backtrace.
```

Listing 9-2: Der Funktionsstapel, der durch einen Aufruf von `panic!` generiert wird, wenn die Umgebungsvariable `RUST_BACKTRACE` gesetzt ist

Das ist eine Menge Ausgabe! Die genaue Ausgabe, die Sie sehen, kann je nach Betriebssystem und Rust-Version unterschiedlich sein. Um Funktionsstapel mit dieser Information zu erhalten, müssen die Debugsymbole aktiviert sein. Debugsymbole werden standardmäßig aktiviert, wenn Sie `cargo build` oder `cargo run` ohne das `--release`-Flag verwenden, wie wir es hier tun.

In der Ausgabe in Listing 9-2 zeigt die 6. Zeile des Funktionsstapels auf die Zeile in unserem Projekt, die das Problem verursacht: Zeile 4 von `src/main.rs`. Wenn wir nicht möchten, dass unser Programm in Panik gerät, sollten wir unsere Untersuchung am Ort beginnen, der durch die erste Zeile angegeben wird, in der eine Datei erwähnt wird, die wir geschrieben haben. In Listing 9-1, in dem wir absichtlich Code geschrieben haben, der in Panik gerät, ist die Art, den Panic zu beheben, darin, kein Element außerhalb des Bereichs der Vektorindizes anzufordern. Wenn Ihr Code in Zukunft in Panik gerät, müssen Sie herausfinden, welche Aktion der Code mit welchen Werten ausführt, um den Panic zu verursachen, und was der Code stattdessen tun sollte.

Wir werden im Abschnitt "To panic! or Not to panic!" wieder auf `panic!` zurückkommen und wann wir `panic!` verwenden sollten und nicht sollten, um Fehlerbedingungen zu behandeln. Als Nächstes werden wir uns ansehen, wie man von einem Fehler mithilfe von `Result` recovert.
