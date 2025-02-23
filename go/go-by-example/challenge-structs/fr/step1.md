# Structs

Dans ce défi, vous devez compléter la fonction `newPerson` qui construit un nouveau struct `person` avec le nom donné. Le type de struct `person` a les champs `name` et `age`.

## Exigences

- Le type de struct `person` doit avoir les champs `name` et `age`.
- La fonction `newPerson` doit construire un nouveau struct `person` avec le nom donné.
- La fonction `newPerson` doit retourner un pointeur vers le nouveau struct `person` créé.
- La fonction `main` doit afficher ce qui suit :
  - Un nouveau struct avec le nom "Bob" et l'âge 20.
  - Un nouveau struct avec le nom "Alice" et l'âge 30.
  - Un nouveau struct avec le nom "Fred" et l'âge 0.
  - Un pointeur vers un nouveau struct avec le nom "Ann" et l'âge 40.
  - Un nouveau struct construit à l'aide de la fonction `newPerson` avec le nom "Jon" et l'âge 42.
  - Le champ `name` d'un struct avec le nom "Sean" et l'âge 50.
  - Le champ `age` d'un pointeur de struct vers un struct avec le nom "Sean" et l'âge 50.
  - Le champ `age` d'un pointeur de struct vers un struct avec le nom "Sean" et l'âge 50 après que le champ `age` ait été mis à jour à 51.

## Exemple

```sh
$ go run structs.go
{Bob 20}
{Alice 30}
{Fred 0}
&{Ann 40}
&{Jon 42}
Sean
50
51
```
