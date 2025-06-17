# Autoriser le transfert de propriété entre les threads avec Send

Le trait marqueur `Send` indique que la propriété des valeurs du type implémentant `Send` peut être transférée entre les threads. Presque tous les types Rust sont `Send`, mais il existe quelques exceptions, notamment `Rc<T>` : celui-ci ne peut pas être `Send` car si vous cloniez une valeur `Rc<T>` et tentiez de transférer la propriété du clone vers un autre thread, les deux threads pourraient mettre à jour le compteur de références en même temps. Pour cette raison, `Rc<T>` est implémenté pour une utilisation dans des situations mono-thread où vous ne voulez pas payer la pénalité de performance liée à la sécurité des threads.

Par conséquent, le système de types et les bornes de traits de Rust garantissent que vous ne pouvez jamais accidentellement envoyer une valeur `Rc<T>` entre les threads de manière non sécurisée. Lorsque nous avons essayé de le faire dans le Listing 16-14, nous avons obtenu l'erreur `the trait Send is not implemented for Rc<Mutex<i32>>`. Lorsque nous sommes passés à `Arc<T>`, qui est `Send`, le code a compilé.

Tout type composé entièrement de types `Send` est automatiquement marqué comme `Send` également. Presque tous les types primitifs sont `Send`, à l'exception des pointeurs bruts, dont nous discuterons au chapitre 19.
