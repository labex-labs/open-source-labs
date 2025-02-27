# Vererbung als Typsystem und als Code - Wiederverwendung

_Vererbung_ ist ein Mechanismus, durch den ein Objekt Elemente aus der Definition eines anderen Objekts erben kann und somit die Daten und das Verhalten des Elternobjekts erhält, ohne dass Sie es erneut definieren müssen.

Wenn eine Sprache Vererbung haben muss, um objektorientiert zu sein, dann ist Rust keine solche Sprache. Es gibt keine Möglichkeit, eine Struktur zu definieren, die die Felder und Methodenimplementierungen der Elternstruktur erbt, ohne Makros zu verwenden.

Wenn Sie jedoch in Ihrem Programmierungswerkzeugkasten an Vererbung gewöhnt sind, können Sie in Rust andere Lösungen verwenden, je nachdem, warum Sie ursprünglich auf Vererbung zurückgegriffen haben.

Es gibt zwei Hauptgründe, warum Sie Vererbung wählen würden. Ein Grund ist die Wiederverwendung von Code: Sie können ein bestimmtes Verhalten für einen Typ implementieren, und die Vererbung ermöglicht es Ihnen, diese Implementierung für einen anderen Typ zu verwenden. Sie können dies in begrenztem Maße in Rust -Code tun, indem Sie Standard -Trait -Methodenimplementierungen verwenden, wie Sie es in Listing 10-14 gesehen haben, als wir eine Standardimplementierung der `summarize` -Methode auf dem `Summary` -Trait hinzufügten. Jeder Typ, der das `Summary` -Trait implementiert, hätte die `summarize` -Methode verfügbar, ohne weitere Codezeilen. Dies ähnelt der Situation, in der eine Elternklasse eine Implementierung einer Methode hat und eine erbende Kindklasse ebenfalls die Implementierung der Methode hat. Wir können auch die Standardimplementierung der `summarize` -Methode überschreiben, wenn wir das `Summary` -Trait implementieren, was der Situation ähnelt, in der eine Kindklasse die Implementierung einer von der Elternklasse geerbten Methode überschreibt.

Der andere Grund, Vererbung zu verwenden, bezieht sich auf das Typsystem: um es zu ermöglichen, dass ein Kindtyp an den gleichen Stellen wie der Elterntyp verwendet werden kann. Dies wird auch als _Polymorphismus_ bezeichnet, was bedeutet, dass Sie zur Laufzeit mehrere Objekte für einander austauschen können, wenn sie bestimmte Merkmale teilen.

> **Polymorphismus**
>
> Für viele Menschen ist Polymorphismus synonym mit Vererbung. Tatsächlich ist es jedoch ein allgemeineres Konzept, das sich auf Code bezieht, der mit Daten mehrerer Typen arbeiten kann. Bei der Vererbung sind diese Typen im Allgemeinen Unterklassen.
>
> Rust verwendet stattdessen Generics, um über verschiedene mögliche Typen abzustrahlen, und Trait -Bedingungen, um Beschränkungen auf das zu setzen, was diese Typen liefern müssen. Dies wird manchmal als _beschränkter parametrischer Polymorphismus_ bezeichnet.

In letzter Zeit ist die Vererbung als Lösung für das Programmierungsdesign in vielen Programmiersprachen weniger beliebt geworden, weil es oft das Risiko birgt, mehr Code zu teilen, als notwendig ist. Unterklassen sollten nicht immer alle Merkmale ihrer Elternklasse teilen, aber dies passiert bei der Vererbung. Dies kann die Flexibilität des Programmdesigns verringern. Es führt auch zur Möglichkeit, Methoden auf Unterklassen aufzurufen, die keinen Sinn ergeben oder die Fehler verursachen, weil die Methoden nicht auf die Unterklasse zutreffen. Darüber hinaus erlauben einige Sprachen nur die einfache Vererbung (d.h. eine Unterklasse kann nur von einer Klasse erben), was die Flexibilität des Programmdesigns weiter einschränkt.

Aus diesen Gründen nimmt Rust den anderen Ansatz, Trait -Objekte anstelle von Vererbung zu verwenden. Schauen wir uns an, wie Trait -Objekte Polymorphismus in Rust ermöglichen.
