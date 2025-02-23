# SHA256 Hashes

Étant donné une chaîne de caractères, calculez son hash SHA256.

## Exigences

- Le programme doit importer les packages `crypto/sha256` et `fmt`.
- Le programme doit utiliser la fonction `sha256.New()` pour créer un nouveau hash.
- Le programme doit utiliser la fonction `Write` pour écrire les octets de la chaîne dans le hash.
- Le programme doit utiliser la fonction `Sum` pour obtenir le résultat de hash finalisé sous forme de tranche d'octets.
- Le programme doit imprimer la chaîne d'origine et le résultat du hash au format hexadécimal.

## Exemple

```sh
# Exécuter le programme calcule le hash et l'imprime
# au format hexadécimal lisible par l'homme.
$ go run sha256-hashes.go
sha256 cette chaîne de caractères
1af1dfa857bf1d8814fe1af8983c18080019922e557f15a8a...

# Vous pouvez calculer d'autres hashs en utilisant un modèle similaire
# à celui montré ci-dessus. Par exemple, pour calculer
# les hashs SHA512, importer `crypto/sha512` et utiliser
# `sha512.New()`.

# Notez que si vous avez besoin de hashs cryptographiquement sécurisés,
# vous devriez soigneusement étudier
# [la force du hash](https://en.wikipedia.org/wiki/Cryptographic_hash_function)!
```
