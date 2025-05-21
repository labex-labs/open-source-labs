# Erstellen einer praktischen Anwendung

Nachdem wir nun eine funktionierende Funktion haben, um die Differenz zwischen Daten in Sekunden zu berechnen, erstellen wir eine praktischere Anwendung. Wir werden einen einfachen Timer erstellen, der berechnet, wie viel Zeit seit dem Start vergangen ist.

## Erstellen einer Timer-Anwendung

Erstellen Sie eine neue Datei mit dem Namen `timer.js` im WebIDE:

1. Klicken Sie auf das Symbol "Explorer" in der linken Seitenleiste.
2. Klicken Sie mit der rechten Maustaste im Dateiexplorer und wählen Sie "Neue Datei" aus.
3. Benennen Sie die Datei `timer.js` und drücken Sie die Eingabetaste.
4. Fügen Sie den folgenden Code in die Datei ein:

```javascript
// Funktion zur Berechnung der Differenz zwischen zwei Daten in Sekunden
const getSecondsDiffBetweenDates = (dateInitial, dateFinal) =>
  (dateFinal - dateInitial) / 1000;

// Startzeit - wenn das Skript beginnt, auszuführen
const startTime = new Date();
console.log(`Timer gestartet um: ${startTime.toLocaleTimeString()}`);

// Funktion zum Aktualisieren und Anzeigen der verstrichenen Zeit
function updateTimer() {
  const currentTime = new Date();
  const elapsedSeconds = getSecondsDiffBetweenDates(startTime, currentTime);

  // Formatieren der Zeit als Stunden:Minuten:Sekunden
  const hours = Math.floor(elapsedSeconds / 3600);
  const minutes = Math.floor((elapsedSeconds % 3600) / 60);
  const seconds = Math.floor(elapsedSeconds % 60);

  const formattedTime = `${hours.toString().padStart(2, "0")}:${minutes
    .toString()
    .padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;

  // Leeren der Konsole und Anzeigen der aktualisierten Zeit
  console.clear();
  console.log(`Timer gestartet um: ${startTime.toLocaleTimeString()}`);
  console.log(`Verstrichene Zeit: ${formattedTime}`);
}

// Aktualisieren des Timers alle Sekunden
console.log("Timer läuft... Drücken Sie Strg+C, um ihn zu stoppen.");
const timerInterval = setInterval(updateTimer, 1000);

// Halten des Skripts am Laufen
setTimeout(() => {
  clearInterval(timerInterval);
  console.log("\nTimer gestoppt nach 1 Minute.");
}, 60000); // Laufzeit: 1 Minute
```

Speichern Sie die Datei, indem Sie Strg+S drücken oder auf Datei > Speichern klicken.

## Ausführen der Timer-Anwendung

Um die Timer-Anwendung auszuführen, verwenden Sie den folgenden Befehl im Terminal:

```bash
node timer.js
```

Der Timer startet und wird jede Sekunde aktualisiert, um anzuzeigen, wie viel Zeit seit dem Start vergangen ist. Der Timer stoppt automatisch nach 1 Minute, oder Sie können ihn früher stoppen, indem Sie Strg+C drücken.

## Verständnis der Timer-Anwendung

Lassen Sie uns analysieren, wie die Timer-Anwendung funktioniert:

1. Wir definieren die `getSecondsDiffBetweenDates`-Funktion, um die Zeitdifferenz in Sekunden zu berechnen.
2. Wir erfassen die Startzeit, wenn das Skript beginnt, auszuführen.
3. Wir definieren eine `updateTimer`-Funktion, die:
   - Die aktuelle Zeit ermittelt
   - Berechnet, wie viele Sekunden seit der Startzeit vergangen sind
   - Die verstrichene Zeit im Format Stunden:Minuten:Sekunden formatiert
   - Die formatierte Zeit anzeigt
4. Wir verwenden `setInterval`, um die `updateTimer`-Funktion alle 1000 Millisekunden (1 Sekunde) auszuführen.
5. Wir verwenden `setTimeout`, um den Timer nach 60000 Millisekunden (1 Minute) zu stoppen.

Diese Anwendung zeigt eine praktische Verwendung unserer Funktion zur Berechnung der Datumsdifferenz für die Erstellung eines Echtzeit-Timers.
