# Tic Tac Toe

Um loszulegen, öffne den Editor. Du kannst die folgenden Dateien in deinem Editor sehen.

```txt
├── public
├── src
│   ├── components
│   │   ├── common
│   │   │   └── Utils.js
│   │   ├── Board.js
│   │   ├── Game.js
│   │   └── Square.js
│   ├── App.css
│   ├── App.js
│   ├── App.test.js
│   ├── index.css
│   ├── index.js
│   ├── logo.svg
│   ├── reportWebVitals.js
│   └── setupTests.js
├── package-lock.json
└── package.json
```

## Anforderungen

- Um die Projektabhängigkeiten zu installieren, verwende den folgenden Befehl:

  ```bash
  npm i
  ```

- Bitte vervollständige diese Herausforderung in der Datei `src/components/Game.js`.
- Verwende den `useState`-Hook, um drei Zustandsvariablen zu definieren: board, xTurn und winner.
  - `board` repräsentiert den Zustand des Spielfelds. Es wird initialisiert als ein Array von 9 Elementen, wobei jedes Element zunächst auf null gesetzt ist.
  - `xTurn` ist ein boolescher Flag, das angibt, ob es derzeit X's Zug ist.
  - `winner` speichert das Ergebnis der `calculateWinner`-Funktion, die den Gewinner anhand des aktuellen Zustands des Spielfelds bestimmt.
- Die `handleClick`-Funktion wird aufgerufen, wenn auf ein Quadrat auf dem Spielfeld geklickt wird.
  - Sie erstellt eine Kopie des aktuellen Spielfeldzustands mit dem Spread-Operator (`[...board]`) und weist sie der tmpBoard zu.
  - Wenn es bereits einen Gewinner gibt (winner ist wahr) oder das geklickte Quadrat bereits markiert ist (`tmpBoard[i]` ist wahr), kehrt die Funktion ohne Änderungen zurück.
  - Andernfalls aktualisiert es den Wert des geklickten Quadrats in `tmpBoard` auf entweder "X" oder "O" basierend auf dem Wert von `xTurn`.
  - Die aktualisierte `tmpBoard` wird dann als neuer Wert für den Zustand des Spielfelds mit `setBoard` gesetzt, und xTurn wird mit setXTurn umgeschaltet.

## Beispiel

Wenn du den Code abgeschlossen hast, führe ihn mit dem folgenden Befehl aus:

```bash
npm start
```

Das fertige Ergebnis sieht wie folgt aus:

![Tic Tac Toe game demo](../assets/finished.gif)
