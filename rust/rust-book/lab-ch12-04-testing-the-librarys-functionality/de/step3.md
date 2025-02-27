# Schreiben von Code, um den Test zu bestehen

Derzeit fehlschlägt unser Test, weil wir immer einen leeren Vektor zurückgeben. Um das zu beheben und `search` zu implementieren, muss unser Programm die folgenden Schritte ausführen:

1.  Iterieren Sie über jede Zeile des Inhalts.
2.  Überprüfen Sie, ob die Zeile unseren Suchstring enthält.
3.  Wenn ja, fügen Sie sie zur Liste der zurückgegebenen Werte hinzu.
4.  Wenn nicht, tun Sie nichts.
5.  Geben Sie die Liste der übereinstimmenden Ergebnisse zurück.

Lassen Sie uns jeden Schritt einzeln durcharbeiten, beginnend mit dem Iterieren über die Zeilen.
