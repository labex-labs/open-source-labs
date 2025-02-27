# Vergleichen der Vermutung mit der Geheimzahl

Jetzt, wo wir Benutzereingaben und eine Zufallszahl haben, können wir sie vergleichen. Dieser Schritt wird in Listing 2-4 gezeigt. Beachten Sie, dass dieser Code noch nicht kompilieren wird, wie wir erklären werden.

Dateiname: `src/main.rs`

```rust
use rand::Rng;
1 use std::cmp::Ordering;
use std::io;

fn main() {
    --snip--

    println!("You guessed: {guess}");

  2 match guess.3 cmp(&secret_number) {
        Ordering::Less => println!("Too small!"),
        Ordering::Greater => println!("Too big!"),
        Ordering::Equal => println!("You win!"),
    }
}
```

Listing 2-4: Behandlung der möglichen Rückgabewerte beim Vergleichen von zwei Zahlen

Zuerst fügen wir eine weitere `use`-Anweisung hinzu \[1\], um einen Typ namens `std::cmp::Ordering` aus der Standardbibliothek in den Gültigkeitsbereich zu bringen. Der `Ordering`-Typ ist eine weitere Enumeration und hat die Varianten `Less`, `Greater` und `Equal`. Dies sind die drei möglichen Ergebnisse, wenn Sie zwei Werte vergleichen.

Dann fügen wir fünf neue Zeilen am Ende hinzu, die den `Ordering`-Typ verwenden. Die `cmp`-Methode \[3\] vergleicht zwei Werte und kann auf jedem Objekt aufgerufen werden, das verglichen werden kann. Sie nimmt eine Referenz auf das Objekt, mit dem Sie vergleichen möchten: hier wird `guess` mit `secret_number` verglichen. Dann gibt sie eine Variante der `Ordering`-Enumeration zurück, die wir mit der `use`-Anweisung in den Gültigkeitsbereich gebracht haben. Wir verwenden einen `match`-Ausdruck \[2\], um zu bestimmen, was als nächstes zu tun ist, basierend auf der Variante von `Ordering`, die von der `cmp`-Methode mit den Werten in `guess` und `secret_number` zurückgegeben wurde.

Ein `match`-Ausdruck besteht aus _Armen_. Ein Arm besteht aus einem _Muster_, gegen das verglichen wird, und dem Code, der ausgeführt werden soll, wenn der Wert, der an `match` übergeben wird, dem Muster des Arms entspricht. Rust nimmt den Wert, der an `match` übergeben wird, und durchsucht nacheinander jedes Arm-Muster. Muster und die `match`-Konstruktion sind leistungsstarke Rust-Features: sie ermöglichen es Ihnen, eine Vielzahl von Situationen auszudrücken, die Ihr Code möglicherweise auftauchen kann, und stellen sicher, dass Sie alle behandeln. Diese Features werden in Kapitel 6 und Kapitel 18 detailliert behandelt.

Lassen Sie uns ein Beispiel mit dem `match`-Ausdruck durchgehen, den wir hier verwenden. Nehmen wir an, dass der Benutzer 50 geraten hat und die zufällig generierte Geheimzahl diesmal 38 ist.

Wenn der Code 50 mit 38 vergleicht, wird die `cmp`-Methode `Ordering::Greater` zurückgeben, da 50 größer als 38 ist. Der `match`-Ausdruck erhält den Wert `Ordering::Greater` und beginnt, jedes Arm-Muster zu überprüfen. Er betrachtet das Muster des ersten Arms, `Ordering::Less`, und erkennt, dass der Wert `Ordering::Greater` nicht mit `Ordering::Less` übereinstimmt, daher ignoriert er den Code in diesem Arm und geht zum nächsten Arm. Das Muster des nächsten Arms ist `Ordering::Greater`, was tatsächlich mit `Ordering::Greater` übereinstimmt! Der zugehörige Code in diesem Arm wird ausgeführt und druckt `Too big!` auf dem Bildschirm. Der `match`-Ausdruck endet nach der ersten erfolgreichen Übereinstimmung, daher wird er in diesem Szenario den letzten Arm nicht betrachten.

Der Code in Listing 2-4 wird jedoch noch nicht kompilieren. Probieren wir es aus:

```bash
$ cargo build
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
error[E0308]: mismatched types
  --> src/main.rs:22:21
   |
22 |     match guess.cmp(&secret_number) {
   |                     ^^^^^^^^^^^^^^ expected struct `String`, found integer
   |
   = note: expected reference `&String`
              found reference `&{integer}`
```

Der Kern des Fehlers besagt, dass es _ungleiche Typen_ gibt. Rust hat ein starkes, statisches Typsystem. Allerdings hat es auch Typinferenz. Als wir `let mut guess = String::new()` geschrieben haben, konnte Rust schließen, dass `guess` ein `String` sein sollte, und hat uns nicht dazu gezwungen, den Typ zu schreiben. Die `secret_number` ist dagegen ein Zahlentyp. Einige der Zahlentypen in Rust können einen Wert zwischen 1 und 100 haben: `i32`, eine 32-Bit-Zahl; `u32`, eine unsigned 32-Bit-Zahl; `i64`, eine 64-Bit-Zahl; sowie andere. Wenn nichts anderes angegeben wird, nimmt Rust standardmäßig einen `i32`, was der Typ von `secret_number` ist, es sei denn, Sie geben an anderer Stelle Typinformationen an, die dazu führen würden, dass Rust einen anderen numerischen Typ schließt. Der Grund für den Fehler ist, dass Rust einen String und einen Zahlentyp nicht vergleichen kann.

