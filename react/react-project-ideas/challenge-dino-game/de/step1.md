# Dino Spiel

Um loszulegen, öffnen Sie den Editor. Sie können die folgenden Dateien in Ihrem Editor sehen.

```txt
├── public
├── src
│   ├──components
│   │  └── Dino
│   │       ├── img
│   │       │   ├── cactus.png
│   │       │   └── trex.png
│   │       ├── Dino.css
│   │       └── Dino.js
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

- Bitte vervollständigen Sie diese Herausforderung in der Datei `src/components/Dino/Dino.js`.
- Initialisieren Sie zwei `useRef`-Hooks: `dinoRef` und `cactusRef`. Diese Hooks werden verwendet, um auf die Dinosaurier- und Kaktus-DOM-Elemente zu verweisen.
- Initialisieren Sie einen `useState`-Hook namens score mit einem Anfangswert von 0. Dieser Hook wird die Punktzahl des Spielers verfolgen.
- Definieren Sie die jump-Funktion. Sie fügt die Klasse "jump" zum von dinoRef referenzierten Dinosaurier-DOM-Element hinzu. Dies löst eine CSS-Animation aus, die den Dinosaurier springen lässt. Nach einer Wartezeit von 300 Millisekunden wird die Klasse "jump" entfernt, und der Dinosaurier kehrt an seine ursprüngliche Position zurück.
- Verwenden Sie den `useEffect`-Hook, um die Spiel-Logik zu behandeln. Er setzt einen Intervalltimer ein, der alle 10 Millisekunden ausgeführt wird. Innerhalb der Intervallfunktion werden die aktuellen Positionen des Dinosauriers (dinoTop) und des Kaktus (cactusLeft) mithilfe der getComputedStyle-Funktion abgerufen.
- Es wird überprüft, ob ein Konflikt aufgetreten ist, indem die Kaktusposition (cactusLeft) mit der Dinosaurierposition (dinoTop) verglichen wird. Wenn der Kaktus innerhalb eines bestimmten Bereichs und auf der gleichen Höhe wie der Dinosaurier ist, wird ein Konflikt erkannt. In diesem Fall wird eine Meldung mit der Punktzahl des Spielers angezeigt, und die Punktzahl wird mit der setScore-Funktion auf 0 zurückgesetzt. Andernfalls wird die Punktzahl um 1 erhöht, indem setScore verwendet wird.
- Der erste `useEffect`-Hook gibt auch eine Bereinigungsmethode zurück, die das Intervall beendet, wenn die Komponente entfernt wird. Dies gewährleistet, dass das Intervall richtig bereinigt wird, um Speicherlecks zu vermeiden.
- Der zweite `useEffect`-Hook ist verantwortlich für das Einrichten und Entfernen eines Ereignislisteners für das "keydown"-Ereignis. Wenn eine Taste gedrückt wird, wird die jump-Funktion aufgerufen. Dies ermöglicht es dem Spieler, den Dinosaurier zu einem Sprung zu bringen, indem er eine beliebige Taste drückt.

## Beispiel

Sobald Sie den Code abgeschlossen haben, führen Sie ihn mit dem folgenden Befehl aus:

```bash
npm start
```

Das fertige Ergebnis sieht wie folgt aus:

![Dino game final result](../assets/finished.gif)
