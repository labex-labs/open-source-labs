# Durchlaufen einer Sammlung mit for

Sie können die `while`-Konstruktion verwenden, um über die Elemente einer Sammlung wie eines Arrays zu iterieren. Beispielsweise druckt die Schleife in Listing 3-4 jedes Element im Array `a`.

Dateiname: `src/main.rs`

```rust
fn main() {
    let a = [10, 20, 30, 40, 50];
    let mut index = 0;

    while index < 5 {
        println!("the value is: {}", a[index]);

        index += 1;
    }
}
```

Listing 3-4: Iterieren durch jedes Element einer Sammlung mit einer `while`-Schleife

Hier zählt der Code durch die Elemente im Array aufwärts. Es startet bei Index `0` und iteriert dann, bis es den letzten Index im Array erreicht hat (d.h., wenn `index < 5` nicht mehr `true` ist). Wenn Sie diesen Code ausführen, werden alle Elemente des Arrays gedruckt:

```bash
$ cargo run
   Compiling loops v0.1.0 (file:///projects/loops)
    Finished dev [unoptimized + debuginfo] target(s) in 0.32s
     Running `target/debug/loops`
the value is: 10
the value is: 20
the value is: 30
the value is: 40
the value is: 50
```

Alle fünf Arraywerte erscheinen im Terminal, wie erwartet. Auch wenn `index` irgendwann den Wert `5` erreichen wird, stoppt die Schleife vor dem Versuch, einen sechsten Wert aus dem Array abzurufen.

Dieser Ansatz ist jedoch fehleranfällig; wir könnten das Programm zum Absturz bringen, wenn der Indexwert oder die Prüfbedingung falsch ist. Beispielsweise würde der Code abstürzen, wenn Sie die Definition des `a`-Arrays geändert hätten, um nur vier Elemente zu haben, aber vergessen hätten, die Bedingung auf `while index < 4` zu aktualisieren. Es ist auch langsam, weil der Compiler Laufzeitcode hinzufügt, um die bedingte Prüfung durchzuführen, ob der Index innerhalb der Grenzen des Arrays liegt, bei jeder Iteration durch die Schleife.

Als kompaktere Alternative können Sie eine `for`-Schleife verwenden und für jedes Element in einer Sammlung einige Code ausführen. Eine `for`-Schleife sieht wie der Code in Listing 3-5 aus.

Dateiname: `src/main.rs`

```rust
fn main() {
    let a = [10, 20, 30, 40, 50];

    for element in a {
        println!("the value is: {element}");
    }
}
```

Listing 3-5: Iterieren durch jedes Element einer Sammlung mit einer `for`-Schleife

Wenn wir diesen Code ausführen, werden wir die gleichen Ausgabe wie in Listing 3-4 sehen. Wichtiger ist, dass wir jetzt die Sicherheit des Codes erhöht haben und die Möglichkeit von Fehlern eliminiert haben, die möglicherweise durch das Überschreiten des Arrays oder das Nichtreichen des Endes und das Überspringen einiger Elemente entstehen könnten.

Mit der `for`-Schleife müssten Sie keine anderen Codeänderungen vornehmen, wenn Sie die Anzahl der Werte im Array ändern, wie Sie es mit der Methode in Listing 3-4 tun müssten.

Die Sicherheit und Kürze von `for`-Schleifen machen sie zu der am häufigsten verwendeten Schleifenkonstruktion in Rust. Auch in Situationen, in denen Sie einen bestimmten Code eine bestimmte Anzahl von Malen ausführen möchten, wie im Countdown-Beispiel, das in Listing 3-3 eine `while`-Schleife verwendete, würden die meisten Rust-Entwickler eine `for`-Schleife verwenden. Die Vorgehensweise dazu wäre, eine `Range` zu verwenden, die von der Standardbibliothek bereitgestellt wird und alle Zahlen in aufsteigender Reihenfolge von einer Zahl bis zu einer anderen Zahl generiert.

So würde der Countdown aussehen, wenn Sie eine `for`-Schleife und eine weitere Methode verwenden, die wir noch nicht besprochen haben, `rev`, um die Reihenfolge umzukehren:

Dateiname: `src/main.rs`

```rust
fn main() {
    for number in (1..4).rev() {
        println!("{number}!");
    }
    println!("LIFTOFF!!!");
}
```

Dieser Code ist ein bisschen hübscher, oder?