Letztendlich möchten wir die `String`, die das Programm als Eingabe liest, in einen echten Zahlentyp umwandeln, damit wir sie numerisch mit der Geheimzahl vergleichen können. Wir tun dies, indem wir diese Zeile in den `main`-Funktionskörper einfügen:

Dateiname: `src/main.rs`

```rust
use std::io;
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    println!("The secret number is: {secret_number}");

    println!("Please input your guess.");

    let mut guess = String::new();

    io::stdin()
      .read_line(&mut guess)
      .expect("Failed to read line");

    let guess: u32 = guess
      .trim()
      .parse()
      .expect("Please type a number!");

    println!("You guessed: {guess}");

    match guess.cmp(&secret_number) {
        Ordering::Less => println!("Too small!"),
        Ordering::Greater => println!("Too big!"),
        Ordering::Equal => println!("You win!"),
    }
}
```

Wir erstellen eine Variable namens `guess`. Aber warte, hat das Programm nicht bereits eine Variable namens `guess`? Ja, aber es ist hilfreich, dass Rust uns erlaubt, den vorherigen Wert von `guess` mit einem neuen zu überschreiben. _Überschreiben_ ermöglicht es uns, den Variablennamen `guess` zu wiederverwenden, anstatt uns zu zwingen, zwei eindeutige Variablen zu erstellen, wie z. B. `guess_str` und `guess`. Wir werden dies im Kapitel 3 genauer behandeln, aber für jetzt wissen Sie, dass diese Funktion oft verwendet wird, wenn Sie einen Wert von einem Typ in einen anderen Typ umwandeln möchten.

Wir binden diese neue Variable an den Ausdruck `guess.trim().parse()`. Die `guess` im Ausdruck bezieht sich auf die ursprüngliche `guess`-Variable, die die Eingabe als String enthielt. Die `trim`-Methode auf einer `String`-Instanz entfernt alle Leerzeichen am Anfang und Ende, was wir tun müssen, um den String mit dem `u32` vergleichen zu können, der nur numerische Daten enthalten kann. Der Benutzer muss die Eingabetaste drücken, um `read_line` zu befriedigen und seine Vermutung einzugeben, was einem Zeilenumbruchzeichen am Ende der Zeichenfolge hinzufügt. Wenn der Benutzer beispielsweise `5` eingibt und die Eingabetaste drückt, sieht `guess` so aus: `5\n`. Das `\n` repräsentiert "Zeilenumbruch". (Auf Windows führt das Drücken der Eingabetaste zu einem Wagenrücklauf und einem Zeilenumbruch, `\r\n`.) Die `trim`-Methode entfernt `\n` oder `\r\n`, was nur `5` zurücklässt.

Die `parse`-Methode auf Strings wandelt einen String in einen anderen Typ um. Hier verwenden wir es, um von einem String zu einer Zahl zu wechseln. Wir müssen Rust den genauen Zahlentyp sagen, den wir möchten, indem wir `let guess: u32` verwenden. Das Doppelpunktzeichen (`:`) nach `guess` sagt Rust, dass wir den Typ der Variable annotieren werden. Rust hat einige integrierte Zahlentypen; der hier verwendete `u32` ist eine unsigned 32-Bit-Ganzzahl. Es ist eine gute Standardauswahl für eine kleine positive Zahl. Sie werden in Kapitel 3 über andere Zahlentypen lernen.

Zusätzlich bedeutet die `u32`-Annotation in diesem Beispielprogramm und der Vergleich mit `secret_number`, dass Rust schließen wird, dass `secret_number` ebenfalls ein `u32` sein sollte. Jetzt wird der Vergleich zwischen zwei Werten des gleichen Typs durchgeführt!

Die `parse`-Methode funktioniert nur auf Zeichen, die logisch in Zahlen umgewandelt werden können, und kann daher leicht zu Fehlern führen. Wenn beispielsweise die Zeichenfolge `A`👍`%` enthielt, gäbe es keine Möglichkeit, das in eine Zahl umzuwandeln. Da es fehlschlagen kann, gibt die `parse`-Methode einen `Result`-Typ zurück, ähnlich wie die `read_line`-Methode (siehe zuvor in "Behandlung von potenziellen Fehlern mit Result"). Wir werden dieses `Result` auf die gleiche Weise behandeln, indem wir die `expect`-Methode erneut verwenden. Wenn `parse` ein `Err`-`Result`-Variant zurückgibt, weil es keine Zahl aus der Zeichenfolge erstellen konnte, wird der `expect`-Aufruf das Spiel abbrechen und die Nachricht ausgeben, die wir ihm geben. Wenn `parse` die Zeichenfolge erfolgreich in eine Zahl umwandeln kann, wird es das `Ok`-Variant von `Result` zurückgeben, und `expect` wird die Zahl zurückgeben, die wir aus dem `Ok`-Wert wollen.

Lassen Sie uns jetzt das Programm ausführen:

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 0.43s
     Running `target/debug/guessing_game`
Guess the number!
The secret number is: 58
Please input your guess.
  76
You guessed: 76
Too big!
```

Super! Auch wenn Leerzeichen vor der Vermutung hinzugefügt wurden, hat das Programm immer noch erkannt, dass der Benutzer 76 geraten hat. Führen Sie das Programm ein paar Mal aus, um das unterschiedliche Verhalten mit verschiedenen Arten von Eingaben zu überprüfen: erraten Sie die Zahl richtig, erraten Sie eine zu hohe Zahl und erraten Sie eine zu niedrige Zahl.

Wir haben jetzt den Großteil des Spiels funktional, aber der Benutzer kann nur eine Vermutung machen. Ändern wir das, indem wir eine Schleife hinzufügen!
