# Un cas d'utilisation de la mutabilité interne : Les objets de mock

Parfois, lors des tests, un programmeur utilisera un type à la place d'un autre type, afin d'observer un comportement particulier et d'affirmer qu'il est correctement implémenté. Ce type de substitut est appelé un **doublon de test**. Pensez à cela comme un double de tournage dans le cinéma, où une personne prend la place d'un acteur pour réaliser une scène particulièrement difficile. Les doubles de test prennent la place d'autres types lorsque nous exécutons des tests. Les **objets de mock** sont des types spécifiques de doubles de test qui enregistrent ce qui se passe pendant un test, afin que vous puissiez affirmer que les bonnes actions ont eu lieu.

Rust n'a pas d'objets au sens où d'autres langages les ont, et Rust n'a pas de fonctionnalité d'objet de mock intégrée dans la bibliothèque standard comme certains autres langages le font. Cependant, vous pouvez certainement créer une structure qui servira les mêmes buts qu'un objet de mock.

Voici le scénario que nous allons tester : nous allons créer une bibliothèque qui suit une valeur par rapport à une valeur maximale et envoie des messages en fonction de la proximité de la valeur maximale de la valeur actuelle. Cette bibliothèque pourrait être utilisée pour suivre le quota d'un utilisateur pour le nombre d'appels API qu'il est autorisé à effectuer, par exemple.

Notre bibliothèque ne fournira que la fonctionnalité de suivre à quel point une valeur est proche de la valeur maximale et quels messages devraient être envoyés à quels moments. Les applications qui utilisent notre bibliothèque devront fournir le mécanisme d'envoi des messages : l'application pourrait placer un message dans l'application, envoyer un courrier électronique, envoyer un message texte ou faire autre chose. La bibliothèque n'a pas besoin de connaître ces détails. Tout ce qu'elle a besoin, c'est de quelque chose qui implémente un trait que nous allons fournir appelé `Messenger`. La liste 15-20 montre le code de la bibliothèque.

Nom de fichier : `src/lib.rs`

```rust
pub trait Messenger {
  1 fn send(&self, msg: &str);
}

pub struct LimitTracker<'a, T: Messenger> {
    messenger: &'a T,
    value: usize,
    max: usize,
}

impl<'a, T> LimitTracker<'a, T>
where
    T: Messenger,
{
    pub fn new(
        messenger: &'a T,
        max: usize
    ) -> LimitTracker<'a, T> {
        LimitTracker {
            messenger,
            value: 0,
            max,
        }
    }

  2 pub fn set_value(&mut self, value: usize) {
        self.value = value;

        let percentage_of_max =
            self.value as f64 / self.max as f64;

        if percentage_of_max >= 1.0 {
            self.messenger
             .send("Error: You are over your quota!");
        } else if percentage_of_max >= 0.9 {
            self.messenger
             .send("Urgent: You're at 90% of your quota!");
        } else if percentage_of_max >= 0.75 {
            self.messenger
             .send("Warning: You're at 75% of your quota!");
        }
    }
}
```

Liste 15-20 : Une bibliothèque pour suivre à quel point une valeur est proche d'une valeur maximale et avertir lorsqu'elle atteint certains niveaux

Une partie importante de ce code est que le trait `Messenger` a une méthode appelée `send` qui prend une référence immuable à `self` et le texte du message \[1\]. Ce trait est l'interface que notre objet de mock doit implémenter pour que le mock puisse être utilisé de la même manière qu'un objet réel. L'autre partie importante est que nous voulons tester le comportement de la méthode `set_value` sur le `LimitTracker` \[2\]. Nous pouvons changer ce que nous passons pour le paramètre `value`, mais `set_value` ne renvoie rien pour que nous puissions formuler des assertions. Nous voulons être en mesure de dire que si nous créons un `LimitTracker` avec quelque chose qui implémente le trait `Messenger` et une valeur particulière pour `max`, lorsque nous passons différents nombres pour `value`, le messager est invité à envoyer les messages appropriés.

Nous avons besoin d'un objet de mock qui, au lieu d'envoyer un courrier électronique ou un message texte lorsque nous appelons `send`, ne fera que suivre les messages qu'il est invité à envoyer. Nous pouvons créer une nouvelle instance de l'objet de mock, créer un `LimitTracker` qui utilise l'objet de mock, appeler la méthode `set_value` sur `LimitTracker`, puis vérifier que l'objet de mock a les messages que nous attendons. La liste 15-21 montre une tentative d'implémenter un objet de mock pour faire exactement cela, mais l'analyseur d'emprunt ne le permettra pas.

Nom de fichier : `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

  1 struct MockMessenger {
      2 sent_messages: Vec<String>,
    }

    impl MockMessenger {
      3 fn new() -> MockMessenger {
            MockMessenger {
                sent_messages: vec![],
            }
        }
    }

  4 impl Messenger for MockMessenger {
        fn send(&self, message: &str) {
          5 self.sent_messages.push(String::from(message));
        }
    }

    #[test]
  6 fn it_sends_an_over_75_percent_warning_message() {
        let mock_messenger = MockMessenger::new();
        let mut limit_tracker = LimitTracker::new(
            &mock_messenger,
            100
        );

        limit_tracker.set_value(80);

        assert_eq!(mock_messenger.sent_messages.len(), 1);
    }
}
```

