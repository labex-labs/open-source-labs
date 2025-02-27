# Choix de compromis du patron d'état

Nous avons montré que Rust est capable d'implémenter le patron d'état orienté objet pour encapsuler les différents types de comportement qu'une publication devrait avoir dans chaque état. Les méthodes sur `Post` ne connaissent rien des différents comportements. Avec la manière dont nous avons organisé le code, il suffit de regarder dans un seul endroit pour connaître les différents comportements d'une publication publiée : l'implémentation du trait `State` sur le struct `Published`.

Si nous créions une implémentation alternative qui n'utiliserait pas le patron d'état, nous pourrions plutôt utiliser des expressions `match` dans les méthodes de `Post` ou même dans le code de `main` qui vérifie l'état de la publication et change le comportement à ces endroits. Cela signifierait que nous devrions regarder dans plusieurs endroits pour comprendre toutes les implications d'une publication étant dans l'état publié! Cela ne ferait qu'augmenter avec le nombre d'états que nous ajouterions : chaque expression `match` aurait besoin d'un autre bras.

Avec le patron d'état, les méthodes de `Post` et les endroits où nous utilisons `Post` n'ont pas besoin d'expressions `match`, et pour ajouter un nouvel état, il suffirait d'ajouter un nouveau struct et d'implémenter les méthodes du trait sur ce seul struct.

L'implémentation utilisant le patron d'état est facile à étendre pour ajouter plus de fonctionnalités. Pour voir la simplicité de la maintenance du code utilisant le patron d'état, essayez quelques-unes de ces suggestions :

- Ajoutez une méthode `reject` qui change l'état de la publication de `PendingReview` en retournant à `Draft`.
- Exigez deux appels à `approve` avant que l'état ne puisse être changé en `Published`.
- Autorisez les utilisateurs à ajouter du contenu textuel seulement lorsqu'une publication est dans l'état `Draft`. Indice : rendez l'objet d'état responsable de ce qui peut changer au sujet du contenu mais pas responsable de modifier `Post`.

Un inconvénient du patron d'état est que, parce que les états implémentent les transitions entre les états, certains des états sont couplés les uns aux autres. Si nous ajoutons un autre état entre `PendingReview` et `Published`, tel que `Scheduled`, nous devrons modifier le code dans `PendingReview` pour passer à `Scheduled` à la place. Il faudrait moins de travail si `PendingReview` n'avait pas besoin de changer avec l'ajout d'un nouvel état, mais cela signifierait passer à un autre patron de conception.

Un autre inconvénient est que nous avons dupliqué une certaine logique. Pour éliminer une partie de la duplication, nous pourrions essayer de créer des implémentations par défaut pour les méthodes `request_review` et `approve` sur le trait `State` qui renvoient `self`. Cependant, cela ne fonctionnerait pas : lorsqu'on utilise `State` comme un objet de trait, le trait ne sait pas exactement quel sera le `self` concret, de sorte que le type de retour n'est pas connu au moment de la compilation.

Une autre duplication inclut les implémentations similaires des méthodes `request_review` et `approve` sur `Post`. Les deux méthodes délèguent à l'implémentation de la même méthode sur la valeur dans le champ `state` de `Option` et définissent la nouvelle valeur du champ `state` sur le résultat. Si nous avions beaucoup de méthodes sur `Post` qui suivaient ce modèle, nous pourrions considérer définir une macro pour éliminer la répétition (voir "Macros").

En implémentant le patron d'état exactement comme il est défini pour les langages orientés objet, nous ne tirons pas pleinement parti des atouts de Rust comme nous le pourrions. Regardons quelques modifications que nous pouvons apporter au crate `blog` qui peuvent transformer les états invalides et les transitions en erreurs de compilation.
