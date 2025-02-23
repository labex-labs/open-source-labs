# Introduction

Dans ce laboratoire, nous nous appuyons sur les connaissances acquises dans le laboratoire 1 où nous avons utilisé des commandes Docker pour exécuter des conteneurs. Nous allons créer une image Docker personnalisée à partir d'un Dockerfile. Une fois que nous aurons construit l'image, nous la pousserons vers un registre central où elle pourra être extraite pour être déployée dans d'autres environnements. Nous décrirons également brièvement les couches d'image, et la manière dont Docker incorpore le "copy-on-write" et le système de fichiers union pour stocker efficacement les images et exécuter les conteneurs.

Nous utiliserons quelques commandes Docker dans ce laboratoire. Pour la documentation complète des commandes disponibles, consultez la [documentation officielle](https://docs.docker.com/).
