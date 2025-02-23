# Récapitulatif

Dans ce laboratoire, vous avez créé vos premiers conteneurs Ubuntu, Nginx et MongoDB.

Points clés à retenir

- Les conteneurs sont composés d'espaces de noms Linux et de groupes de contrôle qui assurent l'isolation des autres conteneurs et de l'hôte.
- En raison des propriétés d'isolation des conteneurs, vous pouvez planifier de nombreux conteneurs sur un seul hôte sans vous inquiéter des dépendances conflictuelles. Cela facilite l'exécution de plusieurs conteneurs sur un seul hôte : en utilisant pleinement les ressources allouées à cet hôte et en économisant finalement quelques frais de serveur.
- Évitez d'utiliser du contenu non vérifié du Docker Store lors du développement de vos propres images car ces images peuvent contenir des vulnérabilités de sécurité ou même du logiciel malveillant.
- Les conteneurs incluent tout ce dont ils ont besoin pour exécuter les processus à l'intérieur d'eux, il n'est donc pas nécessaire d'installer des dépendances supplémentaires directement sur votre hôte.
