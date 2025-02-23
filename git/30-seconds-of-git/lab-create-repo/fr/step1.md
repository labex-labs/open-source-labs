# Créer un nouveau référentiel

Nous avons appris à cloner un référentiel Git existant. Maintenant, créons un nouveau référentiel Git de zéro.

Ouvrez votre terminal ou invite de commandes et suivez les étapes ci-dessous pour créer un nouveau référentiel Git :

```bash
cd ~/projet
git init mon_repo
```

Cela créera un nouveau répertoire nommé `mon_repo` dans votre répertoire de travail actuel et initialisera un nouveau référentiel Git à l'intérieur.

Voyons ce qui se trouve dans le répertoire `mon_repo` :

```bash
ls -a mon_repo
```

Vous devriez voir les fichiers et répertoires suivants :

```plaintext
. .. .git
```

Les répertoires `.` et `..` sont des répertoires spéciaux qui représentent respectivement le répertoire actuel et le répertoire parent.

Le répertoire `.git` est celui où Git stocke tous les fichiers de configuration et l'historique des versions du référentiel.

Essayez d'exécuter la commande suivante pour voir les fichiers et répertoires à l'intérieur du répertoire `.git` :

```bash
ls -a mon_repo/.git
```

Vous devriez voir les fichiers et répertoires suivants :

```plaintext
. ..  branches  config  description  HEAD  hooks  info  objets  ref
```

- Le répertoire `branches` contient des références aux branches du référentiel.
- Le fichier `config` contient les paramètres de configuration spécifiques au référentiel.
- Le fichier `description` contient une courte description du référentiel.
- Le fichier `HEAD` contient une référence à la branche actuellement sélectionnée.
- Le répertoire `hooks` contient des scripts qui peuvent être déclenchés par des événements Git.
- Le répertoire `info` contient des fichiers d'informations globales.
- Le répertoire `objets` contient tous les objets du référentiel.
- Le répertoire `ref` contient des références aux commits du référentiel.

Nous n'avons pas besoin de nous soucier du contenu du répertoire `.git` pour l'instant. Rappelez-vous simplement que c'est là que Git stocke toutes les informations sur le référentiel.