Liste 15-21 : Une tentative d'implémenter un `MockMessenger` qui n'est pas autorisé par l'analyseur d'emprunt

Ce code de test définit une structure `MockMessenger` \[1\] qui a un champ `sent_messages` avec un `Vec` de valeurs `String` \[2\] pour suivre les messages qu'il est invité à envoyer. Nous définissons également une fonction associée `new` \[3\] pour faciliter la création de nouvelles valeurs `MockMessenger` qui commencent avec une liste vide de messages. Nous implémentons ensuite le trait `Messenger` pour `MockMessenger` \[4\] afin que nous puissions fournir un `MockMessenger` à un `LimitTracker`. Dans la définition de la méthode `send` \[5\], nous prenons le message passé en tant que paramètre et le stockons dans la liste `sent_messages` de `MockMessenger`.

Dans le test, nous testons ce qui se passe lorsque le `LimitTracker` est invité à définir `value` sur une valeur supérieure à 75 % de la valeur `max` \[6\]. Tout d'abord, nous créons un nouveau `MockMessenger`, qui commencera avec une liste vide de messages. Ensuite, nous créons un nouveau `LimitTracker` et lui donnons une référence au nouveau `MockMessenger` et une valeur `max` de `100`. Nous appelons la méthode `set_value` sur le `LimitTracker` avec une valeur de `80`, qui est supérieure à 75 % de 100. Ensuite, nous affirmons que la liste de messages que le `MockMessenger` suit devrait maintenant avoir un message.

Cependant, il y a un problème avec ce test, comme le montre ici :

```bash
error[E0596]: cannot borrow `self.sent_messages` as mutable, as it is behind a
`&` reference
  --> src/lib.rs:58:13
   |
2  |     fn send(&self, msg: &str);
   |             ----- help: consider changing that to be a mutable reference:
`&mut self`
...
58 |             self.sent_messages.push(String::from(message));
   |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ `self` is a
`&` reference, so the data it refers to cannot be borrowed as mutable
```

Nous ne pouvons pas modifier le `MockMessenger` pour suivre les messages car la méthode `send` prend une référence immuable à `self`. Nous ne pouvons pas non plus suivre la suggestion du message d'erreur d'utiliser `&mut self` à la place car alors, la signature de `send` ne correspondrait pas à la signature dans la définition du trait `Messenger` (n'hésitez pas à essayer et à voir quel message d'erreur vous obtenez).

C'est une situation où la mutabilité interne peut aider! Nous stockerons les `sent_messages` dans un `RefCell<T>`, puis la méthode `send` sera capable de modifier `sent_messages` pour stocker les messages que nous avons reçus. La liste 15-22 montre à quoi cela ressemble.

Nom de fichier : `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;
    use std::cell::RefCell;

    struct MockMessenger {
      1 sent_messages: RefCell<Vec<String>>,
    }

    impl MockMessenger {
        fn new() -> MockMessenger {
            MockMessenger {
              2 sent_messages: RefCell::new(vec![]),
            }
        }
    }

    impl Messenger for MockMessenger {
        fn send(&self, message: &str) {
            self.sent_messages
              3.borrow_mut()
               .push(String::from(message));
        }
    }

    #[test]
    fn it_sends_an_over_75_percent_warning_message() {
        --snip--

        assert_eq!(
          4 mock_messenger.sent_messages.borrow().len(),
            1
        );
    }
}
```

Liste 15-22 : Utilisation de `RefCell<T>` pour modifier une valeur interne tandis que la valeur externe est considérée immuable

Le champ `sent_messages` est maintenant de type `RefCell<Vec<String>>` \[1\] au lieu de `Vec<String>`. Dans la fonction `new`, nous créons une nouvelle instance de `RefCell<Vec<String>>` autour du vecteur vide \[2\].

Pour l'implémentation de la méthode `send`, le premier paramètre est toujours un emprunt immuable de `self`, ce qui correspond à la définition du trait. Nous appelons `borrow_mut` sur le `RefCell<Vec<String>>` dans `self.sent_messages` \[3\] pour obtenir une référence mutable à la valeur à l'intérieur du `RefCell<Vec<String>>`, qui est le vecteur. Ensuite, nous pouvons appeler `push` sur la référence mutable au vecteur pour suivre les messages envoyés pendant le test.

La dernière modification que nous devons apporter est dans l'assertion : pour voir combien d'éléments sont dans le vecteur interne, nous appelons `borrow` sur le `RefCell<Vec<String>>` pour obtenir une référence immuable au vecteur \[4\].

Maintenant que vous avez vu comment utiliser `RefCell<T>`, approfondissons comment cela fonctionne!
