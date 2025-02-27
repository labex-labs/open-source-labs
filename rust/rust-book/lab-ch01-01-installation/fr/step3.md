# Dépannage

Pour vérifier si Rust est correctement installé, ouvrez un **nouveau shell** et entrez cette ligne :

```bash
# Ouvrez d'abord un nouveau terminal!
rustc --version
```

Vous devriez voir le numéro de version, le hachage du commit et la date du commit pour la dernière version stable publiée, au format suivant :

```bash
rustc x.y.z (abcabcabc yyyy-mm-dd)
```

Si vous voyez ces informations, vous avez installé Rust avec succès! Si vous ne voyez pas ces informations, vérifiez que Rust est dans votre variable de système `%PATH%` comme suit.

En Linux, utilisez :

```bash
echo $PATH
```

Si tout est correct et que Rust ne fonctionne toujours pas, il existe de nombreux endroits où vous pouvez obtenir de l'aide. Découvrez comment vous mettre en contact avec d'autres Rustaceens (un surnom amusant que nous nous donnons) sur la page communautaire à l'adresse *https://www.rust-lang.org/community*.
