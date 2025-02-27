# Utiliser les threads pour exécuter du code simultanément

Dans la plupart des systèmes d'exploitation actuels, le code d'un programme exécuté est exécuté dans un _processus_, et le système d'exploitation gérera plusieurs processus en même temps. Dans un programme, vous pouvez également avoir des parties indépendantes qui s'exécutent simultanément. Les fonctionnalités qui exécutent ces parties indépendantes sont appelées _threads_. Par exemple, un serveur web pourrait avoir plusieurs threads de sorte qu'il puisse répondre à plusieurs requêtes en même temps.

Diviser le calcul dans votre programme en plusieurs threads pour exécuter plusieurs tâches en même temps peut améliorer les performances, mais cela ajoute également de la complexité. Parce que les threads peuvent s'exécuter simultanément, il n'y a pas de garantie inhérente sur l'ordre dans lequel les parties de votre code sur différents threads seront exécutées. Cela peut entraîner des problèmes tels que :

- Les conditions de course, où les threads accèdent à des données ou des ressources dans un ordre incohérent
- Les verrous morts, où deux threads s'attendent mutuellement, empêchant les deux threads de continuer
- Des bogues qui ne se produisent que dans certaines situations et sont difficiles à reproduire et à corriger de manière fiable

Rust tente d'atténuer les effets négatifs de l'utilisation de threads, mais la programmation dans un contexte multithreadé nécessite toujours une réflexion attentive et exige une structure de code différente de celle des programmes s'exécutant dans un seul thread.

Les langages de programmation implémentent les threads de quelques manières différentes, et de nombreux systèmes d'exploitation fournissent une API que le langage peut appeler pour créer de nouveaux threads. La bibliothèque standard de Rust utilise un modèle _1:1_ d'implémentation de threads, selon lequel un programme utilise un thread d'exploitation par un thread de langage. Il existe des crânes qui implémentent d'autres modèles de threading qui font des compromis différents par rapport au modèle 1:1.
