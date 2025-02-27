# Abhängigkeit von einem externen Paket in einem Arbeitsbereich

Beachten Sie, dass der Arbeitsbereich nur eine _Cargo.lock_-Datei auf der obersten Ebene hat, anstatt in jedem Kratenverzeichnis eine _Cargo.lock_ zu haben. Dadurch wird sichergestellt, dass alle Kraten die gleiche Version aller Abhängigkeiten verwenden. Wenn wir das `rand`-Paket zu den _adder/Cargo.toml_- und _add_one/Cargo.toml_-Dateien hinzufügen, wird Cargo beide auf eine Version von `rand` auflösen und das in der einen _Cargo.lock_ aufzeichnen. Dass alle Kraten im Arbeitsbereich die gleichen Abhängigkeiten verwenden, bedeutet, dass die Kraten immer miteinander kompatibel sein werden. Fügen wir das `rand`-Kraten zur `[dependencies]`-Sektion in der _add_one/Cargo.toml_-Datei hinzu, so dass wir das `rand`-Kraten im `add_one`-Kraten verwenden können:

Dateiname: `add_one/Cargo.toml`

```tomlrust
[dependencies]
rand = "0.8.5"
```

Wir können jetzt `use rand;` zur `add_one/src/lib.rs`-Datei hinzufügen, und das Erstellen des gesamten Arbeitsbereichs, indem wir `cargo build` im `add`-Verzeichnis ausführen, wird das `rand`-Kraten einbinden und kompilieren. Wir erhalten eine Warnung, weil wir nicht auf das `rand` verweisen, das wir in den Geltungsbereich gebracht haben:

```bash
$ cargo build
    Updating crates.io index
  Downloaded rand v0.8.5
   --snip--
   Compiling rand v0.8.5
   Compiling add_one v0.1.0 (file:///projects/add/add_one)
   Compiling adder v0.1.0 (file:///projects/add/adder)
    Finished dev [unoptimized + debuginfo] target(s) in 10.18s
```

Die oberste Ebene _Cargo.lock_ enthält jetzt Informationen über die Abhängigkeit von `add_one` von `rand`. Allerdings können wir `rand` auch dann nicht in anderen Kraten im Arbeitsbereich verwenden, es sei denn, wir fügen `rand` auch zu ihren `Cargo.toml`-Dateien hinzu. Beispielsweise erhalten wir einen Fehler, wenn wir `use rand;` zur `adder/src/main.rs`-Datei für das `adder`-Paket hinzufügen:

```bash
$ cargo build
   --snip--
   Compiling adder v0.1.0 (file:///projects/add/adder)
error[E0432]: unresolved import `rand`
 --> adder/src/main.rs:2:5
  |
2 | use rand;
  |     ^^^^ no external crate `rand`
```

Um das zu beheben, bearbeiten Sie die `Cargo.toml`-Datei für das `adder`-Paket und geben an, dass `rand` auch eine Abhängigkeit für es ist. Das Erstellen des `adder`-Pakets wird `rand` zur Liste der Abhängigkeiten von `adder` in _Cargo.lock_ hinzufügen, aber keine zusätzlichen Kopien von `rand` werden heruntergeladen. Cargo hat sichergestellt, dass jedes Kraten in jedem Paket im Arbeitsbereich, das das `rand`-Paket verwendet, die gleiche Version verwenden wird, spart uns Speicher und stellt sicher, dass die Kraten im Arbeitsbereich miteinander kompatibel sein werden.
