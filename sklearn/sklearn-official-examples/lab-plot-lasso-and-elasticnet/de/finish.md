# Zusammenfassung

Es ist bekannt, dass Lasso sparse Daten effektiv wiedergewinnen kann, aber mit stark korrelierten Merkmalen nicht gut abschneidet. Wenn nämlich mehrere korrelierte Merkmale zum Ziel beitragen, wird Lasso schließlich nur eines von ihnen auswählen. Im Falle von dünn besetzten, aber nicht korrelierten Merkmalen wäre ein Lasso-Modell geeignet.

ElasticNet bringt eine gewisse Dünnbesetzung der Koeffizienten ein und reduziert deren Werte auf Null. Somit kann das Modell in Gegenwart von korrelierten Merkmalen, die zum Ziel beitragen, ihre Gewichte reduzieren, ohne sie genau auf Null zu setzen. Dies führt zu einem weniger dünn besetzten Modell als ein reines Lasso und kann auch nicht prädiktive Merkmale erfassen.

ARDRegression ist bei der Behandlung von Gaussian-Rauschen besser, kann aber immer noch nicht mit korrelierten Merkmalen umgehen und erfordert aufgrund der Anpassung eines Priors mehr Zeit.
