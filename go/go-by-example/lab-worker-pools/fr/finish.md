# Résumé

Ce laboratoire a montré comment implémenter un pool de travailleurs à l'aide de goroutines et de canaux. Le pool de travailleurs reçoit des travaux sur le canal `jobs` et envoie les résultats correspondants sur le canal `results`. Chaque travailleur dort une seconde par travail pour simuler une tâche coûteuse.
