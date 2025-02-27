# Lifetime Elision

Sie haben gelernt, dass jede Referenz eine Lebenszeit hat und dass Sie Lebenszeitparameter für Funktionen oder Structs angeben müssen, die Referenzen verwenden. Allerdings hatten wir in Listing 4-9 eine Funktion, die erneut in Listing 10-25 gezeigt wird, die ohne Lebenszeitannotationen kompilierte.

Dateiname: `src/lib.rs`

```rust
fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
}
```

Listing 10-25: Eine Funktion, die wir in Listing 4-9 definiert haben, die ohne Lebenszeitannotationen kompilierte, obwohl der Parameter und der Rückgabetyp Referenzen sind

Der Grund, warum diese Funktion ohne Lebenszeitannotationen kompiliert, liegt in der Geschichte: In frühen Versionen (vor 1.0) von Rust hätte dieser Code nicht kompiliert, weil jede Referenz eine explizite Lebenszeit benötigte. Damals hätte die Funktionssignatur so ausgesehen:

```rust
fn first_word<'a>(s: &'a str) -> &'a str {
```

Nachdem die Rust-Mannschaft viel Rust-Code geschrieben hatte, stellte sie fest, dass Rust-Programmierer in bestimmten Situationen immer wieder die gleichen Lebenszeitannotationen eingaben. Diese Situationen waren vorhersehbar und folgten einigen deterministischen Mustern. Die Entwickler haben diese Muster in den Compilercode programmiert, sodass der Borrow-Checker in diesen Situationen die Lebenszeiten ableiten und keine expliziten Annotations benötigen konnte.

Dieser Teil der Rust-Geschichte ist relevant, weil es möglich ist, dass weitere deterministische Muster auftauchen und zum Compiler hinzugefügt werden. In Zukunft könnten sogar noch weniger Lebenszeitannotationen erforderlich sein.

Die Muster, die in die Rust-Analyse von Referenzen programmiert sind, werden als _Lebenszeitelisionsregeln_ bezeichnet. Dies sind keine Regeln, die die Programmierer befolgen müssen; es sind eine Reihe von speziellen Fällen, die der Compiler betrachtet, und wenn Ihr Code diesen Fällen entspricht, müssen Sie die Lebenszeiten nicht explizit schreiben.

Die Elisionsregeln bieten keine vollständige Inferenz. Wenn Rust die Regeln deterministisch anwendet, aber es immer noch Unklarheit darüber besteht, welche Lebenszeiten die Referenzen haben, wird der Compiler nicht raten, welche Lebenszeit die verbleibenden Referenzen haben sollten. Anstatt zu raten, gibt der Compiler Ihnen einen Fehler, den Sie durch Hinzufügen der Lebenszeitannotationen beheben können.

Lebenszeiten von Funktions- oder Methodenparametern werden als _Eingangslebenszeiten_ bezeichnet, und Lebenszeiten von Rückgabewerten werden als _Ausgangslebenszeiten_ bezeichnet.

Der Compiler verwendet drei Regeln, um die Lebenszeiten der Referenzen zu ermitteln, wenn keine expliziten Annotations vorhanden sind. Die erste Regel gilt für Eingangslebenszeiten, und die zweiten und dritten Regeln gelten für Ausgangslebenszeiten. Wenn der Compiler am Ende der drei Regeln angelangt ist und es immer noch Referenzen gibt, für die er die Lebenszeiten nicht ermitteln kann, wird der Compiler mit einem Fehler abbrechen. Diese Regeln gelten für `fn`-Definitionen sowie für `impl`-Blöcke.

Die erste Regel ist, dass der Compiler einem jeden Parameter, der eine Referenz ist, einen Lebenszeitparameter zuweist. Mit anderen Worten, eine Funktion mit einem Parameter bekommt einen Lebenszeitparameter: `fn foo<'a>(x: &'a i32)`; eine Funktion mit zwei Parametern bekommt zwei separate Lebenszeitparameter: `fn foo<'a, 'b>(x: &'a i32, y: &'b i32)`; und so weiter.

Die zweite Regel ist, dass, wenn es genau einen Eingangslebenszeitparameter gibt, diese Lebenszeit allen Ausgangslebenszeitparametern zugewiesen wird: `fn foo<'a>(x: &'a i32) -> &'a i32`.

Die dritte Regel ist, dass, wenn es mehrere Eingangslebenszeitparameter gibt, aber einer von ihnen `&self` oder `&mut self` ist, weil dies eine Methode ist, die Lebenszeit von `self` allen Ausgangslebenszeitparametern zugewiesen wird. Diese dritte Regel macht Methoden viel lesbarer und schreibbarer, weil weniger Symbole erforderlich sind.

Lassen Sie uns vorstellen, dass wir der Compiler sind. Wir werden diese Regeln anwenden, um die Lebenszeiten der Referenzen in der Signatur der `first_word`-Funktion in Listing 10-25 zu ermitteln. Die Signatur beginnt ohne jede Lebenszeit, die mit den Referenzen assoziiert ist:

```rust
fn first_word(s: &str) -> &str {
```

Dann wendet der Compiler die erste Regel an, die angibt, dass jeder Parameter seine eigene Lebenszeit bekommt. Wir werden es wie üblich `'a` nennen, also sieht die Signatur jetzt so aus:

```rust
fn first_word<'a>(s: &'a str) -> &str {
```

Die zweite Regel tritt in Kraft, weil es genau einen Eingangslebenszeitparameter gibt. Die zweite Regel besagt, dass die Lebenszeit des einen Eingangsparameters dem Ausgangslebenszeitparameter zugewiesen wird, also sieht die Signatur jetzt so aus:

```rust
fn first_word<'a>(s: &'a str) -> &'a str {
```

Jetzt haben alle Referenzen in dieser Funktionssignatur Lebenszeiten, und der Compiler kann seine Analyse fortsetzen, ohne dass der Programmierer die Lebenszeiten in dieser Funktionssignatur annotieren muss.

Schauen wir uns ein weiteres Beispiel an, diesmal mit der `longest`-Funktion, die keine Lebenszeitparameter hatte, als wir in Listing 10-20 damit begannen:

```rust
fn longest(x: &str, y: &str) -> &str {
```

Lassen Sie uns die erste Regel anwenden: Jeder Parameter bekommt seine eigene Lebenszeit. Diesmal haben wir zwei Parameter statt eines, also haben wir zwei Lebenszeiten:

```rust
fn longest<'a, 'b>(x: &'a str, y: &'b str) -> &str {
```

Sie können sehen, dass die zweite Regel nicht zutrifft, weil es mehr als einen Eingangslebenszeitparameter gibt. Die dritte Regel trifft auch nicht zu, weil `longest` eine Funktion und keine Methode ist, sodass keiner der Parameter `self` ist. Nachdem wir alle drei Regeln durchlaufen haben, haben wir immer noch nicht herausgefunden, was die Lebenszeit des Rückgabetyps ist. Deshalb haben wir einen Fehler bekommen, als wir den Code in Listing 10-20 kompilieren wollten: Der Compiler hat die Lebenszeitelisionsregeln durchlaufen, konnte aber immer noch nicht alle Lebenszeiten der Referenzen in der Signatur ermitteln.

Da die dritte Regel eigentlich nur in Methodensignaturen gilt, werden wir im nächsten Abschnitt die Lebenszeiten in diesem Kontext betrachten, um zu verstehen, warum die dritte Regel bedeutet, dass wir Lebenszeiten in Methodensignaturen nicht so oft annotieren müssen.
