# Auf das TCP-Verbindung hören

Unser Webserver muss auf eine TCP-Verbindung hören, daher ist das der erste Teil, an dem wir arbeiten werden. Die Standardbibliothek bietet ein `std::net`-Modul, das uns dies ermöglicht. Lassen Sie uns ein neues Projekt auf die übliche Weise erstellen:

```bash
$ cargo new hello
     Created binary (application) `hello` project
$ cd hello
```

Nun geben Sie den Code in Listing 20-1 in `src/main.rs` ein, um zu beginnen. Dieser Code wird an der lokalen Adresse `127.0.0.1:7878` auf eingehende TCP-Streams hören. Wenn er einen eingehenden Stream erhält, wird er `Connection established!` ausgeben.

Dateiname: `src/main.rs`

```rust
use std::net::TcpListener;

fn main() {
  1 let listener = TcpListener::bind("127.0.0.1:7878").unwrap();

  2 for stream in listener.incoming() {
      3 let stream = stream.unwrap();

      4 println!("Connection established!");
    }
}
```

Listing 20-1: Lauschen auf eingehende Ströme und Ausgeben einer Nachricht, wenn wir einen Stream erhalten

Mit `TcpListener` können wir auf TCP-Verbindungen an der Adresse `127.0.0.1:7878` hören \[1\]. In der Adresse ist der Teil vor dem Doppelpunkt eine IP-Adresse, die Ihren Computer repräsentiert (dies ist auf jedem Computer gleich und repräsentiert nicht speziell den Computer der Autoren), und `7878` ist der Port. Wir haben diesen Port aus zwei Gründen gewählt: Normalerweise wird HTTP nicht auf diesem Port akzeptiert, daher ist es unwahrscheinlich, dass unser Server mit einem anderen Webserver auf Ihrem Computer in Konflikt tritt, und 7878 ist _rust_ auf einem Telefon getippt.

Die `bind`-Funktion in diesem Szenario funktioniert wie die `new`-Funktion, in dem sie eine neue `TcpListener`-Instanz zurückgibt. Die Funktion heißt `bind`, weil im Netzwerkverbindung auf einen Port zu hören als "sich an einen Port binden" bekannt ist.

Die `bind`-Funktion gibt ein `Result<T, E>` zurück, was darauf hinweist, dass das Binden fehlschlagen kann. Beispielsweise erfordert das Verbinden mit Port 80 Administratorrechte (Nicht-Administratoren können nur auf Ports höher als 1023 hören), daher würde das Binden nicht funktionieren, wenn wir versuchten, uns an Port 80 zu verbinden, ohne Administrator zu sein. Das Binden würde auch nicht funktionieren, wenn wir zwei Instanzen unseres Programms ausführten und daher zwei Programme auf den gleichen Port hätten. Da wir nur ein einfachen Server für Lernzwecke schreiben, werden wir uns nicht um das Handling dieser Arten von Fehlern kümmern; stattdessen verwenden wir `unwrap`, um das Programm zu beenden, wenn Fehler auftreten.

Die `incoming`-Methode auf `TcpListener` gibt einen Iterator zurück, der uns eine Sequenz von Strömen gibt \[2\] (genauer gesagt Ströme vom Typ `TcpStream`). Ein einzelner _Stream_ repräsentiert eine offene Verbindung zwischen dem Client und dem Server. Eine _Verbindung_ ist der Name für den gesamten Anforderungs- und Antwortprozess, in dem ein Client sich an den Server verbindet, der Server eine Antwort generiert und der Server die Verbindung schließt. Daher werden wir aus dem `TcpStream` lesen, um zu sehen, was der Client gesendet hat, und dann unsere Antwort an den Stream schreiben, um Daten zurück an den Client zu senden. Insgesamt wird diese `for`-Schleife jede Verbindung nacheinander verarbeiten und eine Reihe von Strömen für uns erzeugen, die wir verarbeiten müssen.

Zur Zeit besteht unsere Behandlung des Streams darin, `unwrap` aufzurufen, um unser Programm zu beenden, wenn der Stream Fehler hat \[3\]; wenn es keine Fehler gibt, druckt das Programm eine Nachricht \[4\]. Wir werden im nächsten Listing für den Erfolgfall weitere Funktionalität hinzufügen. Der Grund, warum wir Fehler von der `incoming`-Methode erhalten können, wenn ein Client sich an den Server verbindet, ist, dass wir tatsächlich nicht über Verbindungen iterieren. Stattdessen iterieren wir über _Verbindungsversuche_. Die Verbindung kann aus einer Vielzahl von Gründen nicht erfolgreich sein, viele davon sind Betriebssystem-spezifisch. Beispielsweise haben viele Betriebssysteme eine Begrenzung für die Anzahl der gleichzeitig offenen Verbindungen, die sie unterstützen können; neue Verbindungsversuche über diese Anzahl hinaus werden zu einem Fehler führen, bis einige der offenen Verbindungen geschlossen werden.

Lassen Sie uns versuchen, diesen Code auszuführen! Rufen Sie in der Konsole `cargo run` auf und laden Sie dann _127.0.0.1:7878_ in einem Webbrowser. Der Browser sollte eine Fehlermeldung wie "Connection reset" anzeigen, da der Server derzeit keine Daten zurücksendet. Aber wenn Sie sich die Konsole ansehen, sollten Sie mehrere Nachrichten sehen, die gedruckt wurden, als der Browser sich an den Server verbunden hat!

         Running `target/debug/hello`
    Connection established!
    Connection established!
    Connection established!

Manchmal werden Sie für einen Browseranforderung mehrere Nachrichten gedruckt; Der Grund kann sein, dass der Browser eine Anforderung für die Seite sowie eine Anforderung für andere Ressourcen macht, wie das _favicon.ico_ -Symbol, das im Browser-Tab erscheint.

Es könnte auch sein, dass der Browser versucht, sich mehrmals an den Server zu verbinden, weil der Server keine Daten zurücksendet. Wenn `stream` außerhalb des Gültigkeitsbereichs geht und am Ende der Schleife gelöscht wird, wird die Verbindung als Teil der `drop`-Implementierung geschlossen. Browser behandeln manchmal geschlossene Verbindungen, indem sie versuchen, da das Problem möglicherweise vorübergehend ist. Der wichtigste Faktor ist, dass wir erfolgreich einen Zugang zu einer TCP-Verbindung erhalten haben!

Denken Sie daran, das Programm mit Strg+C zu beenden, wenn Sie mit der Ausführung einer bestimmten Version des Codes fertig sind. Starten Sie dann das Programm erneut, indem Sie nach jeder Codeänderung den Befehl `cargo run` aufrufen, um sicherzustellen, dass Sie den neuesten Code ausführen.
