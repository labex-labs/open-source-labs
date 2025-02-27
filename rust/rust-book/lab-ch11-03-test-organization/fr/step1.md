# Test Organization

Comme mentionné au début du chapitre, le test est une discipline complexe et différents personnes utilisent des terminologies et des organisations différentes. La communauté Rust considère les tests en termes de deux principales catégories : les tests unitaires et les tests d'intégration. Les _tests unitaires_ sont petits et plus axés, testant un module isolément à la fois et peuvent tester les interfaces privées. Les _tests d'intégration_ sont entièrement externes à votre bibliothèque et utilisent votre code de la même manière que n'importe quel autre code externe, en utilisant seulement l'interface publique et en testant potentiellement plusieurs modules par test.

Ecrire les deux types de tests est important pour s'assurer que les parties de votre bibliothèque font ce que vous attendez d'elles, séparément et ensemble.
