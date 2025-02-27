# Method Syntax

Les _méthodes_ sont similaires aux fonctions : nous les déclarons avec le mot clé `fn` et un nom, elles peuvent avoir des paramètres et une valeur de retour, et elles contiennent du code qui est exécuté lorsqu'on appelle la méthode depuis un autre endroit. Contrairement aux fonctions, les méthodes sont définies dans le contexte d'un struct (ou d'un enum ou d'un trait object, que nous aborderons respectivement dans le Chapitre 6 et le Chapitre 17), et leur premier paramètre est toujours `self`, qui représente l'instance du struct sur laquelle la méthode est appelée.
