# Aktualisieren einer Hash-Tabelle (Hash Map)

Obwohl die Anzahl der Schlüssel-Wert-Paare wachsen kann, kann jeder eindeutige Schlüssel zu einem bestimmten Zeitpunkt nur einen Wert zugeordnet haben (aber nicht umgekehrt: Beispielsweise könnten sowohl die Blue-Mannschaft als auch die Yellow-Mannschaft den Wert `10` in der `scores`-Hash-Tabelle gespeichert haben).

Wenn Sie die Daten in einer Hash-Tabelle ändern möchten, müssen Sie entscheiden, wie Sie den Fall behandeln möchten, wenn einem Schlüssel bereits ein Wert zugewiesen ist. Sie könnten den alten Wert durch den neuen Wert ersetzen und dabei den alten Wert völlig ignorieren. Sie könnten den alten Wert beibehalten und den neuen Wert ignorieren und den neuen Wert nur hinzufügen, wenn der Schlüssel _noch nicht_ einen Wert hat. Oder Sie könnten den alten Wert und den neuen Wert kombinieren. Schauen wir uns an, wie man dies jeweils macht!
