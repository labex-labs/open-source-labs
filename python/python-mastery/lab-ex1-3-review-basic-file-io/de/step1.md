# Das Problem verstehen

In diesem Schritt werden wir zunächst verstehen, welches Problem wir lösen müssen, und uns dann die Daten ansehen, mit denen wir arbeiten werden. Dies ist ein wichtiger erster Schritt bei jeder Programmieraufgabe, da es uns hilft, genau zu wissen, was wir erreichen wollen und welche Ressourcen uns zur Verfügung stehen.

In Ihrem Projektverzeichnis befindet sich eine Datei namens `portfolio.dat`. Diese Datei speichert Informationen über ein Aktienportfolio. Ein Portfolio ist wie eine Sammlung verschiedener Aktien, die ein Investor besitzt. Jede Zeile in dieser Datei repräsentiert einen einzelnen Aktienkauf. Das Format jeder Zeile ist wie folgt:

```
[Stock Symbol] [Number of Shares] [Price per Share]
```

Das Aktiensymbol ist ein kurzer Code, der die Aktie eines bestimmten Unternehmens repräsentiert. Die Anzahl der Aktien gibt an, wie viele Einheiten dieser Aktie gekauft wurden, und der Preis pro Aktie ist die Kosten für eine Einheit dieser Aktie.

Schauen wir uns ein Beispiel an. Betrachten Sie die erste Zeile der Datei:

```
AA 100 32.20
```

Diese Zeile gibt an, dass 100 Aktien der Aktie mit dem Symbol "AA" gekauft wurden. Jede Aktie kostete 32,20 US-Dollar.

Wenn Sie sehen möchten, was in der Datei `portfolio.dat` steht, können Sie den folgenden Befehl im Terminal ausführen. Der Befehl `cat` ist ein nützliches Werkzeug im Terminal, das es Ihnen ermöglicht, den Inhalt einer Datei anzuzeigen.

```bash
cat ~/project/portfolio.dat
```

Nun ist Ihre Aufgabe, ein Python-Programm namens `pcost.py` zu erstellen. Dieses Programm wird drei Hauptaufgaben ausführen:

1. Zunächst muss es die Datei `portfolio.dat` öffnen und lesen. Das Öffnen einer Datei in Python ermöglicht es unserem Programm, auf die darin gespeicherten Daten zuzugreifen.
2. Dann muss es die Gesamtkosten aller Aktienkäufe im Portfolio berechnen. Dazu müssen wir für jede Zeile in der Datei die Anzahl der Aktien mit dem Preis pro Aktie multiplizieren. Nachdem wir diese Werte für jede Zeile erhalten haben, summieren wir sie alle auf. Dies gibt uns die Gesamtmenge an Geld, die für alle Aktien im Portfolio ausgegeben wurde.
3. Schließlich sollte das Programm die Gesamtkosten ausgeben. Auf diese Weise können wir das Ergebnis unserer Berechnungen sehen.

Beginnen wir damit, die Datei `pcost.py` zu erstellen. Sie können den Editor verwenden, um diese Datei zu öffnen und zu bearbeiten. Sie wurde bereits für Sie während des Einrichtungsschritts erstellt. In dieser Datei werden Sie den Python-Code schreiben, um das Problem zu lösen, das wir gerade besprochen haben.
