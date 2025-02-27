# Variablen und Daten, die mit Clone interagieren

Wenn wir tatsächlich die Heap-Daten des `String`s, nicht nur die Stapel-Daten, tief kopieren möchten, können wir eine häufige Methode namens `clone` verwenden. Wir werden die Methodensyntax im Kapitel 5 diskutieren, aber da Methoden ein häufiges Merkmal in vielen Programmiersprachen sind, haben Sie sie wahrscheinlich schon einmal gesehen.

Hier ist ein Beispiel für die Verwendung der `clone`-Methode:

```rust
let s1 = String::from("hello");
let s2 = s1.clone();

println!("s1 = {s1}, s2 = {s2}");
```

Dies funktioniert einwandfrei und erzeugt explizit das Verhalten, das in Abbildung 4-3 gezeigt wird, bei dem die Heap-Daten tatsächlich kopiert werden.

Wenn Sie einen Aufruf von `clone` sehen, wissen Sie, dass irgendein beliebiger Code ausgeführt wird und dass dieser Code möglicherweise aufwendig sein kann. Es ist ein visueller Hinweis darauf, dass etwas anderes geschieht.
