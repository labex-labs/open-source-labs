# Automate la création de branche upstream

En tant que développeur, vous souhaitez automatiser le processus de création de branches upstream lors du push pour éviter la gêne de créer manuellement la branche dans le référentiel distant.

Pour ce laboratoire, vous allez forker le référentiel `https://github.com/labex-labs/git-playground` sur votre compte et utiliser le référentiel `git-playground` de votre compte pour créer automatiquement la branche upstream lors du push.

1. Sur le site web GitHub, connectez-vous à votre compte et trouvez `https://github.com/labex-labs/git-playground` pour forker le référentiel sur votre compte.
2. Sur la page de votre référentiel forké personnel, cliquez sur le bouton `Code` et copiez l'URL du référentiel.
3. Clonez le référentiel, accédez au répertoire et configurez l'identité :

```shell
git clone https://github.com/your-username/git-playground.git
cd git-playground
git config --global user.name "your-username"
git config --global user.email "your-email"
```

4. Utilisez la commande suivante pour activer la création automatique de branche upstream lors du push :

```shell
git config --global push.default current
```

5. Poussez une nouvelle branche appelée `new-feature`, qui n'existe pas dans le référentiel distant :

```shell
git checkout -b new-feature
git push
```

6. Vérifiez que la nouvelle branche a été créée dans le référentiel distant :

```shell
git ls-remote --heads origin
```

Voici le résultat après avoir terminé le laboratoire :

![automatic upstream branch result](../assets/challenge-automatic-push-upstream-step1-1.png)
