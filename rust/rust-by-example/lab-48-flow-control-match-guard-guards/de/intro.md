# Einführung

In diesem Lab lernen wir, wie in Rust Match Guards verwendet werden, um Arme basierend auf Bedingungen zu filtern. Der Match Guard wird nach dem Muster hinzugefügt und wird durch das `if`-Schlüsselwort gefolgt von einer Bedingung dargestellt. Die Bedingung des Guards ermöglicht es uns, die Übereinstimmung von Mustern weiter zu verfeinern und zusätzliche Prüfungen durchzuführen, bevor der entsprechende Arm des Match-Ausdrucks ausgeführt wird. Es ist jedoch wichtig zu beachten, dass der Compiler die Guard-Bedingungen nicht bei der Prüfung der Musterabdeckung berücksichtigt, sodass es erforderlich ist, sicherzustellen, dass alle Muster weiterhin von dem Match-Ausdruck abgedeckt werden.

> **Hinweis:** Wenn im Lab kein Dateiname angegeben ist, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
