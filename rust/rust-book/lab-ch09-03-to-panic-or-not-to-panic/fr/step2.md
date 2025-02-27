# Examples, Prototype Code, and Tests

Lorsque vous écrivez un exemple pour illustrer un concept, inclure également du code de gestion robuste des erreurs peut rendre l'exemple moins clair. Dans les exemples, il est compris qu'un appel à une méthode comme `unwrap` qui peut provoquer une panique est destiné à être un emplacement réservé pour la manière dont vous voudriez que votre application gère les erreurs, ce qui peut différer selon ce que le reste de votre code fait.

De manière similaire, les méthodes `unwrap` et `expect` sont très pratiques lors du prototypage, avant que vous ne soyez prêt à décider de la manière de gérer les erreurs. Elles laissent des marqueurs clairs dans votre code pour le moment où vous êtes prêt à rendre votre programme plus robuste.

Si un appel de méthode échoue dans un test, vous voudriez que tout le test échoue, même si cette méthode n'est pas la fonctionnalité testée. Parce que `panic!` est la manière dont un test est marqué comme un échec, appeler `unwrap` ou `expect` est exactement ce qui devrait se produire.
