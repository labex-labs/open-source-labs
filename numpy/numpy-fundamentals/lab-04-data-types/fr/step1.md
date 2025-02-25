# Comprendre les types de données

NumPy prend en charge une variété de types numériques étroitement liés à ceux du langage de programmation C. Voici quelques-uns des types de données les plus couramment utilisés dans NumPy :

- `numpy.bool_` : Booléen (True ou False) stocké sous forme d'un octet
- `numpy.byte` : Char signé (défini par la plateforme)
- `numpy.ubyte` : Char non signé (défini par la plateforme)
- `numpy.short` : Entier court (défini par la plateforme)
- `numpy.ushort` : Entier court non signé (défini par la plateforme)
- `numpy.intc` : Entier (défini par la plateforme)
- `numpy.uintc` : Entier non signé (défini par la plateforme)
- `numpy.int_` : Long (défini par la plateforme)
- `numpy.uint` : Long non signé (défini par la plateforme)
- `numpy.longlong` : Long long (défini par la plateforme)
- `numpy.ulonglong` : Long long non signé (défini par la plateforme)
- `numpy.half` / `numpy.float16` : Flottant à demi-précision
- `numpy.single` : Flottant à précision simple (défini par la plateforme)
- `numpy.double` : Flottant à double précision (défini par la plateforme)
- `numpy.longdouble` : Flottant à précision étendue (défini par la plateforme)
- `numpy.csingle` : Nombre complexe représenté par deux flottants à précision simple
- `numpy.cdouble` : Nombre complexe représenté par deux flottants à double précision
- `numpy.clongdouble` : Nombre complexe représenté par deux flottants à précision étendue

Ces types de données ont des définitions dépendantes de la plateforme, mais NumPy fournit également des alias de taille fixe pour la commodité.
