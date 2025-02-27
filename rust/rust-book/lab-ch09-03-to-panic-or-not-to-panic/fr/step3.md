# Cases in Which You Have More Information Than the Compiler

Il serait également approprié d'appeler `unwrap` ou `expect` lorsque vous avez une autre logique qui assure que le `Result` aura une valeur `Ok`, mais la logique n'est pas comprise par le compilateur. Vous aurez toujours une valeur `Result` que vous devrez gérer : quelle que soit l'opération que vous appelez, elle a toujours la possibilité d'échouer en général, même si c'est logiquement impossible dans votre situation particulière. Si vous pouvez vous assurer en inspectant manuellement le code que vous n'aurez jamais une variante `Err`, il est parfaitement acceptable d'appeler `unwrap`, et il est même mieux de documenter la raison pour laquelle vous pensez que vous n'aurez jamais une variante `Err` dans le texte de `expect`. Voici un exemple :

```rust
use std::net::IpAddr;

let home: IpAddr = "127.0.0.1"
 .parse()
 .expect("Hardcoded IP address should be valid");
```

Nous créons une instance `IpAddr` en analysant une chaîne codée en dur. Nous pouvons voir que `127.0.0.1` est une adresse IP valide, il est donc acceptable d'utiliser `expect` ici. Cependant, avoir une chaîne codée en dur et valide ne change pas le type de retour de la méthode `parse` : nous obtenons toujours une valeur `Result`, et le compilateur nous forcera toujours à gérer le `Result` comme si la variante `Err` était une possibilité car le compilateur n'est pas assez intelligent pour voir que cette chaîne est toujours une adresse IP valide. Si la chaîne d'adresse IP provenait d'un utilisateur plutôt que d'être codée en dur dans le programme et avait donc une possibilité d'échec, nous voudrions certainement gérer le `Result` d'une manière plus robuste. Mentionner l'hypothèse que cette adresse IP est codée en dur nous incitera à changer `expect` en un code de gestion d'erreur meilleur si, à l'avenir, nous devons obtenir l'adresse IP à partir d'une autre source.
