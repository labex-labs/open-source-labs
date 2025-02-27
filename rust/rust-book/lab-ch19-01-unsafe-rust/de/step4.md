# Aufrufen einer unsicheren Funktion oder Methode

Die zweite Art von Operation, die du in einem unsafe Block ausführen kannst, ist das Aufrufen von unsicheren Funktionen. Unsichere Funktionen und Methoden sehen genau wie reguläre Funktionen und Methoden aus, aber sie haben ein zusätzliches `unsafe` vor der restlichen Definition. Das Schlüsselwort `unsafe` in diesem Kontext zeigt an, dass die Funktion Anforderungen hat, die wir einhalten müssen, wenn wir diese Funktion aufrufen, weil Rust nicht gewährleisten kann, dass wir diese Anforderungen erfüllt haben. Indem wir eine unsichere Funktion innerhalb eines `unsafe` Blocks aufrufen, sagen wir Rust, dass wir die Dokumentation dieser Funktion gelesen haben und wir uns für die Einhaltung der Verträge der Funktion verantworten.

Hier ist eine unsichere Funktion namens `dangerous`, die im Wesentlichen nichts tut:

    unsafe fn dangerous() {}

    unsafe {
        dangerous();
    }

Wir müssen die `dangerous` Funktion innerhalb eines separaten `unsafe` Blocks aufrufen. Wenn wir versuchen, `dangerous` ohne den `unsafe` Block aufzurufen, erhalten wir einen Fehler:

```bash
error[E0133]: call to unsafe function is unsafe and requires
unsafe function or block
 --> src/main.rs:4:5
  |
4 |     dangerous();
  |     ^^^^^^^^^^^ call to unsafe function
  |
  = note: consult the function's documentation for information on
how to avoid undefined behavior
```

Mit dem `unsafe` Block sagen wir Rust, dass wir die Dokumentation der Funktion gelesen haben, wir verstehen, wie wir sie richtig verwenden, und wir haben überprüft, dass wir die Verträge der Funktion erfüllen.

Die Körper von unsicheren Funktionen sind effektiv `unsafe` Blöcke, so dass wir keine zusätzlichen `unsafe` Blöcke hinzufügen müssen, um andere unsichere Operationen innerhalb einer unsicheren Funktion durchzuführen.
