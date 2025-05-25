# Tests parallel oder nacheinander ausführen

Wenn du mehrere Tests ausführst, werden diese standardmäßig parallel mithilfe von Threads ausgeführt, was bedeutet, dass sie schneller abgeschlossen werden und du schneller Feedback erhältst. Da die Tests gleichzeitig ausgeführt werden, musst du 确保，dass deine Tests nicht voneinander abhängen oder von einem gemeinsamen Zustand abhängen, einschließlich einer gemeinsamen Umgebung, wie dem aktuellen Arbeitsverzeichnis oder Umgebungsvariablen.

Nehmen wir beispielsweise an, dass jeder deiner Tests einige Code ausführt, der eine Datei namens _test-output.txt_ auf der Festplatte erstellt und einige Daten in diese Datei schreibt. Dann liest jeder Test die Daten in dieser Datei und stellt sicher, dass die Datei einen bestimmten Wert enthält, der in jedem Test unterschiedlich ist. Da die Tests gleichzeitig ausgeführt werden, kann ein Test die Datei in der Zeit zwischen dem Schreiben und Lesen der Datei durch einen anderen Test überschreiben. Der zweite Test wird dann fehlschlagen, nicht weil der Code fehlerhaft ist, sondern weil die Tests sich gegenseitig stören, während sie parallel ausgeführt werden. Eine Lösung besteht darin, sicherzustellen, dass jeder Test in eine andere Datei schreibt; eine andere Lösung besteht darin, die Tests nacheinander auszuführen.

Wenn du die Tests nicht parallel ausführen möchtest oder wenn du eine feinere Kontrolle über die Anzahl der verwendeten Threads möchten, kannst du das Flag `--test-threads` und die Anzahl der Threads, die du verwenden möchtest, an die Testbinärdatei senden. Schau dir das folgende Beispiel an:

```bash
cargo test -- --test-threads=1
```

Wir setzen die Anzahl der Testthreads auf `1`, was dem Programm mitteilt, keine Parallelität zu verwenden. Das Ausführen der Tests mit einem Thread wird länger dauern als das parallele Ausführen, aber die Tests werden sich nicht gegenseitig stören, wenn sie sich einen Zustand teilen.
