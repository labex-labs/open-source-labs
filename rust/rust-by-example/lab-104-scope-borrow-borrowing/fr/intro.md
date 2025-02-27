# Introduction

Dans ce laboratoire, nous allons apprendre à emprunter en Rust, qui permet d'accéder aux données sans prendre la propriété en utilisant des références ('&T') au lieu de passer les objets par valeur ('T'). Le vérificateur d'emprunt s'assure que les références pointent toujours vers des objets valides et empêche la destruction des objets qui sont empruntés.

> **Note:** Si le laboratoire ne spécifie pas de nom de fichier, vous pouvez utiliser n'importe quel nom de fichier que vous voulez. Par exemple, vous pouvez utiliser `main.rs`, le compiler et l'exécuter avec `rustc main.rs &&./main`.
