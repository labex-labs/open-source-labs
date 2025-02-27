# Die Ergebnisse analysieren

Wir werden nun die Ergebnisse unserer hierarchischen Clusteranalyse analysieren. Basierend auf den Toy-Datasets, die wir verwendet haben, können wir die folgenden Beobachtungen machen:

- Single Linkage ist schnell und kann bei nicht-kugelförmigen Daten gut funktionieren, ist jedoch bei Vorhandensein von Rauschen schlecht.
- Average und Complete Linkage funktionieren gut bei sauber voneinander getrennten kugelförmigen Clustern, haben jedoch sonst gemischte Ergebnisse.
- Ward ist die effektivste Methode für rauschende Daten.

Es ist wichtig zu beachten, dass diese Beobachtungen uns zwar einige Intuition über die Algorithmen vermitteln, diese Intuition möglicherweise nicht auf sehr hochdimensionale Daten zutrifft.
