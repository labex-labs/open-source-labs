# Opérations de manipulation binaire

## Problème

Implémentez les opérations courantes de manipulation binaire suivantes en Python :

- `get_bit` : Étant donné un nombre et un index, renvoyez la valeur du bit à l'index donné.
- `set_bit` : Étant donné un nombre et un index, définissez la valeur du bit à l'index donné sur 1.
- `clear_bit` : Étant donné un nombre et un index, définissez la valeur du bit à l'index donné sur 0.
- `clear_bits_msb_to_index` : Étant donné un nombre et un index, définissez tous les bits depuis le bit de poids fort jusqu'à l'index donné sur 0.
- `clear_bits_index_to_lsb` : Étant donné un nombre et un index, définissez tous les bits depuis l'index donné jusqu'au bit de poids faible sur 0.
- `update_bit` : Étant donné un nombre, un index et une valeur, mettez à jour la valeur du bit à l'index donné avec la valeur donnée.

## Exigences

L'implémentation doit répondre aux exigences suivantes :

- Les entrées peuvent ne pas être valides, et l'implémentation doit gérer de telles situations de manière appropriée.
- L'implémentation doit être mémoire-économique.

## Utilisation exemple

Voici quelques exemples d'utilisation des fonctions implémentées :

- `get_bit` :
  ```
  number   = 0b10001110
  index = 3
  expected = True
  ```
- `set_bit` :
  ```
  number   = 0b10001110
  index = 4
  expected = 0b10011110
  ```
- `clear_bit` :
  ```
  number   = 0b10001110
  index = 3
  expected = 0b10000110
  ```
- `clear_bits_msb_to_index` :
  ```
  number   = 0b10001110
  index = 3
  expected = 0b00000110
  ```
- `clear_bits_index_to_lsb` :
  ```
  number   = 0b10001110
  index = 3
  expected = 0b10000000
  ```
- `update_bit` :

  ```
  number   = 0b10001110
  index = 3
  value = 1
  expected = 0b10001110

  number   = 0b10001110
  index = 3
  value = 0
  expected = 0b10000110

  number   = 0b10001110
  index = 0
  value = 1
  expected = 0b10001111
  ```
