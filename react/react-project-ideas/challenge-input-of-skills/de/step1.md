# Eingabe von Fähigkeiten

Um loszulegen, öffnen Sie den Editor. Sie können die folgenden Dateien in Ihrem Editor sehen.

```txt
├── public
├── src
│   ├── components
│   │   └── TagInput.js
│   ├── App.css
│   ├── App.js
│   ├── index.css
│   └── index.js
├── package-lock.json
└── package.json
```

## Anforderungen

- Um die Projektabhängigkeiten zu installieren, verwenden Sie den folgenden Befehl:

  ```bash
  npm i
  ```

- Bitte vervollständigen Sie diese Herausforderung in der Datei `src/component/TagInput.js`.
- Die `handleAddTag`-Funktion wird aufgerufen, wenn eine Taste in das Eingabefeld gedrückt wird. Wenn die Taste nicht die Enter-Taste ist, kehrt die Funktion frühzeitig zurück und tut nichts. Andernfalls prüft sie den Eingabewert und fügt ihn dem Tags-Zustand hinzu, wenn er nicht leer ist und noch nicht hinzugefügt wurde. Anschließend leert sie das Eingabefeld.
- Die `onDeleteTag`-Funktion wird aufgerufen, wenn ein Tag angeklickt wird. Sie filtert den Tags-Zustand, um das angeklickte Tag zu entfernen, und aktualisiert den Zustand mit den gefilterten Tags.

## Beispiel

Sobald Sie den Code abgeschlossen haben, führen Sie ihn mit dem folgenden Befehl aus:

```bash
npm start
```

Das fertige Ergebnis sieht wie folgt aus:

![Tag input functionality demo](../assets/finished.gif)
