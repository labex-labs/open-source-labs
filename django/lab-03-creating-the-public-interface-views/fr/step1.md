# Présentation

Une vue est un "type" de page web dans votre application Django qui a généralement une fonction spécifique et un modèle spécifique. Par exemple, dans une application de blog, vous pourriez avoir les vues suivantes :

- Page d'accueil du blog - Affiche les dernières entrées.
- Page de "détail" d'une entrée - Page de lien permanent pour une seule entrée.
- Page d'archive par année - Affiche tous les mois avec des entrées dans l'année donnée.
- Page d'archive par mois - Affiche tous les jours avec des entrées dans le mois donné.
- Page d'archive par jour - Affiche toutes les entrées du jour donné.
- Action de commentaire - Gère la publication de commentaires pour une entrée donnée.

Dans notre application de sondage, nous aurons les quatre vues suivantes :

- Page d'"index" des questions - Affiche les dernières questions.
- Page de "détail" des questions - Affiche le texte d'une question, sans résultats mais avec un formulaire pour voter.
- Page des "résultats" des questions - Affiche les résultats pour une question particulière.
- Action de vote - Gère le vote pour un choix particulier dans une question particulière.

Dans Django, les pages web et le reste du contenu sont fournis par les vues. Chaque vue est représentée par une fonction Python (ou une méthode, dans le cas des vues basées sur des classes). Django choisira une vue en examinant l'URL demandée (plus précisément, la partie de l'URL après le nom de domaine).

Maintenant, au fil de vos expériences sur le web, vous avez peut-être croisé des beautés telles que `ME2/Sites/dirmod.htm?sid=&type=gen&mod=Core+Pages&gid=A6CD4967199A42D9B65B1B`. Vous serez ravis de savoir que Django nous permet des modèles d'URL bien plus élégants que ça.

Un modèle d'URL est la forme générale d'une URL - par exemple : `/newsarchive/<year>/<month>/`.

Pour passer d'une URL à une vue, Django utilise ce qu'on appelle des 'URLconf'. Un URLconf associe les modèles d'URL aux vues.

Ce tutoriel fournit des instructions de base sur l'utilisation des URLconf, et vous pouvez vous référer à `/topics/http/urls` pour plus d'informations.
