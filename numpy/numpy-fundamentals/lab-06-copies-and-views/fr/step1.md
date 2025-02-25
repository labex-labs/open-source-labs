# Comprendre les copies et les vues

Les tableaux NumPy sont composés de deux parties : le tampon de données et les métadonnées. Le tampon de données contient les éléments de données réels, tandis que les métadonnées incluent des informations telles que le type de données et les incréments.

Lors de l'opération sur les tableaux NumPy, il est important de comprendre la différence entre les copies et les vues :

- Une **vue** vous permet d'accéder au tableau différemment en changeant certaines métadonnées sans modifier le tampon de données. Toute modification effectuée sur une vue sera réfléchie dans le tableau d'origine.

- Une **copie** est un nouveau tableau qui duplique à la fois le tampon de données et les métadonnées. Les modifications effectuées sur une copie n'affecteront pas le tableau d'origine.
