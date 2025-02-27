# Aufbau eines Rust-Programms

Lassen Sie uns dieses "Hello, world!"-Programm im Detail überprüfen. Hier ist der erste Teil des Puzzles:

```rust
fn main() {

}
```

Diese Zeilen definieren eine Funktion namens `main`. Die `main`-Funktion ist speziell: Sie ist immer der erste Code, der in jedem ausführbaren Rust-Programm ausgeführt wird. Hier deklariert die erste Zeile eine Funktion namens `main`, die keine Parameter hat und nichts zurückgibt. Wenn es Parameter gäbe, würden sie innerhalb der Klammern `()` stehen.

Der Funktionskörper ist in `{}` eingeschlossen. Rust erfordert geschweifte Klammern um alle Funktionskörper. Es ist guter Stil, die öffnende geschweifte Klammer auf derselben Zeile wie die Funktionsdeklaration zu platzieren, mit einem Leerzeichen dazwischen.

> Hinweis: Wenn Sie einen standardisierten Stil in Rust-Projekten beibehalten möchten, können Sie ein automatisiertes Formatierungstool namens `rustfmt` verwenden, um Ihren Code in einem bestimmten Stil zu formatieren (mehr über `rustfmt` in Anhang D). Das Rust-Team hat dieses Tool wie `rustc` mit der standardmäßigen Rust-Verteilung mitgeliefert, so dass es bereits auf Ihrem Computer installiert sein sollte!

Der Körper der `main`-Funktion enthält folgenden Code:

```rust
    println!("Hello, world!");
```

Diese Zeile erledigt alle Arbeiten in diesem kleinen Programm: Sie druckt Text auf dem Bildschirm. Es gibt hier vier wichtige Details zu beachten.

Zunächst ist der Rust-Stil, mit vier Leerzeichen einzurücken, nicht mit einem Tabulator.

Zweitens ruft `println!` eine Rust-Makro auf. Wenn es stattdessen eine Funktion aufgerufen hätte, würde es als `println` (ohne das `!`) eingegeben werden. Wir werden Rust-Makros im Kapitel 19 im Detail diskutieren. Für jetzt müssen Sie nur wissen, dass das Verwenden eines `!` bedeutet, dass Sie ein Makro statt einer normalen Funktion aufrufen und dass Makros nicht immer den gleichen Regeln wie Funktionen folgen.

Drittens sehen Sie die Zeichenfolge `"Hello, world!"`. Wir übergeben diese Zeichenfolge als Argument an `println!`, und die Zeichenfolge wird auf dem Bildschirm gedruckt.

Viertens beenden wir die Zeile mit einem Semikolon (`;`), was angibt, dass dieser Ausdruck beendet ist und der nächste beginnen kann. Die meisten Zeilen von Rust-Code enden mit einem Semikolon.
