# Übung 3.12: Verwenden Ihres Bibliotheksmoduls

Im Abschnitt 2 haben Sie ein Programm `report.py` geschrieben, das einen Aktienbericht wie diesen erzeugt hat:

          Name     Anteile      Preis     Änderung
    ---------- ---------- ---------- ----------
            AA        100       9.22     -22.98
           IBM         50     106.28      15.18
           CAT        150      35.46     -47.98
          MSFT        200      20.89     -30.34
            GE         95      13.48     -26.89
          MSFT         50      20.89     -44.21
           IBM        100     106.28      35.84

Nehmen Sie dieses Programm und ändern Sie es so, dass alle Verarbeitung der Eingabedateien mit Funktionen aus Ihrem `fileparse`-Modul erfolgt. Dazu importieren Sie `fileparse` als Modul und ändern Sie die Funktionen `read_portfolio()` und `read_prices()`, um die Funktion `parse_csv()` zu verwenden.

Verwenden Sie das interaktive Beispiel am Anfang dieser Übung als Anleitung. Danach sollten Sie genau die gleiche Ausgabe wie zuvor erhalten.
