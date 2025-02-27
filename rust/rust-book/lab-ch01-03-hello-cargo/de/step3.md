# Ein Cargo-Projekt bauen und ausführen

Schauen wir uns nun an, was sich ändert, wenn wir das "Hello, world!"-Programm mit Cargo bauen und ausführen! Aus Ihrem `hello_cargo`-Verzeichnis aus führen Sie den folgenden Befehl aus, um Ihr Projekt zu bauen:

```bash
$ cargo build
   Compiling hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 2.85 secs
```

Dieser Befehl erstellt eine ausführbare Datei in `target/debug/hello_cargo` statt im aktuellen Verzeichnis. Da der Standardaufbau ein Debug-Aufbau ist, legt Cargo die Binärdatei in einem Verzeichnis namens `debug` ab. Sie können die ausführbare Datei mit diesem Befehl ausführen:

```bash
$./target/debug/hello_cargo
Hello, world!
```

Wenn alles funktioniert, sollte `Hello, world!` in der Konsole ausgegeben werden. Wenn Sie `cargo build` zum ersten Mal ausführen, erstellt Cargo auch eine neue Datei im obersten Verzeichnis: _Cargo.lock_. Diese Datei verfolgt die genauen Versionen der Abhängigkeiten in Ihrem Projekt. Dieses Projekt hat keine Abhängigkeiten, daher ist die Datei etwas spärlich. Sie müssen diese Datei niemals manuell ändern; Cargo verwaltet ihren Inhalt für Sie.

Wir haben gerade ein Projekt mit `cargo build` gebaut und es mit `./target/debug/hello_cargo` ausgeführt, aber wir können auch `cargo run` verwenden, um den Code zu kompilieren und dann die resultierende ausführbare Datei in einem einzigen Befehl auszuführen:

```bash
$ cargo run
    Finished dev [unoptimized + debuginfo] target(s) in 0.0 secs
     Running `target/debug/hello_cargo`
Hello, world!
```

Das Verwenden von `cargo run` ist bequemer als das Erinnern, `cargo build` auszuführen und dann den gesamten Pfad zur Binärdatei zu verwenden, daher verwenden die meisten Entwickler `cargo run`.

Beachten Sie, dass wir diesmal keine Ausgabe gesehen haben, die angibt, dass Cargo `hello_cargo` kompiliert. Cargo hat erkannt, dass die Dateien nicht geändert wurden, daher hat es nicht neu gebaut, sondern nur die Binärdatei ausgeführt. Wenn Sie Ihren Quellcode geändert hätten, hätte Cargo das Projekt vor der Ausführung neu gebaut, und Sie hätten diese Ausgabe gesehen:

```bash
$ cargo run
   Compiling hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 0.33 secs
     Running `target/debug/hello_cargo`
Hello, world!
```

Cargo bietet auch einen Befehl namens `cargo check`. Dieser Befehl überprüft Ihren Code schnell, um sicherzustellen, dass er kompiliert, erzeugt jedoch keine ausführbare Datei:

```bash
$ cargo check
   Checking hello_cargo v0.1.0 (file:///projects/hello_cargo)
    Finished dev [unoptimized + debuginfo] target(s) in 0.32 secs
```

Warum möchten Sie keine ausführbare Datei haben? Oft ist `cargo check` viel schneller als `cargo build`, weil es den Schritt der Erzeugung einer ausführbaren Datei überspringt. Wenn Sie Ihre Arbeit ständig während des Schreibens des Codes überprüfen, wird das Verwenden von `cargo check` den Prozess beschleunigen, Ihnen mitzuteilen, ob Ihr Projekt weiterhin kompiliert! Daher führen viele Rust-Entwickler periodisch `cargo check` aus, wenn sie ihren Code schreiben, um sicherzustellen, dass er kompiliert. Dann führen sie `cargo build` aus, wenn sie bereit sind, die ausführbare Datei zu verwenden.

Fassen wir zusammen, was wir bisher über Cargo gelernt haben:

- Wir können ein Projekt mit `cargo new` erstellen.
- Wir können ein Projekt mit `cargo build` bauen.
- Wir können ein Projekt in einem Schritt bauen und ausführen mit `cargo run`.
- Wir können ein Projekt bauen, ohne eine Binärdatei zu erzeugen, um Fehler zu überprüfen, mit `cargo check`.
- Anstatt das Ergebnis des Builds im selben Verzeichnis wie unseren Code zu speichern, legt Cargo es im Verzeichnis `target/debug` ab.

Ein zusätzlicher Vorteil der Verwendung von Cargo ist, dass die Befehle unabhängig von dem Betriebssystem, auf dem Sie arbeiten, gleich sind. Daher werden wir ab diesem Punkt keine spezifischen Anweisungen mehr für Linux und macOS im Vergleich zu Windows geben.
