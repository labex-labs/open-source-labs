# Exécution du module

Lorsque l'on importe un module, _toutes les instructions du module s'exécutent_ les unes après les autres jusqu'à la fin du fichier. Le contenu de l'espace de noms du module est tous les noms _globaux_ qui sont encore définis à la fin du processus d'exécution. Si vous avez des instructions de script qui effectuent des tâches dans l'espace de portée globale (affichage, création de fichiers, etc.), vous les verrez s'exécuter lors de l'importation.
