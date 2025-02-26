# Lecture des attributs avec héritage

Logiquement, le processus de recherche d'un attribut est le suivant. Tout d'abord, vérifiez dans `__dict__` local. Si non trouvé, cherchez dans `__dict__` de la classe. Si non trouvé dans la classe, cherchez dans les classes de base via `__bases__`. Cependant, il y a quelques aspects subtils de ceci qui seront discutés ci-dessous.
