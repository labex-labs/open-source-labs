# Das Schreiben einer Antwort

Wir werden die Implementierung von Datenübertragung als Antwort auf eine Clientanfrage vornehmen. Antworten haben das folgende Format:

    HTTP-Version Status-Code Grundtext CRLF
    Header CRLF
    Nachrichtenkörper

Die erste Zeile ist eine _Statuszeile_, die die verwendete HTTP-Version in der Antwort, einen numerischen Statuscode, der das Ergebnis der Anfrage zusammenfasst, und einen Grundtext enthält, der eine textliche Beschreibung des Statuscodes liefert. Nach der CRLF-Sequenz folgen beliebige Header, eine weitere CRLF-Sequenz und der Körper der Antwort.

Hier ist ein Beispiel für eine Antwort, die HTTP-Version 1.1 verwendet, einen Statuscode von 200, einen OK-Grundtext, keine Header und keinen Körper hat:

```rust
HTTP/1.1 200 OK\r\n\r\n
```

Der Statuscode 200 ist die standardmäßige Erfolgsantwort. Der Text ist eine winzige erfolgreiche HTTP-Antwort. Schreiben wir dies in den Stream als Antwort auf eine erfolgreiche Anfrage! Entfernen Sie aus der `handle_connection`-Funktion die `println!`, die die Anfragedaten ausgab, und ersetzen Sie sie durch den Code in Listing 20-3.

Dateiname: `src/main.rs`

```rust
fn handle_connection(mut stream: TcpStream) {
    let buf_reader = BufReader::new(&mut stream);
    let http_request: Vec<_> = buf_reader
     .lines()
     .map(|result| result.unwrap())
     .take_while(|line|!line.is_empty())
     .collect();

  1 let response = "HTTP/1.1 200 OK\r\n\r\n";

  2 stream.write_all(response.3 as_bytes()).unwrap();
}
```

Listing 20-3: Schreiben einer winzigen erfolgreichen HTTP-Antwort in den Stream

Die erste neue Zeile definiert die `response`-Variable, die die Daten der Erfolgsnachricht enthält \[1\]. Dann rufen wir `as_bytes` auf unserer `response` auf, um die Zeichenfolge-Daten in Bytes umzuwandeln \[3\]. Die `write_all`-Methode auf `stream` nimmt ein `&[u8]` und sendet diese Bytes direkt über die Verbindung \[2\]. Da die `write_all`-Operation fehlschlagen kann, verwenden wir wie zuvor `unwrap` bei jedem Fehlerergebnis. Wiederholen Sie, in einer echten Anwendung würden Sie hier die Fehlerbehandlung hinzufügen.

Mit diesen Änderungen führen wir unseren Code aus und stellen eine Anfrage. Wir drucken keine Daten mehr in die Konsole, daher werden wir keine Ausgabe sehen, außer der Ausgabe von Cargo. Wenn Sie _127.0.0.1:7878_ in einem Webbrowser laden, sollten Sie eine leere Seite statt eines Fehlers erhalten. Sie haben gerade manuell die Empfang einer HTTP-Anfrage und das Senden einer Antwort implementiert!
