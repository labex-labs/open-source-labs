# Écrire des messages d'erreur sur la sortie d'erreur standard au lieu de la sortie standard

À l'heure actuelle, nous écrivons toute notre sortie dans le terminal en utilisant la macro `println!`. Dans la plupart des terminaux, il existe deux types de sortie : la _sortie standard_ (`stdout`) pour les informations générales et la _sortie d'erreur standard_ (`stderr`) pour les messages d'erreur. Cette distinction permet aux utilisateurs de choisir de rediriger la sortie réussie d'un programme vers un fichier tout en imprimant toujours les messages d'erreur sur l'écran.

La macro `println!` est seulement capable d'imprimer sur la sortie standard, donc nous devons utiliser autre chose pour imprimer sur la sortie d'erreur standard.
