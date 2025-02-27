# Dokumentationskommentare als Tests

Das Hinzufügen von Codebeispielblöcken in Ihren Dokumentationskommentaren kann helfen, zu zeigen, wie Ihre Bibliothek verwendet werden kann, und dabei gibt es einen zusätzlichen Vorteil: Wenn Sie `cargo test` ausführen, werden die Codebeispiele in Ihrer Dokumentation als Tests ausgeführt! Nichts ist besser als Dokumentation mit Beispielen. Aber nichts ist schlimmer als Beispiele, die nicht funktionieren, weil der Code seit der Erstellung der Dokumentation geändert wurde. Wenn wir `cargo test` mit der Dokumentation der `add_one`-Funktion aus Listing 14-1 ausführen, werden wir einen Abschnitt in den Testergebnissen sehen, der wie folgt aussieht:

```rust
   Doc-tests my_crate

running 1 test
test src/lib.rs - add_one (line 5)... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0
filtered out; finished in 0.27s
```

Nun, wenn wir die Funktion oder das Beispiel ändern, sodass das `assert_eq!` im Beispiel in Panik gerät und wir `cargo test` erneut ausführen, werden wir sehen, dass die Dokutests erkennen, dass das Beispiel und der Code nicht mehr übereinstimmen!
