# Tests supplémentaires

Ce tutoriel ne présente que quelques bases du test. Vous pouvez faire beaucoup plus, et disposez d'un certain nombre d'outils très utiles pour réaliser des choses très astucieuses.

Par exemple, alors que nos tests ici ont couvert une partie de la logique interne d'un modèle et la manière dont nos vues publient des informations, vous pouvez utiliser un framework "en navigateur" tel que [Selenium](https://www.selenium.dev/) pour tester la manière dont votre HTML est effectivement affiché dans un navigateur. Ces outils vous permettent de vérifier non seulement le comportement de votre code Django, mais également, par exemple, celui de votre JavaScript. C'est assez incroyable de voir les tests lancer un navigateur et commencer à interagir avec votre site, comme si une personne humaine le pilotait! Django inclut `~django.test.LiveServerTestCase` pour faciliter l'intégration avec des outils comme Selenium.

Si vous avez une application complexe, vous pouvez souhaiter exécuter les tests automatiquement avec chaque commit dans le cadre de la [continuous integration](https://en.wikipedia.org/wiki/Continuous_integration), de sorte que le contrôle de qualité soit lui-même - au moins en partie - automatisée.

Un bon moyen de repérer les parties non testées de votre application est de vérifier la couverture de code. Cela aide également à identifier le code fragile ou même inutilisé. Si vous ne pouvez pas tester un morceau de code, cela signifie généralement que le code devrait être refactorisé ou supprimé. La couverture vous aidera à identifier le code inutilisé. Consultez `topics-testing-code-coverage` pour plus de détails.

`Testing in Django </topics/testing/index>` contient des informations complètes sur les tests.
