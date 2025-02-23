# Le serveur de développement

Vérifions que votre projet Django fonctionne. Si vous ne l'avez pas déjà fait, accédez au répertoire externe `mysite` et exécutez les commandes suivantes :

```bash
cd ~/project/mysite
python manage.py runserver
```

Vous verrez la sortie suivante sur la ligne de commande :

```plaintext
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied. Run 'python manage.py migrate' to apply them.

- 15:50:53 Django version, using settings'mysite.settings' Starting development server at <http://127.0.0.1:8000/> Quit the server with CONTROL-C.
```

Ignorez le message d'avertissement concernant les migrations de base de données non appliquées pour l'instant ; nous en reparlerons bientôt.

Vous avez démarré le serveur de développement Django, un serveur web léger écrit entièrement en Python. Nous l'avons inclus avec Django pour que vous puissiez développer rapidement, sans avoir à vous occuper de la configuration d'un serveur de production - tel qu'Apache - jusqu'à ce que vous soyez prêt pour la production.

C'est le moment de noter : **ne** pas utiliser ce serveur dans un environnement ressemblant à un environnement de production. Il est destiné uniquement à l'utilisation pendant le développement. (Nous sommes dans l'affaire de création de frameworks web, pas de serveurs web.)

Maintenant que le serveur est en cours d'exécution, accédez à <http://127.0.0.1:8000/> avec votre navigateur web. Ou, exécutez `curl 127.0.0.1:8000` dans le terminal. Vous verrez une page "Félicitations!", avec une fusée qui décoll. Ça a fonctionné!

Dans la machine virtuelle LabEx, nous devons ajouter le domaine LabEx à `ALLOWED_HOSTS`. Éditez `mysite/settings.py` et ajoutez `*` à la fin de `ALLOWED_HOSTS`, de sorte qu'il ressemble à ceci :

```python
ALLOWED_HOSTS = ["*"]
```

Cela indique à Django qu'il est autorisé à traiter les requêtes avec n'importe quel en-tête d'hôte.

![Django development server running](../assets/20230907-08-56-33-3uvbOwp3.png)

## Changement du port

Par défaut, la commande `runserver` lance le serveur de développement sur l'adresse IP interne au port 8000.

Si vous voulez changer le port du serveur, passez-le en tant qu'argument de ligne de commande. Par exemple, cette commande lance le serveur sur le port 8080 :

```bash
python manage.py runserver 8080
```

Si vous voulez changer l'adresse IP du serveur, passez-la avec le port. Par exemple, pour écouter sur toutes les adresses IP publiques disponibles (ce qui est utile si vous exécutez Vagrant ou si vous voulez montrer votre travail sur d'autres ordinateurs du réseau), utilisez :

```bash
python manage.py runserver 0.0.0.0:8080
```

Maintenant, basculez sur l'onglet **Web 8080** dans la machine virtuelle LabEx et vous verrez la même page "Félicitations".

![Django development server page](../assets/20230907-08-58-22-M3Luydxk.png)

Les documents complets pour le serveur de développement sont disponibles dans la référence `runserver`.

> Rechargement automatique de `runserver`
> Le serveur de développement recharge automatiquement le code Python pour chaque requête selon les besoins. Vous n'avez pas besoin de redémarrer le serveur pour que les modifications de code prennent effet. Cependant, certaines actions comme l'ajout de fichiers ne déclenchent pas un redémarrage, donc vous devrez redémarrer le serveur dans ces cas.
