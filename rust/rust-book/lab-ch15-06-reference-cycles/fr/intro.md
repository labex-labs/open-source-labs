# Introduction

Bienvenue dans **Reference Cycles Can Leak Memory**. Ce laboratoire est une partie du [Rust Book](https://doc.rust-lang.org/book/). Vous pouvez pratiquer vos compétences Rust dans LabEx.

Dans ce laboratoire, nous explorons comment les garanties de sécurité mémoire de Rust rendent difficile mais pas impossible de créer accidentellement des fuites mémoire, en particulier lorsqu'on utilise `Rc<T>` et `RefCell<T>` qui peuvent entraîner des cycles de référence empêchant les valeurs d'être supprimées et donc fuitant la mémoire.
