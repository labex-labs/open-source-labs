# En-têtes de sécurité

Les navigateurs reconnaissent divers en-têtes de réponse pour contrôler la sécurité. Il est recommandé de réviser et d'utiliser les en-têtes de sécurité suivants dans votre application Flask :

- HTTP Strict Transport Security (HSTS) : Indique au navigateur de convertir toutes les requêtes HTTP en HTTPS.
- Content Security Policy (CSP) : Spécifie d'où les différents types de ressources peuvent être chargées.
- X-Content-Type-Options : Force le navigateur à respecter le type de contenu de la réponse.
- X-Frame-Options : Empêche les sites externes d'incorporer votre site dans un iframe.

Vous pouvez utiliser l'extension `Flask-Talisman` pour gérer l'HTTPS et les en-têtes de sécurité dans votre application Flask.
