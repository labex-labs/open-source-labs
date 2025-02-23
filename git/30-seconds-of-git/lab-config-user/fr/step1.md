# Configure Git User Information

Vous venez de commencer à travailler sur un nouveau projet et vous voulez configurer vos informations d'utilisateur pour Git. Vous voulez vous assurer que votre nom et votre adresse e-mail sont associés à toutes les modifications que vous apportez au référentiel.

Pour ce laboratoire, nous allons utiliser le référentiel Git nommé `https://github.com/labex-labs/git-playground`. Suivez ces étapes pour configurer vos informations d'utilisateur pour ce référentiel :

1. Clonez le référentiel en utilisant la commande suivante :

```
git clone https://github.com/labex-labs/git-playground.git
```

2. Accédez au référentiel cloné en utilisant la commande suivante :

```
cd git-playground
```

3. Utilisez la commande `git config` pour définir vos informations d'utilisateur pour le référentiel. Par exemple, si votre adresse e-mail est `jane.doe@example.com` et que votre nom est `Jane Doe`, vous utiliseriez les commandes suivantes :

```
git config user.email "jane.doe@example.com"
git config user.name "Jane Doe"
```

4. Vérifiez que vos informations d'utilisateur ont été correctement configurées en utilisant la commande suivante : `git config --list`. Vous devriez voir votre adresse e-mail et votre nom listés respectivement sous les clés `user.email` et `user.name`.

Voici le résultat après avoir terminé le laboratoire :

![Git user configuration result](../assets/challenge-config-user-step1-1.png)
