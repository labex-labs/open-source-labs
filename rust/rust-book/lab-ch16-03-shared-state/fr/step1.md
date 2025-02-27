# Shared-State Concurrency

La communication par message est un bon moyen de gérer la concurrence, mais ce n'est pas le seul. Une autre méthode consisterait à ce que plusieurs threads accèdent aux mêmes données partagées. Considérez encore cette partie de l'affiche de la documentation du langage Go : "Ne communiquez pas en partageant la mémoire."

Quel serait le fait de communiquer en partageant la mémoire? En outre, pourquoi les partisans de la communication par message recommandent-ils de ne pas utiliser le partage de mémoire?

D'une certaine manière, les canaux dans n'importe quel langage de programmation sont similaires à la propriété unique car une fois que vous transférez une valeur dans un canal, vous ne devriez plus utiliser cette valeur. La concurrence en mémoire partagée est comme la propriété multiple : plusieurs threads peuvent accéder au même emplacement mémoire en même temps. Comme vous l'avez vu au chapitre 15, où les pointeurs intelligents ont rendu la propriété multiple possible, la propriété multiple peut ajouter de la complexité car ces différents propriétaires ont besoin d'être gérés. Le système de types et les règles d'appartenance de Rust aident grandement à bien gérer cette opération. Pour un exemple, regardons les mutex, l'un des primitives de concurrence les plus courantes pour la mémoire partagée.
