# Aktualisierung einer Kiste, um eine neue Version zu erhalten

Wenn Sie tatsächlich eine Kiste aktualisieren möchten, bietet Cargo den Befehl `update`, der die _Cargo.lock_-Datei ignorieren und alle neuesten Versionen ermitteln wird, die Ihren Spezifikationen in `Cargo.toml` entsprechen. Cargo wird dann diese Versionen in die _Cargo.lock_-Datei schreiben. Andernfalls wird Cargo standardmäßig nur nach Versionen suchen, die größer als 0.8.5 und kleiner als 0.9.0 sind. Wenn die `rand`-Kiste die beiden neuen Versionen 0.8.6 und 0.9.0 veröffentlicht hat, würden Sie Folgendes sehen, wenn Sie `cargo update` ausführen:

```bash
$ cargo update
Updating crates.io index
Updating rand v0.8.5 - > v0.8.6
```

Cargo ignoriert die 0.9.0-Version. An diesem Punkt würden Sie auch eine Änderung in Ihrer _Cargo.lock_-Datei bemerken, die angibt, dass die Version der `rand`-Kiste, die Sie jetzt verwenden, 0.8.6 ist. Um die `rand`-Version 0.9.0 oder jede Version in der 0.9._x_-Reihe zu verwenden, müssten Sie die `Cargo.toml`-Datei so aktualisieren, dass sie wie folgt aussieht:

```rust
[dependencies]
rand = "0.9.0"
```

Die nächste Mal, wenn Sie `cargo build` ausführen, wird Cargo das Registrierungsverzeichnis der verfügbaren Kisten aktualisieren und Ihre `rand`-Anforderungen gemäß der neuen Version, die Sie angegeben haben, neu bewerten.

Es gibt noch viel mehr zu sagen über Cargo und seine Ökosystem, über das wir im Kapitel 14 sprechen werden, aber für jetzt ist das alles, was Sie wissen müssen. Cargo macht es sehr einfach, Bibliotheken zu wiederverwenden, sodass Rustaceans kleinere Projekte schreiben können, die aus einer Anzahl von Paketen zusammengesetzt sind.
