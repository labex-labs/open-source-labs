# Trade-offs of the State Pattern

Wir haben gezeigt, dass Rust in der Lage ist, das objektorientierte State-Pattern zu implementieren, um die verschiedenen Arten von Verhalten zu kapseln, die ein Beitrag in jedem Zustand haben sollte. Die Methoden auf `Post` wissen nichts über die verschiedenen Verhaltensweisen. Mit der Art, wie wir den Code organisiert haben, müssen wir an nur einem Ort schauen, um zu wissen, auf welche verschiedenen Arten ein veröffentlichter Beitrag verhalten kann: die Implementierung des `State`-Traits auf der `Published`-Struktur.

Wenn wir eine alternative Implementierung erstellen würden, die das State-Pattern nicht verwenden würde, könnten wir stattdessen `match`-Ausdrücke in den Methoden auf `Post` oder sogar im `main`-Code verwenden, der den Zustand des Beitrags überprüft und das Verhalten an diesen Stellen ändert. Das würde bedeuten, dass wir an mehreren Stellen schauen müssten, um alle Auswirkungen eines Beitrags im veröffentlichten Zustand zu verstehen! Dies würde sich nur noch erhöhen, wenn wir mehr Zustände hinzufügen würden: jeder dieser `match`-Ausdrücke würde einen weiteren Fall benötigen.

Mit dem State-Pattern brauchen die `Post`-Methoden und die Stellen, an denen wir `Post` verwenden, keine `match`-Ausdrücke, und um einen neuen Zustand hinzuzufügen, müssten wir nur eine neue Struktur hinzufügen und die Trait-Methoden auf dieser einen Struktur implementieren.

Die Implementierung mit dem State-Pattern lässt sich leicht erweitern, um weitere Funktionalität hinzuzufügen. Um die Einfachheit der Wartung von Code zu sehen, der das State-Pattern verwendet, versuchen Sie einige dieser Vorschläge:

- Fügen Sie eine `reject`-Methode hinzu, die den Zustand des Beitrags von `PendingReview` zurück in `Draft` ändert.
- Erfordern Sie zwei Aufrufe von `approve`, bevor der Zustand in `Published` geändert werden kann.
- Erlauben Sie es Benutzern, nur wenn ein Beitrag im `Draft`-Zustand ist, Textinhalt hinzuzufügen. Tipp: Lassen Sie das Zustandsobjekt für das verantwortlich sein, was sich am Inhalt ändern könnte, aber nicht für die Modifikation von `Post`.

Ein Nachteil des State-Patterns ist, dass, da die Zustände die Übergänge zwischen den Zuständen implementieren, einige der Zustände miteinander gekoppelt sind. Wenn wir einen weiteren Zustand zwischen `PendingReview` und `Published` hinzufügen, wie `Scheduled`, müssten wir den Code in `PendingReview` ändern, um zu `Scheduled` zu übergehen. Es wäre weniger Arbeit, wenn `PendingReview` nicht mit der Hinzufügung eines neuen Zustands geändert werden müsste, aber das würde bedeuten, dass wir zu einem anderen Entwurfsmuster wechseln müssten.

Ein weiterer Nachteil ist, dass wir einige Logik dupliziert haben. Um einige der Duplikation zu eliminieren, könnten wir versuchen, Standardimplementierungen für die `request_review`- und `approve`-Methoden auf dem `State`-Trait zu erstellen, die `self` zurückgeben. Dies würde jedoch nicht funktionieren: Wenn `State` als Trait-Objekt verwendet wird, weiß der Trait nicht genau, was das konkrete `self` sein wird, daher ist der Rückgabetyp zur Compile-Zeit nicht bekannt.

Andere Duplikationen umfassen die ähnlichen Implementierungen der `request_review`- und `approve`-Methoden auf `Post`. Beide Methoden delegieren an die Implementierung der gleichen Methode auf dem Wert im `state`-Feld von `Option` und setzen den neuen Wert des `state`-Felds auf das Ergebnis. Wenn wir viele Methoden auf `Post` hätten, die diesem Muster folgten, könnten wir überlegen, eine Makro zu definieren, um die Wiederholung zu eliminieren (siehe "Makros").

Indem wir das State-Pattern genau so implementieren, wie es für objektorientierte Sprachen definiert ist, nutzen wir die Stärken von Rust nicht so optimal wie möglich. Schauen wir uns einige Änderungen an, die wir am `blog`-Kratzen vornehmen können, um ungültige Zustände und Übergänge zu Kompilierungsfehlern zu machen.
