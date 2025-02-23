# Introduction

En Golang, la fermeture d'un canal peut être utilisée pour communiquer la fin à des récepteurs de canal. Dans ce laboratoire, nous allons démontrer comment utiliser un canal pour communiquer des travaux à effectuer du goroutine `main()` à une goroutine de travail, et comment fermer le canal lorsqu'il n'y a plus de tâches pour le travailleur.
