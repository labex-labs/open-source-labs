# Verkettung mit dem +-Operator oder der format!-Makro

Oft möchten Sie zwei vorhandene Strings kombinieren. Ein Möglichkeit dazu ist, den `+`-Operator zu verwenden, wie in Listing 8-18 gezeigt.

```rust
let s1 = String::from("Hello, ");
let s2 = String::from("world!");
let s3 = s1 + &s2; // beachten Sie, dass s1 hier verschoben wurde und nicht mehr verwendet werden kann
```

Listing 8-18: Verwenden des `+`-Operators, um zwei `String`-Werte zu einer neuen `String`-Wert zu kombinieren

Der String `s3` wird den Wert `Hello, world!` enthalten. Der Grund, warum `s1` nach der Addition nicht mehr gültig ist, und der Grund, warum wir auf `s2` eine Referenz verwendet haben, hat mit der Signatur der Methode zu tun, die aufgerufen wird, wenn wir den `+`-Operator verwenden. Der `+`-Operator verwendet die `add`-Methode, deren Signatur ungefähr so aussieht:

```rust
fn add(self, s: &str) -> String {
```

In der Standardbibliothek werden Sie `add` mit Generics und assoziierten Typen definiert sehen. Hier haben wir konkrete Typen eingesetzt, was passiert, wenn wir diese Methode mit `String`-Werten aufrufen. Wir werden Generics im Kapitel 10 besprechen. Diese Signatur gibt uns die Hinweise, die wir benötigen, um die komplizierten Teile des `+`-Operators zu verstehen.

Zunächst hat `s2` ein `&`, was bedeutet, dass wir eine _Referenz_ des zweiten Strings zum ersten String hinzufügen. Dies liegt an dem `s`-Parameter in der `add`-Funktion: Wir können nur einen `&str` zu einem `String` hinzufügen; wir können zwei `String`-Werte nicht zusammenfügen. Aber warte mal - der Typ von `&s2` ist `&String`, nicht `&str`, wie im zweiten Parameter von `add` angegeben. Warum kompiliert also Listing 8-18?

Der Grund, warum wir `&s2` im Aufruf von `add` verwenden können, ist, dass der Compiler die `&String`-Argument in einen `&str` _umwandeln_ kann. Wenn wir die `add`-Methode aufrufen, verwendet Rust eine _Deref-Umwandlung_, die hier `&s2` in `&s2[..]` umwandelt. Wir werden Deref-Umwandlungen im Kapitel 15 im Detail besprechen. Da `add` die Eigentumsgewalt über den `s`-Parameter nicht übernimmt, wird `s2` nach dieser Operation immer noch ein gültiger `String` sein.

Zweitens können wir in der Signatur sehen, dass `add` die Eigentumsgewalt über `self` übernimmt, weil `self` kein `&` hat. Dies bedeutet, dass `s1` in Listing 8-18 in den `add`-Aufruf verschoben wird und danach nicht mehr gültig ist. Also, obwohl `let s3 = s1 + &s2;` so aussieht, als würde es beide Strings kopieren und einen neuen erstellen, nimmt dieser Ausdruck tatsächlich die Eigentumsgewalt über `s1`, fügt eine Kopie des Inhalts von `s2` hinzu und gibt dann die Eigentumsgewalt über das Ergebnis zurück. Mit anderen Worten, es sieht so aus, als würde es viele Kopien machen, aber es tut es nicht; die Implementierung ist effizienter als das Kopieren.

Wenn wir mehrere Strings konkatenieren müssen, wird das Verhalten des `+`-Operators unhandlich:

```rust
let s1 = String::from("tic");
let s2 = String::from("tac");
let s3 = String::from("toe");

let s = s1 + "-" + &s2 + "-" + &s3;
```

An diesem Punkt wird `s` `tic-tac-toe` sein. Mit all den `+`- und `"-"`-Zeichen ist es schwierig, zu sehen, was passiert. Um Strings auf komplexere Weise zu kombinieren, können wir stattdessen das `format!`-Makro verwenden:

```rust
let s1 = String::from("tic");
let s2 = String::from("tac");
let s3 = String::from("toe");

let s = format!("{s1}-{s2}-{s3}");
```

Dieser Code setzt auch `s` auf `tic-tac-toe`. Das `format!`-Makro funktioniert wie `println!`, aber anstatt die Ausgabe auf den Bildschirm zu drucken, gibt es einen `String` mit dem Inhalt zurück. Die Version des Codes mit `format!` ist viel lesbarer, und der von dem `format!`-Makro generierte Code verwendet Referenzen, sodass dieser Aufruf keine der Parameter in die Eigentumsgewalt nimmt.
