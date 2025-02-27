# Ein ein-threadiger Webserver bauen

Wir beginnen damit, einen ein-threadigen Webserver zum Laufen zu bringen. Bevor wir beginnen, schauen wir uns einen kurzen Überblick über die Protokolle an, die bei der Erstellung von Webservern beteiligt sind. Die Details dieser Protokolle liegen außerhalb des Rahmens dieses Buches, aber ein kurzer Überblick wird Ihnen die benötigten Informationen geben.

Die beiden Hauptprotokolle, die bei Webservern beteiligt sind, sind das _Hypertext Transfer Protocol_ _(HTTP)_ und das _Transmission Control Protocol_ _(TCP)_. Beide Protokolle sind _request-response_ -Protokolle, was bedeutet, dass ein _Client_ Anfragen initiiert und ein _Server_ auf die Anfragen hört und eine Antwort an den Client liefert. Der Inhalt dieser Anfragen und Antworten wird durch die Protokolle definiert.

TCP ist das niedriger Ebene liegende Protokoll, das die Details darüber beschreibt, wie Informationen von einem Server zum anderen gelangen, aber nicht angibt, was diese Informationen sind. HTTP baut auf TCP auf, indem es den Inhalt der Anfragen und Antworten definiert. Technisch ist es möglich, HTTP mit anderen Protokollen zu verwenden, aber in den vast majority of cases, sendet HTTP seine Daten über TCP. Wir werden mit den rohen Bytes von TCP- und HTTP-Anfragen und -Antworten arbeiten.
