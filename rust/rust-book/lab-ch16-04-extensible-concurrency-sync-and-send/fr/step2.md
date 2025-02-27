# Allowing Transference of Ownership Between Threads with Send

Le trait marqueur `Send` indique que la propriété des valeurs du type implémentant `Send` peut être transférée entre les threads. Presque tous les types Rust sont `Send`, mais il y a quelques exceptions, y compris `Rc<T>` : ce type ne peut pas être `Send` car si vous clonez une valeur `Rc<T>` et essayez de transférer la propriété du clone à un autre thread, les deux threads pourraient mettre à jour le compteur de références en même temps. C'est pourquoi `Rc<T>` est conçu pour être utilisé dans des situations mono-threadées où vous ne voulez pas payer le prix de performance lié à la sécurité des threads.

Par conséquent, le système de types de Rust et les contraintes de traits garantissent que vous ne pouvez jamais accidentellement envoyer une valeur `Rc<T>` entre les threads de manière non sécurisée. Lorsque nous avons essayé de le faire dans la liste 16-14, nous avons obtenu l'erreur `the trait`Send`is not implemented for`Rc\<Mutex`<i32>`{=html}\>\``. Lorsque nous avons changé pour `Arc`<T>`{=html}`, qui est `Send`, le code s'est compilé.

Tout type composé entièrement de types `Send` est automatiquement marqué comme `Send` également. Presque tous les types primitifs sont `Send`, à l'exception des pointeurs bruts, que nous aborderons au chapitre 19.
