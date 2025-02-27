# Ein neuer Thread für jede Anforderung erzeugen

Zunächst wollen wir untersuchen, wie unser Code aussehen könnte, wenn er tatsächlich für jede Verbindung einen neuen Thread erstellt. Wie bereits erwähnt, ist dies nicht unsere endgültige Lösung aufgrund der Probleme, die mit der potenziellen Erzeugung einer unbegrenzten Anzahl von Threads verbunden sind, aber es ist ein Ausgangspunkt, um zunächst einen funktionierenden multi-threadigen Server zu erhalten. Dann werden wir den Threadpool als Verbesserung hinzufügen, und das Kontrastieren der beiden Lösungen wird einfacher sein.

Listing 20-11 zeigt die Änderungen, die an `main` vorgenommen werden müssen, um einen neuen Thread zu erzeugen, um jede Streamverbindung innerhalb der `for`-Schleife zu behandeln.

Dateiname: `src/main.rs`

```rust
fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();

        thread::spawn(|| {
            handle_connection(stream);
        });
    }
}
```

Listing 20-11: Ein neuer Thread für jeden Stream erzeugen

Wie Sie im Kapitel 16 gelernt haben, wird `thread::spawn` einen neuen Thread erstellen und dann den Code in der Closure im neuen Thread ausführen. Wenn Sie diesen Code ausführen und in Ihrem Browser _/sleep_ laden, und dann in zwei weiteren Browser-Tabs _/_, werden Sie tatsächlich sehen, dass die Anfragen an _/_ nicht auf das Ende von _/sleep_ warten müssen. Allerdings wird dies wie erwähnt letztendlich das System überlasten, da Sie neue Threads ohne jede Begrenzung erzeugen würden.
