# Allgemein verwendete Abschnitte

Wir haben im Listing 14-1 den Markdown-Überschriftentext `# Beispiele` verwendet, um einen Abschnitt im HTML mit dem Titel "Beispiele" zu erstellen. Hier sind einige weitere Abschnitte, die Crate-Autoren in ihrer Dokumentation häufig verwenden:

- **Panics**: Die Szenarien, in denen die dokumentierte Funktion in Panik geraten kann. Aufrufer der Funktion, die nicht möchten, dass ihr Programm in Panik gerät, sollten sicherstellen, dass sie die Funktion in diesen Situationen nicht aufrufen.
- **Fehler**: Wenn die Funktion ein `Result` zurückgibt, kann es für die Aufrufer hilfreich sein, die Arten von Fehlern zu beschreiben, die auftreten können, und welche Bedingungen dazu führen können, dass diese Fehler zurückgegeben werden, damit sie Code schreiben können, um die verschiedenen Arten von Fehlern auf unterschiedliche Weise zu behandeln.
- **Sicherheit**: Wenn die Funktion unsicher aufzurufen ist (wir diskutieren die Unsicherheit im Kapitel 19), sollte es einen Abschnitt geben, der erklärt, warum die Funktion unsicher ist und die Invarianten umfasst, die die Funktion erwartet, dass die Aufrufer einhalten.

Die meisten Dokumentationskommentare brauchen nicht alle diese Abschnitte, aber dies ist eine gute Kontrollliste, um Sie daran zu erinnern, an welchen Aspekten Ihres Codes die Benutzer interessiert sein werden.
