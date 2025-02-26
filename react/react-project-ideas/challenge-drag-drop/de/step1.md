# Drag Drop

Um loszulegen, öffnen Sie den Editor. Sie können die folgenden Dateien in Ihrem Editor sehen.

```txt
├── public
├── src
│   ├── App.js
│   ├── App.css
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

- Bitte vervollständigen Sie diese Herausforderung in der Datei `App.js`.
- Die Funktion `onDragStart` ist definiert. Es ist ein Ereignishandler für das dragstart-Ereignis auf einer Task-Karte. Es setzt die Datenübertragungsdaten auf die Name-Eigenschaft der Aufgabe, die verwendet werden wird, um die Aufgabe zu identifizieren, wenn sie fallen gelassen wird.
- Die Funktion `onDrop` ist definiert. Es ist ein Ereignishandler für das drop-Ereignis auf der Task-Board. Es holt den Namen der Aufgabe aus den Datenübertragungsdaten, aktualisiert die Kategorie der Aufgabe im tasks-Zustand basierend auf der Drop-Location (cat) und setzt den aktualisierten tasks-Zustand mit setTasks.

## Beispiel

Sobald Sie den Code abgeschlossen haben, führen Sie ihn mit dem folgenden Befehl aus:

```bash
npm start
```

Das fertige Ergebnis sieht wie folgt aus:

![Drag and drop demo](../assets/finished.gif)
