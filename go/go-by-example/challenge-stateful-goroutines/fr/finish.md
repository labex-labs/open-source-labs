# Sommaire

Ce défi a démontré comment utiliser des canaux et des goroutines pour synchroniser l'accès à un état partagé. En ayant une seule goroutine qui possède l'état et en utilisant des canaux pour émettre des requêtes de lecture et d'écriture, nous pouvons éviter les conditions de course et la corruption des données.
