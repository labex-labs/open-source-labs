# Ein bisschen Refactoring

Im Moment haben die `if`- und `else`-Blöcke viel Wiederholung: Beide lesen Dateien und schreiben die Inhalte der Dateien in den Stream. Die einzigen Unterschiede sind die Statuszeile und der Dateiname. Lassen Sie uns den Code prägnanter machen, indem wir diese Unterschiede in separate `if`- und `else`-Zeilen ziehen, die die Werte der Statuszeile und des Dateinamens an Variablen zuweisen; wir können dann diese Variablen unbedingt im Code verwenden, um die Datei zu lesen und die Antwort zu schreiben. Listing 20-9 zeigt den resultierenden Code nach Ersetzung der großen `if`- und `else`-Blöcke.

Dateiname: `src/main.rs`

```rust
--snip--

fn handle_connection(mut stream: TcpStream) {
    --snip--

    let (status_line, filename) =
        if request_line == "GET / HTTP/1.1" {
            ("HTTP/1.1 200 OK", "hello.html")
        } else {
            ("HTTP/1.1 404 NOT FOUND", "404.html")
        };

    let contents = fs::read_to_string(filename).unwrap();
    let length = contents.len();

    let response = format!(
        "{status_line}\r\n\
         Content-Length: {length}\r\n\r\n\
         {contents}"
    );

    stream.write_all(response.as_bytes()).unwrap();
}
```

Listing 20-9: Refactoring der `if`- und `else`-Blöcke, um nur den Code zu enthalten, der zwischen den beiden Fällen unterschiedlich ist

Jetzt geben die `if`- und `else`-Blöcke nur die passenden Werte für die Statuszeile und den Dateinamen in einem Tupel zurück; wir verwenden dann die Dekonstruktion, um diese beiden Werte an `status_line` und `filename` zuzuweisen, indem wir ein Muster im `let`-Statement verwenden, wie in Kapitel 18 besprochen.

Der zuvor duplizierte Code befindet sich jetzt außerhalb der `if`- und `else`-Blöcke und verwendet die Variablen `status_line` und `filename`. Dies macht es einfacher, den Unterschied zwischen den beiden Fällen zu sehen, und es bedeutet, dass wir nur an einem Ort den Code aktualisieren müssen, wenn wir die Art und Weise ändern möchten, wie das Lesen der Datei und das Schreiben der Antwort funktioniert. Das Verhalten des Codes in Listing 20-9 wird das gleiche wie das in Listing 20-8 sein.

Super! Wir haben jetzt einen einfachen Webserver in ungefähr 40 Zeilen Rust-Code, der auf eine Anfrage mit einer Seite Inhalt antwortet und auf alle anderen Anfragen mit einer 404-Antwort.

Derzeit läuft unser Server in einem einzelnen Thread, was bedeutet, dass er nur eine Anfrage pro Zeitpunkt bedienen kann. Untersuchen wir, wie das ein Problem sein kann, indem wir einige langsame Anfragen simulieren. Dann werden wir es beheben, sodass unser Server mehrere Anfragen gleichzeitig verarbeiten kann.
