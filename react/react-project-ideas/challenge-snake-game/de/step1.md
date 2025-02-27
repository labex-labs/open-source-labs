# Snake-Spiel

Um loszulegen, öffnen Sie den Editor. Sie können die folgenden Dateien in Ihrem Editor sehen.

```txt
├── public
├── src
│   ├── components
│   │   ├── Food.js
│   │   └── Snake.js
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

- Bitte vervollständigen Sie diese Herausforderung in der Datei `src/App.js`.
- Die Funktion `randomFoodPosition` ist definiert, um eine zufällige Position für das Essobjekt auf der Spielfläche zu generieren.
- Innerhalb der App-Funktion sind mehrere Zustandsvariablen definiert, die mit dem useState-Hook erstellt werden:
  - `snake` repräsentiert den aktuellen Zustand der Schlange.
  - `lastDirection` repräsentiert die letzte Richtung, in die sich die Schlange bewegt hat.
  - `foodPosition` repräsentiert die aktuelle Position des Essobjekts.
  - `isStarted` bestimmt, ob das Spiel gestartet hat.
  - `gameOver` gibt an, ob das Spiel beendet ist.
  - `playgroundRef` ist eine Referenz auf das Spielflächenelement.

## Beispiel

Sobald Sie den Code abgeschlossen haben, führen Sie ihn mit dem folgenden Befehl aus:

```bash
npm start
```

Das fertige Ergebnis sieht wie folgt aus:

![Snake game final result](../assets/finished.gif)
