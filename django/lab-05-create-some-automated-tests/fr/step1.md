# Présentation des tests automatisés

## Qu'est-ce qu'un test automatisé?

Les tests sont des routines qui vérifient le fonctionnement de votre code.

Les tests sont effectués à différents niveaux. Certains tests peuvent s'appliquer à un détail minuscule (_une méthode de modèle particulière renvoie-t-elle les valeurs attendues?_), tandis que d'autres examinent le fonctionnement global du logiciel (_une séquence d'entrées d'utilisateur sur le site produit-elle le résultat souhaité?_). Cela ne diffère en rien des tests que vous avez effectués plus tôt dans `**Configurer la base de données**`, en utilisant le `shell` pour examiner le comportement d'une méthode, ou en exécutant l'application et en saisissant des données pour vérifier son comportement.

Ce qui est différent dans les tests _automatisés_ est que le travail de test est effectué pour vous par le système. Vous créez une série de tests une fois, puis, lorsque vous apportez des modifications à votre application, vous pouvez vérifier que votre code fonctionne toujours comme vous l'avez initialement prévu, sans avoir à effectuer de tests manuels fastidieux.

## Pourquoi vous devez créer des tests

Alors pourquoi créer des tests, et pourquoi maintenant?

Vous pouvez penser que vous avez déjà assez à faire en apprenant Python/Django, et qu'avoir une autre chose à apprendre et à faire peut sembler écrasant et peut-être inutile. Après tout, notre application de sondages fonctionne parfaitement pour le moment; prendre la peine de créer des tests automatisés ne la fera pas fonctionner mieux. Si la création de l'application de sondages est la dernière partie de la programmation Django que vous allez jamais faire, alors, effectivement, vous n'avez pas besoin de savoir comment créer des tests automatisés. Mais, si ce n'est pas le cas, maintenant est un excellent moment d'apprendre.

### Les tests vous économiseront du temps

Jusqu'à un certain point, "vérifier que cela semble fonctionner" sera un test satisfaisant. Dans une application plus sophistiquée, vous pouvez avoir des dizaines d'interactions complexes entre les composants.

Un changement dans l'un de ces composants pourrait avoir des conséquences inattendues sur le comportement de l'application. Vérifier qu'elle semble toujours fonctionner pourrait signifier parcourir la fonctionnalité de votre code avec vingt variations différentes de vos données de test pour vous assurer que vous n'avez pas cassé quelque chose - pas une bonne utilisation de votre temps.

Cela est particulièrement vrai lorsque des tests automatisés pourraient le faire pour vous en quelques secondes. Si quelque chose ne va pas, les tests vous aideront également à identifier le code qui cause le comportement inattendu.

Parfois, il peut sembler pénible de vous détourner de votre travail de programmation productive et créative pour affronter la tâche fastidieuse et non passionnante d'écrire des tests, en particulier lorsque vous savez que votre code fonctionne correctement.

Cependant, la tâche d'écrire des tests est bien plus gratifiante que de passer des heures à tester manuellement votre application ou à essayer d'identifier la cause d'un problème nouvellement introduit.

### Les tests ne servent pas seulement à identifier les problèmes, ils les préviennent

Il est une erreur de considérer les tests seulement comme un aspect négatif du développement.

Sans tests, le but ou le comportement attendu d'une application peut être assez opaque. Même lorsque c'est votre propre code, vous allez parfois vous retrouver à fouiller dedans pour essayer de comprendre exactement ce qu'il fait.

Les tests changent cela; ils illuminent votre code de l'intérieur, et lorsqu'il y a un problème, ils mettent en lumière la partie qui a rencontré un problème - _même si vous n'avez même pas réalisé qu'il y avait un problème_.

### Les tests rendent votre code plus attrayant

Vous pouvez avoir créé un excellent logiciel, mais vous constaterez que de nombreux autres développeurs refuseront de le regarder car il manque de tests; sans tests, ils ne le feront pas confiance. Jacob Kaplan-Moss, l'un des premiers développeurs de Django, dit : "Le code sans tests est cassé par conception."

Le fait que d'autres développeurs veuillent voir des tests dans votre logiciel avant de le prendre au sérieux est une autre raison pour laquelle vous devriez commencer à écrire des tests.

### Les tests aident les équipes à travailler ensemble

Les points précédents sont écrits du point de vue d'un seul développeur maintenant une application. Les applications complexes seront maintenues par des équipes. Les tests garantissent que vos collègues ne cassent pas accidentellement votre code (et que vous ne le cassiez pas non plus sans le savoir). Si vous voulez gagner votre vie en tant que programmeur Django, vous devez être bon à écrire des tests!
