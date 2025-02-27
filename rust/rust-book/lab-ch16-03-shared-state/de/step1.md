# Shared-State Concurrency

Message passing ist ein guter Weg, um Concurrency zu handhaben, aber es ist nicht der einzige Weg. Ein anderer Ansatz wäre, dass mehrere Threads auf die gleiche geteilte Daten zugreifen. Betrachten Sie erneut diesen Teil des Slogans aus der Go-Sprachen-Dokumentation: "Kommunizieren Sie nicht, indem Sie Speicher teilen."

Wie würde das Kommandieren durch das Teilen von Speicher aussehen? Darüber hinaus warum würden Unterstützer der Message-Passing-Methode Vorsicht walten lassen, nicht das Speicher teilen zu verwenden?

In gewisser Weise sind Kanäle in jeder Programmiersprache ähnlich wie die einzelne Eigentumsverwaltung, da Sie, nachdem Sie einen Wert über einen Kanal übertragen haben, diesen Wert nicht mehr verwenden sollten. Shared-Memory-Concurrency ist wie die Mehrfach-Eigentumsverwaltung: mehrere Threads können gleichzeitig auf die gleiche Speicheradresse zugreifen. Wie Sie im Kapitel 15 gesehen haben, wo Smart-Pointer die Mehrfach-Eigentumsverwaltung möglich machten, kann die Mehrfach-Eigentumsverwaltung die Komplexität erhöhen, da diese verschiedenen Besitzer verwaltet werden müssen. Rusts Typsystem und die Eigentumsregeln helfen erheblich, um diese Verwaltung richtig zu erledigen. Als Beispiel betrachten wir Mutexe, eines der häufigeren Concurrency-Primitive für Shared Memory.
