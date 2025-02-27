# Einführung

In diesem Lab lernen wir über partielle Verschiebungen innerhalb der Destrukturierung einer einzelnen Variable, bei der sowohl `by-move`- als auch `by-reference`-Musterbindungen gleichzeitig verwendet werden können. Dies führt zu einer partiellen Verschiebung der Variable, wodurch einige Teile verschoben werden können, während andere weiterhin referenziert werden können. Wenn eine übergeordnete Variable partiell verschoben wird, kann sie danach nicht mehr als Ganzes verwendet werden, aber die Teile, die nur referenziert und nicht verschoben werden, können weiterhin verwendet werden.

> **Hinweis:** Wenn das Lab keinen Dateinamen angibt, können Sie einen beliebigen Dateinamen verwenden. Beispielsweise können Sie `main.rs` verwenden und es mit `rustc main.rs &&./main` kompilieren und ausführen.
