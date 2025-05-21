# Tests avec différents types de chaînes de caractères (strings)

Explorons comment différents types de caractères affectent la taille en octets d'une chaîne de caractères.

Dans la console Node.js, testons notre fonction `byteSize` avec diverses chaînes de caractères :

1. Texte anglais simple :

```javascript
byteSize("The quick brown fox jumps over the lazy dog");
```

Résultat attendu :

```
43
```

2. Nombres et caractères spéciaux :

```javascript
byteSize("123!@#$%^&*()");
```

Résultat attendu :

```
13
```

3. Un mélange de caractères ASCII et non-ASCII :

```javascript
byteSize("Hello, 世界！");
```

Résultat attendu :

```
13
```

4. Plusieurs emojis :

```javascript
byteSize("😀😃😄😁");
```

Résultat attendu :

```
16
```

Remarquez qu'avec les types de caractères mixtes, en particulier avec des caractères non-ASCII tels que les caractères chinois et les emojis, la taille en octets est supérieure au nombre de caractères.

Il est important de comprendre cela lorsque vous travaillez avec des données qui peuvent contenir des caractères internationaux ou des symboles spéciaux, car cela affecte les besoins de stockage et les tailles de transfert de données.

Quittez la console Node.js en tapant :

```javascript
.exit
```

Cela vous ramènera à l'invite de commande normale du terminal.
