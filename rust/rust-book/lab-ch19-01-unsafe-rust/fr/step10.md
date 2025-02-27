# Quand utiliser du code non sécurisé

Utiliser `unsafe` pour utiliser l'un des cinq pouvoirs surnaturels que nous venons de discuter n'est pas une erreur et n'est même pas déconseillé, mais il est plus difficile de corriger le code `unsafe` car le compilateur ne peut pas aider à maintenir la sécurité mémoire. Lorsque vous avez une raison d'utiliser du code `unsafe`, vous pouvez le faire, et avoir l'annotation `unsafe` explicite facilite la localisation de la source des problèmes lorsqu'ils se produisent.
