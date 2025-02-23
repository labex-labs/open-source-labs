# Résumé

Dans ce défi, nous avons appris comment utiliser des mutex pour accéder en toute sécurité à des données à travers plusieurs goroutines. Nous avons créé une structure `Container` pour stocker une carte de compteurs, et utilisé un `Mutex` pour synchroniser l'accès à la carte `counters`. Nous avons également implémenté une méthode `inc` pour incrémenter le compteur nommé, et utilisé la structure `sync.WaitGroup` pour attendre que les goroutines se terminent. Enfin, nous avons affiché la carte `counters` en utilisant la fonction `fmt.Println`.
