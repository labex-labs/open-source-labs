# Résumé

Dans ce laboratoire, vous avez commencé à ajouter de la valeur en créant vos propres conteneurs Docker personnalisés.

Idées clés :

- Le Dockerfile est la manière dont vous créez des builds reproductibles pour votre application et la manière dont vous intégrez votre application avec Docker dans le pipeline CI/CD.
- Les images Docker peuvent être rendues disponibles pour tous vos environnements grâce à un registre central. Docker Hub est un exemple de registre, mais vous pouvez déployer votre propre registre sur des serveurs que vous contrôlez.
- Les images Docker contiennent toutes les dépendances dont elles ont besoin pour exécuter une application à l'intérieur de l'image. Cela est pratique car nous n'avons plus à gérer la dérive d'environnement (différences de versions) lorsque nous dépendons de dépendances installées sur chaque environnement dans lequel nous déployons.
- Docker utilise le système de fichiers union et le "copier lors de l'écriture" pour réutiliser les couches d'images. Cela réduit l'occupation mémoire de stockage des images et augmente considérablement les performances du lancement de conteneurs.
- Les couches d'image sont mises en cache par le système de build et de poussée Docker. Il n'est pas nécessaire de reconstruire ou de repousser les couches d'image déjà présentes sur le système souhaité.
- Chaque ligne dans un Dockerfile crée une nouvelle couche, et en raison du cache de couche, les lignes qui changent plus fréquemment (par exemple, ajout de code source à une image) devraient être listées près du bas du fichier.
