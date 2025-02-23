# Lorsque l'on teste, plus c'est mieux

Il peut sembler que nos tests prennent de l'ampleur. À ce rythme, il y aura bientôt plus de code dans nos tests que dans notre application, et la répétition est esthétiquement déplaisante, comparativement à la concision élégante du reste de notre code.

**Cela ne compte pas**. Laissez-les grandir. Dans la plupart des cas, vous pouvez écrire un test une fois et puis l'oublier. Il continuera de jouer son rôle utile tandis que vous continuez à développer votre programme.

Parfois, les tests devront être mis à jour. Supposons que nous modifions nos vues de sorte que seules les `Questions` avec des `Choices` soient publiées. Dans ce cas, de nombreux tests existants échoueront - _nous informant exactement quels tests doivent être amendés pour être à jour_, de sorte que dans cette mesure, les tests aident à s'autogérer.

Au pire, au fur et à mesure que vous continuez à développer, vous pouvez constater que vous avez certains tests qui sont maintenant redondants. Même cela n'est pas un problème ; en testant, la redondance est une _bonne_ chose.

Tant que vos tests sont correctement organisés, ils ne deviendront pas impraticables. De bons principes pratiques incluent :

- une `TestClass` séparée pour chaque modèle ou vue
- une méthode de test séparée pour chaque ensemble de conditions que vous voulez tester
- des noms de méthodes de test qui décrivent leur fonction
