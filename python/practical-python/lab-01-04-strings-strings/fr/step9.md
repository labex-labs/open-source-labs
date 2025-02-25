# Chaînes d'octets

Une chaîne d'octets de 8 bits, couramment rencontrée dans les entrées/sorties de bas niveau, est écrite comme suit :

```python
data = b'Hello World\r\n'
```

En plaçant un petit `b` avant la première citation, vous spécifiez qu'il s'agit d'une chaîne d'octets contrairement à une chaîne de texte.

La plupart des opérations habituelles sur les chaînes fonctionnent.

```python
len(data)                         # 13
data[0:5]                         # b'Hello'
data.replace(b'Hello', b'Cruel')  # b'Cruel World\r\n'
```

L'indexation est un peu différente car elle renvoie les valeurs d'octets sous forme d'entiers.

```python
data[0]   # 72 (code ASCII pour 'H')
```

Conversion vers/à partir de chaînes de texte.

```python
text = data.decode('utf-8') # octets -> texte
data = text.encode('utf-8') # texte -> octets
```

L'argument `'utf-8'` spécifie un codage de caractères. Les autres valeurs courantes incluent `'ascii'` et `'latin1'`.
