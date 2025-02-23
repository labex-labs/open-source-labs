# Introduction

Dans ce tutoriel, vous allez apprendre à créer une étiquette d'angle invariant par échelle à l'aide de Matplotlib. L'annotation d'angle est souvent utilisée pour marquer les angles entre des lignes ou à l'intérieur de formes avec un arc circulaire. Bien que Matplotlib fournisse un `~.patches.Arc`, un problème inhérent lorsqu'on l'utilise directement à de telles fins est que l'arc étant circulaire dans l'espace de données n'est pas nécessairement circulaire dans l'espace d'affichage. De plus, le rayon de l'arc est souvent mieux défini dans un système de coordonnées qui est indépendant des coordonnées de données réelles - du moins si vous voulez être en mesure de zoomer librement sur votre graphe sans que l'annotation ne devienne infinie. Cela nécessite une solution où le centre de l'arc est défini dans l'espace de données, mais son rayon en une unité physique comme les points ou les pixels, ou comme un rapport des dimensions de l'Axe.

## Conseils sur la machine virtuelle

Une fois le démarrage de la machine virtuelle terminé, cliquez sur le coin supérieur gauche pour basculer vers l'onglet **Carnet de notes** pour accéder au carnet Jupyter pour pratiquer.

Parfois, vous devrez peut-être attendre quelques secondes pour que le carnet Jupyter ait fini de charger. La validation des opérations ne peut pas être automatisée en raison des limites du carnet Jupyter.

Si vous rencontrez des problèmes pendant l'apprentissage, n'hésitez pas à demander à Labby. Donnez votre feedback après la session, et nous réglerons rapidement le problème pour vous.
