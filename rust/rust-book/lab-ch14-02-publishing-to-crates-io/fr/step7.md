# Configuration d'un compte sur crates.io

Avant de pouvoir publier des boîtes à outils (crates), vous devez créer un compte sur *https://crates.io* et obtenir un jeton API. Pour ce faire, accédez à la page d'accueil à *https://crates.io* et connectez-vous via un compte GitHub. (Le compte GitHub est actuellement requis, mais le site pourrait prendre en charge d'autres méthodes de création de compte à l'avenir.) Une fois connecté, accédez à vos paramètres de compte à *https://crates.io/me* et récupérez votre clé API. Ensuite, exécutez la commande `cargo login` avec votre clé API, comme ceci :

```bash
cargo login abcdefghijklmnopqrstuvwxyz012345
```

Cette commande informera Cargo de votre jeton API et le stockera localement dans _\~/.cargo/credentials_. Notez que ce jeton est un _secret_ : ne le partagez avec personne d'autre. Si vous le partagez avec quiconque pour quelque raison que ce soit, vous devriez le révoquer et générer un nouveau jeton sur *https://crates.io*.
