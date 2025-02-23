# Beim Testen ist mehr besser

Es mag so aussehen, als würden unsere Tests außer Kontrolle geraten. In diesem Tempo wird es bald mehr Code in unseren Tests geben als in unserer Anwendung, und die Wiederholungen wirken unästhetisch im Vergleich zur eleganten Kürze des restlichen Codes.

**Es spielt keine Rolle**. Lassen Sie sie wachsen. Großteils können Sie einen Test einmal schreiben und dann vergessen. Er wird seine nützliche Funktion weiterhin erfüllen, während Sie Ihr Programm weiterentwickeln.

Manchmal müssen die Tests aktualisiert werden. Nehmen wir an, dass wir unsere Ansichten so ändern, dass nur `Questions` mit `Choices` veröffentlicht werden. In diesem Fall werden viele unserer bestehenden Tests fehlschlagen - **und das sagt uns genau, welche Tests geändert werden müssen, um sie auf dem neuesten Stand zu bringen** - sofern Tests sich in gewisser Weise selber pflegen.

Im schlimmsten Fall können Sie beim weiteren Entwickeln feststellen, dass Sie einige Tests jetzt redundant sind. Auch das ist kein Problem; in der Testwelt ist Redundanz ein **gutes** Ding.

Solange Ihre Tests vernünftig strukturiert sind, werden sie nicht unüberwaltigbar. Gute allgemeine Regeln sind:

- eine separate `TestClass` für jedes Modell oder jede Ansicht
- eine separate Testmethode für jede Bedingung, die Sie testen möchten
- Testmethodennamen, die ihre Funktion beschreiben
