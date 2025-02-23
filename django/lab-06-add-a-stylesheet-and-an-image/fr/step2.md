# Ajout d'une image d'arrière-plan

Ensuite, nous allons créer un sous-répertoire pour les images. Créez un sous-répertoire `images` dans le répertoire `polls/static/polls/`. Dans ce répertoire, ajoutez tout fichier image que vous souhaitez utiliser comme arrière-plan. Dans le cadre de ce tutoriel, nous utilisons un fichier nommé `background.png`, que vous pouvez trouver dans le répertoire `/tmp/background.png` de la machine virtuelle.

Vous devez copier `/tmp/background.png` dans `polls/static/polls/images/background.png`.

Ensuite, ajoutez une référence à votre image dans votre feuille de style (`polls/static/polls/style.css`):

```css
body {
  background: white url("images/background.png") no-repeat;
}
```

Rechargez l'onglet **Web 8080** et vous devriez voir l'arrière-plan chargé en haut à gauche de l'écran.

![exemple d'image d'arrière-plan](../assets/20230908-15-39-41-8dGms0NM.png)

> La balise de modèle `{% static %}` n'est pas disponible pour être utilisée dans les fichiers statiques qui ne sont pas générés par Django, comme votre feuille de style. Vous devriez toujours utiliser des **chemins relatifs** pour lier vos fichiers statiques les uns aux autres, car ainsi vous pouvez changer `STATIC_URL` (utilisé par la balise de modèle `static` pour générer ses URL) sans avoir à modifier une multitude de chemins dans vos fichiers statiques également.

Voici les **bases**. Pour plus de détails sur les paramètres et autres éléments inclus dans le cadre, consultez `le guide pratique sur les fichiers statiques </howto/static-files/index>` et `la référence sur les fichiers statiques </ref/contrib/staticfiles>`. `Le déploiement des fichiers statiques </howto/static-files/deployment>` traite de la manière d'utiliser les fichiers statiques sur un serveur réel.

Lorsque vous serez à l'aise avec les fichiers statiques, lisez **Personnalisation du site d'administration de Django** pour apprendre à personnaliser le site d'administration automatiquement généré par Django.
