# Configuration de la base de données

Maintenant, ouvrez `mysite/settings.py`. C'est un module Python normal avec des variables de niveau de module représentant les paramètres de Django.

Par défaut, la configuration utilise SQLite. Si vous êtes nouveau dans le domaine des bases de données, ou si vous êtes simplement intéressé par l'essai de Django, c'est le choix le plus simple. SQLite est inclus dans Python, donc vous n'aurez pas besoin d'installer autre chose pour prendre en charge votre base de données. Cependant, lorsqu'il s'agit de démarrer votre premier projet réel, vous souhaiterez peut-être utiliser une base de données plus scalable comme PostgreSQL, pour éviter les problèmes de changement de base de données plus tard.

Si vous souhaitez utiliser une autre base de données, installez les `liaisons de base de données appropriées <installation-de-base-de-donnees>` et modifiez les clés suivantes dans l'élément `'default'` de `DATABASES` pour correspondre à vos paramètres de connexion à la base de données :

- `ENGINE <MOTEUR-DE-BASE-DE-DONNEES>` -- Soit `'django.db.backends.sqlite3'`, `'django.db.backends.postgresql'`, `'django.db.backends.mysql'`, ou `'django.db.backends.oracle'`. D'autres backends sont `également disponibles
<notes-sur-les-tiers>`.
- `NAME` -- Le nom de votre base de données. Si vous utilisez SQLite, la base de données sera un fichier sur votre ordinateur ; dans ce cas, `NAME` devrait être le chemin absolu complet, y compris le nom de fichier, de ce fichier. La valeur par défaut, `BASE_DIR / 'db.sqlite3'`, stockera le fichier dans votre répertoire de projet.

Si vous n'utilisez pas SQLite comme base de données, des paramètres supplémentaires tels que `USER`, `PASSWORD` et `HOST` doivent être ajoutés. Pour plus de détails, consultez la documentation de référence pour `DATABASES`.

> Pour les bases de données autres que SQLite

Si vous utilisez une base de données autre que SQLite, assurez-vous d'avoir créé une base de données à ce stade. Faites-le avec "`CREATE DATABASE database_name;`" dans l'invite interactive de votre base de données.

Vérifiez également que l'utilisateur de base de données fourni dans `mysite/settings.py` a les privilèges "créer une base de données". Cela permet la création automatique d'une `base de données de test <la-base-de-donnees-de-test>` qui sera nécessaire dans un tutoriel ultérieur.

Si vous utilisez SQLite, vous n'avez pas besoin de créer quoi que ce soit à l'avance - le fichier de base de données sera créé automatiquement lorsqu'il est nécessaire.

Pendant que vous éditez `mysite/settings.py`, définissez `TIME_ZONE` sur votre fuseau horaire.

Notez également la configuration `INSTALLED_APPS` en haut du fichier. Elle contient les noms de toutes les applications Django qui sont activées dans cette instance de Django. Les applications peuvent être utilisées dans plusieurs projets, et vous pouvez les emballer et les distribuer pour qu'autrui les utilise dans leurs projets.

Par défaut, `INSTALLED_APPS` contient les applications suivantes, toutes fournies avec Django :

- `django.contrib.admin` -- Le site d'administration. Vous l'utiliserez bientôt.
- `django.contrib.auth` -- Un système d'authentification.
- `django.contrib.contenttypes` -- Un cadre pour les types de contenu.
- `django.contrib.sessions` -- Un cadre de sessions.
- `django.contrib.messages` -- Un cadre de messagerie.
- `django.contrib.staticfiles` -- Un cadre pour la gestion des fichiers statiques.

Ces applications sont incluses par défaut pour la commodité du cas général.

Certaines de ces applications utilisent au moins une table de base de données, donc nous devons créer les tables dans la base de données avant de pouvoir les utiliser. Pour cela, exécutez la commande suivante :

```bash
cd ~/project/mysite
python manage.py migrate
```

```plaintext
Opérations à effectuer :
  Appliquer toutes les migrations : admin, auth, contenttypes, sessions
Exécution des migrations :
  Appliquer contenttypes.0001_initial... OK
  Appliquer auth.0001_initial... OK
  Appliquer admin.0001_initial... OK
  Appliquer admin.0002_logentry_remove_auto_add... OK
  Appliquer admin.0003_logentry_add_action_flag_choices... OK
  Appliquer contenttypes.0002_remove_content_type_name... OK
  Appliquer auth.0002_alter_permission_name_max_length... OK
  Appliquer auth.0003_alter_user_email_max_length... OK
  Appliquer auth.0004_alter_user_username_opts... OK
  Appliquer auth.0005_alter_user_last_login_null... OK
  Appliquer auth.0006_require_contenttypes_0002... OK
  Appliquer auth.0007_alter_validators_add_error_messages... OK
  Appliquer auth.0008_alter_user_username_max_length... OK
  Appliquer auth.0009_alter_user_last_name_max_length... OK
  Appliquer auth.0010_alter_group_name_max_length... OK
  Appliquer auth.0011_update_proxy_permissions... OK
  Appliquer auth.0012_alter_user_first_name_max_length... OK
  Appliquer sessions.0001_initial... OK
```

La commande `migrate` examine la configuration `INSTALLED_APPS` et crée toutes les tables de base de données nécessaires selon les paramètres de base de données dans votre fichier `mysite/settings.py` et les migrations de base de données fournies avec l'application (nous aborderons cela plus tard). Vous verrez un message pour chaque migration qu'elle applique. Si vous êtes intéressé, exécutez le client de ligne de commande de votre base de données et tapez `\dt` (PostgreSQL), `SHOW TABLES;` (MariaDB, MySQL), `.tables` (SQLite) ou `SELECT TABLE_NAME FROM USER_TABLES;` (Oracle) pour afficher les tables créées par Django.

> Pour les minimalistes

Comme nous l'avons dit ci-dessus, les applications par défaut sont incluses pour le cas général, mais pas tout le monde en a besoin. Si vous n'en avez pas besoin ou que vous n'en avez besoin que partiellement, n'hésitez pas à commenter ou à supprimer la ligne appropriée de `INSTALLED_APPS` avant d'exécuter `migrate`. La commande `migrate` ne lancera que les migrations pour les applications dans `INSTALLED_APPS`.
