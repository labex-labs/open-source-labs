# Kompilieren und Ausführen sind getrennte Schritte

Du hast gerade ein neu erstelltes Programm ausgeführt, also lassen wir uns jeden Schritt im Prozess untersuchen.

Bevor du ein Rust-Programm ausführst, musst du es mit dem Rust-Compiler kompilieren, indem du den Befehl `rustc` eingibst und ihm den Namen deiner Quelldatei angibst, wie folgt:

```bash
rustc main.rs
```

Wenn du einen Hintergrund in C oder C++ hast, wirst du bemerken, dass dies ähnlich zu `gcc` oder `clang` ist. Nach erfolgreicher Kompilierung gibt Rust eine binäre Ausführdatei aus.

Auf Linux, macOS und PowerShell unter Windows kannst du die Ausführdatei sehen, indem du im Terminal den Befehl `ls` eingibst:

```bash
$ ls
main main.rs
```

Von hier aus führst du die `main`-Datei aus, wie folgt:

```bash
./main
```

Wenn deine `main.rs` dein "Hello, world!"-Programm ist, druckt diese Zeile `Hello, world!` auf dein Terminal.

Wenn du mit einer dynamischen Sprache wie Ruby, Python oder JavaScript vertrauter bist, bist du vielleicht nicht gewohnt, ein Programm separat zu kompilieren und auszuführen. Rust ist eine _ahead-of-time kompilierte_ Sprache, was bedeutet, dass du ein Programm kompilieren und die Ausführdatei an jemand anderen geben kannst, und dieser kann sie auch ausführen, auch wenn er nicht einmal Rust installiert hat. Wenn du jemandem eine `.rb`-, `.py`- oder `.js`-Datei gibst, muss er eine Ruby-, Python- oder JavaScript-Implementierung installiert haben (jeweils). Aber in diesen Sprachen brauchst du nur einen Befehl, um dein Programm zu kompilieren und auszuführen. Alles ist ein Kompromiss in der Sprachendesign.

Mit `rustc` zu kompilieren ist für einfache Programme ausreichend, aber wenn dein Projekt wächst, wirst du alle Optionen verwalten und es einfacher machen, deinen Code zu teilen wollen. Als nächstes werden wir dir das Cargo-Tool vorstellen, das dir helfen wird, echte Rust-Programme zu schreiben.
