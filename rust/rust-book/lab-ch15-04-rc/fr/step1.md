# Rc`<T>`{=html}, le pointeur intelligent à comptage de références

Dans la majorité des cas, la propriété est claire : vous savez exactement quelle variable possède une valeur donnée. Cependant, il existe des cas où une seule valeur peut avoir plusieurs propriétaires. Par exemple, dans les structures de données de graphe, plusieurs arêtes peuvent pointer vers le même nœud, et ce nœud est conceptuellement propriété de toutes les arêtes qui le pointent. Un nœud ne devrait pas être nettoyé à moins qu'il n'ait aucune arête qui le pointe et donc qu'il n'ait aucun propriétaire.

Vous devez activer l'appartenance multiple explicitement en utilisant le type Rust `Rc<T>`, qui est une abréviation de _comptage de références_. Le type `Rc<T>` suit le nombre de références à une valeur pour déterminer si la valeur est encore en usage. Si le nombre de références à une valeur est égal à zéro, la valeur peut être nettoyée sans que les références deviennent invalides.

Imaginez `Rc<T>` comme une télévision dans une salle de séjour. Quand une personne entre pour regarder la télévision, elle l'allume. D'autres peuvent entrer dans la pièce et regarder la télévision. Quand la dernière personne quitte la pièce, elle éteint la télévision car elle n'est plus utilisée. Si quelqu'un éteint la télévision tandis que d'autres sont encore en train de la regarder, il y aurait un tollé des autres téléspectateurs!

Nous utilisons le type `Rc<T>` lorsque nous voulons allouer des données sur le tas pour que plusieurs parties de notre programme puissent les lire et que nous ne puissions pas déterminer à la compilation laquelle des parties utilisera les données en dernier. Si nous savions laquelle des parties terminerait en dernier, nous pourrions simplement rendre cette partie propriétaire des données, et les règles normales de propriété appliquées à la compilation entreraient en vigueur.

Notez que `Rc<T>` n'est destiné qu'à être utilisé dans des scénarios mono-fil. Lorsque nous aborderons la concurrence au chapitre 16, nous verrons comment effectuer le comptage de références dans les programmes multithreadés.
