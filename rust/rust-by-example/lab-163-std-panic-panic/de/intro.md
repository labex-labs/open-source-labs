# Einführung

In diesem Lab lernen wir über die `panic!`-Makro in Rust, das verwendet werden kann, um einen Fehler zu erzeugen und den Stapel zu entspannen, was dazu führt, dass das Programm die Fehlermeldung ausgibt und beendet wird. Die Laufzeit kümmert sich darum, alle von einem Thread besitzten Ressourcen freizugeben, indem sie den Destruktor seiner Objekte aufruft. Wir betrachten auch ein Beispiel für die Verwendung des `panic!`-Makros, um Division durch Null zu behandeln, und überprüfen, dass dies keine Speicherlecks verursacht, indem wir Valgrind verwenden.

> **Hinweis:** Wenn im Lab kein Dateiname angegeben ist, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
