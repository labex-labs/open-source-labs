# Présentation de l'administrateur Django

Générer des sites d'administration pour votre personnel ou vos clients afin qu'ils puissent ajouter, modifier et supprimer du contenu est un travail fastidieux qui ne nécessite pas beaucoup de créativité. Pour cette raison, Django automatise entièrement la création d'interfaces d'administration pour les modèles.

Django a été écrit dans un environnement de rédaction d'actualités, avec une séparation très claire entre les "éditeurs de contenu" et le site "public". Les gestionnaires de site utilisent le système pour ajouter des articles d'actualité, des événements, des scores sportifs, etc., et ce contenu est affiché sur le site public. Django résout le problème de la création d'une interface unifiée pour les administrateurs de site pour éditer le contenu.

L'administrateur n'est pas destiné à être utilisé par les visiteurs du site. C'est pour les gestionnaires de site.

## Création d'un utilisateur administrateur

Tout d'abord, nous devons créer un utilisateur qui peut se connecter au site d'administration. Exécutez la commande suivante :

```bash
python manage.py createsuperuser
```

Entrez le nom d'utilisateur souhaité et appuyez sur Entrée.

```plaintext
Nom d'utilisateur : admin
```

Vous serez ensuite invité à entrer votre adresse e-mail souhaitée :

```plaintext
Adresse e-mail : admin@example.com
```

La dernière étape est d'entrer votre mot de passe. Vous devrez entrer votre mot de passe deux fois, la deuxième fois comme confirmation de la première.

```plaintext
Mot de passe : 12345678
Confirmez le mot de passe : 12345678

Ce mot de passe est trop courant.
Ce mot de passe est entièrement numérique.
Bypasser la validation du mot de passe et créer l'utilisateur malgré tout? [y/N] : y
Superutilisateur créé avec succès.
```

## Démarrer le serveur de développement

Le site d'administration Django est activé par défaut. Démarrons le serveur de développement et explorons-le.

Si le serveur n'est pas en cours d'exécution, démarrez-le comme ceci :

```bash
python manage.py runserver
```

Maintenant, ouvrez un navigateur web dans l'onglet **VNC** et accédez à "/admin/" sur votre domaine local - par exemple, `http://127.0.0.1:8000/admin/`. Vous devriez voir l'écran de connexion de l'administrateur :

![Écran de connexion de l'administrateur Django](../assets/20230907-14-31-50-SvkJF8K8.png)

Depuis que la `traduction </topics/i18n/translation>` est activée par défaut, si vous définissez `LANGUAGE_CODE`, l'écran de connexion sera affiché dans la langue donnée (si Django dispose de traductions appropriées).

## Entrer dans le site d'administration

Maintenant, essayez de vous connecter avec le compte de superutilisateur que vous avez créé dans l'étape précédente. Vous devriez voir la page d'accueil de l'administrateur Django :

![Page d'accueil de l'administrateur Django](../assets/admin02.png)

Vous devriez voir quelques types de contenu éditable : groupes et utilisateurs. Ils sont fournis par `django.contrib.auth`, le cadre d'authentification fourni par Django.

## Rendre l'application de sondage modifiable dans l'administrateur

Mais où est notre application de sondage? Elle n'est pas affichée sur la page d'accueil de l'administrateur.

Il ne reste plus qu'une chose à faire : nous devons dire à l'administrateur que les objets `Question` ont une interface d'administration. Pour ce faire, ouvrez le fichier `polls/admin.py` et modifiez-le pour qu'il ressemble à ceci :

```python
from django.contrib import admin

from.models import Question

admin.site.register(Question)
```

## Explorer la fonctionnalité d'administrateur gratuite

Maintenant que nous avons enregistré `Question`, Django sait qu'elle devrait être affichée sur la page d'accueil de l'administrateur :

![Page d'accueil de l'administrateur Django, maintenant avec les sondages affichés](../assets/admin03t.png)

Cliquez sur "Questions". Maintenant, vous êtes sur la page de "liste de modification" des questions. Cette page affiche toutes les questions dans la base de données et vous permet de choisir une pour la modifier. Il y a la question "Quoi de neuf?" que nous avons créée plus tôt :

![Page de liste de modification des sondages](../assets/admin04t.png)

Cliquez sur la question "Quoi de neuf?" pour l'éditer :

![Édition d'une question de sondage](../assets/20230907-14-33-49-XWeEgAXl.png)

Points à noter ici :

- Le formulaire est automatiquement généré à partir du modèle `Question`.
- Les différents types de champs de modèle (`~django.db.models.DateTimeField`, `~django.db.models.CharField`) correspondent au widget d'entrée HTML approprié. Chaque type de champ sait comment s'afficher dans l'administrateur Django.
- Chaque `~django.db.models.DateTimeField` bénéficie de raccourcis JavaScript gratuits. Les dates ont un raccourci "Aujourd'hui" et une fenêtre contextuelle de calendrier, et les heures ont un raccourci "Maintenant" et une fenêtre contextuelle pratique qui liste les heures couramment entrées.

La partie inférieure de la page vous offre quelques options :

- Enregistrer - Enregistre les modifications et revient à la page de liste de modification de ce type d'objet.
- Enregistrer et continuer l'édition - Enregistre les modifications et recharge la page d'administrateur de cet objet.
- Enregistrer et ajouter un autre - Enregistre les modifications et charge un nouveau formulaire vide de ce type d'objet.
- Supprimer - Affiche une page de confirmation de suppression.

Si la valeur de "Date publiée" ne correspond pas à l'heure à laquelle vous avez créé la question dans **Création d'une application de sondage de base**, cela signifie probablement que vous avez oublié de définir la valeur correcte pour la configuration `TIME_ZONE`. Changez-la, rechargez la page et vérifiez que la valeur correcte apparaît.

Changez la "Date publiée" en cliquant sur les raccourcis "Aujourd'hui" et "Maintenant". Ensuite, cliquez sur "Enregistrer et continuer l'édition". Ensuite, cliquez sur "Histoire" dans le coin supérieur droit. Vous verrez une page listant toutes les modifications apportées à cet objet via l'administrateur Django, avec le horodatage et le nom d'utilisateur de la personne qui a effectué la modification :

![Page d'historique de l'objet question](../assets/admin06t.png)

Lorsque vous serez à l'aise avec l'API des modèles et que vous vous serez familiarisé avec le site d'administrateur, lisez **Création des vues d'interface publique** pour en savoir plus sur la manière d'ajouter plus de vues à notre application de sondages.
