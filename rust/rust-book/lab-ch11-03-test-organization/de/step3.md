# Das Tests-Modul und #\[cfg(test)\]

Die Annotation `#[cfg(test)]` auf dem `tests`-Modul sagt Rust, den Testcode nur zu kompilieren und auszuführen, wenn du `cargo test` ausführst, nicht wenn du `cargo build` ausführst. Dies spart Kompilierzeit, wenn du nur die Bibliothek bauen möchtest, und spart Platz im resultierenden kompilierten Artefakt, da die Tests nicht enthalten sind. Du wirst sehen, dass, weil Integrations-Tests in einem anderen Verzeichnis liegen, sie die `#[cfg(test)]`-Annotation nicht benötigen. Allerdings, weil Einheitstests in den gleichen Dateien wie der Code liegen, wirst du `#[cfg(test)]` verwenden, um anzugeben, dass sie nicht im kompilierten Ergebnis enthalten sein sollen.

Denke daran, dass Cargo uns diesen Code generiert hat, als wir das neue `adder`-Projekt im ersten Abschnitt dieses Kapitels erstellt haben:

Dateiname: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
}
```

Dieser Code ist das automatisch generierte `tests`-Modul. Das Attribut `cfg` steht für _Konfiguration_ und sagt Rust, dass der folgende Codeabschnitt nur unter einer bestimmten Konfigurationseingabe enthalten sein soll. In diesem Fall ist die Konfigurationseingabe `test`, die von Rust für das Kompilieren und Ausführen von Tests bereitgestellt wird. Durch die Verwendung des `cfg`-Attributs kompiliert Cargo unseren Testcode nur, wenn wir die Tests aktiv mit `cargo test` ausführen. Dies umfasst alle Hilfsfunktionen, die möglicherweise innerhalb dieses Moduls sind, zusätzlich zu den Funktionen, die mit `#[test]` annotiert sind.
