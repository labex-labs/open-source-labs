# Wie man Tests schreibt

Tests sind Rust-Funktionen, die überprüfen, ob der nicht-testende Code auf die erwartete Weise funktioniert. Die Körper von Testfunktionen führen normalerweise diese drei Aktionen aus:

- Legen Sie alle erforderlichen Daten oder Zustände fest.
- Führen Sie den Code aus, den Sie testen möchten.
- Stellen Sie sicher, dass die Ergebnisse die erwarteten sind.

Schauen wir uns die Features von Rust an, die speziell für das Schreiben von Tests zur Ausführung dieser Aktionen zur Verfügung stehen, darunter das `test`-Attribut, einige Makros und das `should_panic`-Attribut.
