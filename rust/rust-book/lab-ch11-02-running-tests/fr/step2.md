# Exécuter les tests en parallèle ou séquentiellement

Lorsque vous exécutez plusieurs tests, par défaut, ils s'exécutent en parallèle à l'aide de threads, ce qui signifie qu'ils se terminent plus rapidement et que vous obtenez des réponses plus rapidement. Étant donné que les tests s'exécutent en même temps, vous devez vous assurer que vos tests ne dépendent pas les uns des autres ou d'un état partagé, y compris un environnement partagé, tel que le répertoire de travail actuel ou les variables d'environnement.

Par exemple, supposons que chacun de vos tests exécute du code qui crée un fichier sur le disque nommé _test-output.txt_ et écrit des données dans ce fichier. Ensuite, chaque test lit les données dans ce fichier et affirme que le fichier contient une valeur particulière, qui est différente pour chaque test. Étant donné que les tests s'exécutent en même temps, un test peut écraser le fichier entre l'écriture et la lecture d'un autre test. Le second test échouera donc, non pas parce que le code est incorrect, mais parce que les tests se sont interférés lors de leur exécution en parallèle. Une solution est de vous assurer que chaque test écrit dans un fichier différent ; une autre solution est d'exécuter les tests un par un.

Si vous ne voulez pas exécuter les tests en parallèle ou si vous voulez un contrôle plus fin sur le nombre de threads utilisés, vous pouvez envoyer le drapeau `--test-threads` et le nombre de threads que vous voulez utiliser au binaire de test. Voici un exemple :

```bash
cargo test -- --test-threads=1
```

Nous avons défini le nombre de threads de test sur `1`, ce qui indique au programme de ne pas utiliser de parallélisme. Exécuter les tests avec un seul thread prendra plus de temps que les exécuter en parallèle, mais les tests ne se interféreront pas s'ils partagent un état.
