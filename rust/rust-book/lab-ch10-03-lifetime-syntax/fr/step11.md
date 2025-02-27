# The Static Lifetime

Une durée de vie spéciale que nous devons discuter est `'static`, qui indique que la référence affectée _peut_ exister pendant toute la durée du programme. Tous les littéraux de chaîne de caractères ont la durée de vie `'static`, que nous pouvons annoter comme suit :

```rust
let s: &'static str = "I have a static lifetime.";
```

Le texte de cette chaîne est stocké directement dans le binaire du programme, qui est toujours disponible. Par conséquent, la durée de vie de tous les littéraux de chaîne de caractères est `'static`.

Vous pouvez voir des suggestions d'utiliser la durée de vie `'static` dans les messages d'erreur. Mais avant de spécifier `'static` comme durée de vie pour une référence, réfléchissez à savoir si la référence que vous avez réellement existe pendant toute la durée de votre programme ou non, et si vous le voulez. Dans la plupart des cas, un message d'erreur suggérant la durée de vie `'static` résulte d'une tentative de créer une référence fausse ou d'un chevauchement des durées de vie disponibles. Dans de tels cas, la solution est de corriger ces problèmes, et non pas de spécifier la durée de vie `'static`.
