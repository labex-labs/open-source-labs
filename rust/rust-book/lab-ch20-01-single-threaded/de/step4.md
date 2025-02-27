# Ein genaueres Esehen auf eine HTTP-Anfrage

HTTP ist ein textbasiertes Protokoll, und eine Anfrage hat dieses Format:

    Methode Anfrage-URI HTTP-Version CRLF
    Header CRLF
    Nachrichtenkörper

Die erste Zeile ist die _Anfragezeile_, die Informationen darüber enthält, was der Client anfordert. Der erste Teil der Anfragezeile gibt die verwendete _Methode_ an, wie `GET` oder `POST`, die beschreibt, wie der Client diese Anfrage stellt. Unser Client verwendete eine `GET`-Anfrage, was bedeutet, dass er Informationen anfordert.

Der nächste Teil der Anfragezeile ist _/_, was den _uniform resource identifier_ _(URI)_ angibt, den der Client anfordert: Ein URI ist fast, aber nicht ganz, dasselbe wie ein _uniform resource locator_ _(URL)_. Der Unterschied zwischen URIs und URLs ist für unsere Zwecke in diesem Kapitel nicht wichtig, aber die HTTP-Spezifikation verwendet den Begriff _URI_, daher können wir uns hier einfach _URL_ für _URI_ ersetzen.

Der letzte Teil ist die HTTP-Version, die der Client verwendet, und dann endet die Anfragezeile in einer CRLF-Sequenz. (CRLF steht für _carriage return_ und _line feed_, die Begriffe aus den Schreibmaschinenzeiten!) Die CRLF-Sequenz kann auch als `\r\n` geschrieben werden, wobei `\r` ein Wagenrücklauf und `\n` ein Zeilenumbruch ist. Die _CRLF-Sequenz_ trennt die Anfragezeile von den restlichen Anfragedaten. Beachten Sie, dass wenn die CRLF gedruckt wird, wir einen neuen Zeilenanfang sehen, statt `\r\n`.

Betrachtend die Anfragezeiledaten, die wir bisher von unserem ausgeführten Programm erhalten haben, sehen wir, dass `GET` die Methode, _/_ die Anfrage-URI und `HTTP/1.1` die Version ist.

Nach der Anfragezeile sind die verbleibenden Zeilen ab `Host:` Header. `GET`-Anfragen haben keinen Körper.

Versuchen Sie, eine Anfrage von einem anderen Browser zu stellen oder eine andere Adresse anzufordern, wie _127.0.0.1:7878/test_, um zu sehen, wie sich die Anfragedaten ändern.

Jetzt, da wir wissen, was der Browser anfordert, senden wir etwas Daten zurück!
