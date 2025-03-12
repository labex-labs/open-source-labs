# Comprendre l'héritage simple et multiple

Dans cette étape, nous allons apprendre les deux principaux types d'héritage en Python : l'héritage simple et l'héritage multiple. L'héritage est un concept fondamental en programmation orientée objet qui permet à une classe d'hériter d'attributs et de méthodes d'autres classes. Nous allons également examiner comment Python détermine quelle méthode appeler lorsqu'il y a plusieurs candidats, un processus connu sous le nom de résolution de méthode.

## Héritage simple

L'héritage simple se produit lorsque les classes forment une seule lignée d'ascendance. Imaginez - le comme un arbre généalogique où chaque classe n'a qu'un seul parent direct. Créons un exemple pour comprendre son fonctionnement.

Tout d'abord, ouvrez un nouveau terminal dans le WebIDE. Une fois le terminal ouvert, lancez l'interpréteur Python en tapant la commande suivante puis en appuyant sur Entrée :

```bash
python3
```

Maintenant que vous êtes dans l'interpréteur Python, nous allons créer trois classes qui forment une chaîne d'héritage simple. Entrez le code suivant :

```python
class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()

class C(B):
    def spam(self):
        print('C.spam')
        super().spam()
```

Dans ce code, la classe `B` hérite de la classe `A`, et la classe `C` hérite de la classe `B`. La fonction `super()` est utilisée pour appeler la méthode de la classe parente.

Après avoir défini ces classes, nous pouvons découvrir l'ordre dans lequel Python recherche les méthodes. Cet ordre est appelé l'ordre de résolution de méthode (Method Resolution Order - MRO). Pour voir le MRO de la classe `C`, tapez le code suivant :

```python
C.__mro__
```

Vous devriez voir une sortie similaire à celle - ci :

```
(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
```

Cette sortie montre que Python cherche d'abord une méthode dans la classe `C`, puis dans la classe `B`, ensuite dans la classe `A`, et enfin dans la classe de base `object`.

Maintenant, créons une instance de la classe `C` et appelons sa méthode `spam()`. Tapez le code suivant :

```python
c = C()
c.spam()
```

Vous devriez voir la sortie suivante :

```
C.spam
B.spam
A.spam
```

Cette sortie démontre le fonctionnement de `super()` dans une chaîne d'héritage simple. Lorsque `C.spam()` appelle `super().spam()`, il appelle `B.spam()`. Ensuite, lorsque `B.spam()` appelle `super().spam()`, il appelle `A.spam()`.

## Héritage multiple

L'héritage multiple permet à une classe d'hériter de plusieurs classes parentes. Cela donne à une classe accès aux attributs et méthodes de toutes ses classes parentes. Voyons comment la résolution de méthode fonctionne dans ce cas.

Entrez le code suivant dans votre interpréteur Python :

```python
class Base:
    def spam(self):
        print('Base.spam')

class X(Base):
    def spam(self):
        print('X.spam')
        super().spam()

class Y(Base):
    def spam(self):
        print('Y.spam')
        super().spam()

class Z(Base):
    def spam(self):
        print('Z.spam')
        super().spam()
```

Maintenant, nous allons créer une classe `M` qui hérite de plusieurs classes parentes `X`, `Y` et `Z`. Entrez le code suivant :

```python
class M(X, Y, Z):
    pass

M.__mro__
```

Vous devriez voir la sortie suivante :

```
(<class '__main__.M'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class '__main__.Base'>, <class 'object'>)
```

Cette sortie montre l'ordre de résolution de méthode pour la classe `M`. Python recherchera les méthodes dans cet ordre.

Créons une instance de la classe `M` et appelons sa méthode `spam()` :

```python
m = M()
m.spam()
```

Vous devriez voir la sortie suivante :

```
X.spam
Y.spam
Z.spam
Base.spam
```

Notez que `super()` ne fait pas simplement appel à la méthode de la classe parente immédiate. Au lieu de cela, il suit l'ordre de résolution de méthode (MRO) défini par la classe enfant.

Créons une autre classe `N` avec les classes parentes dans un ordre différent :

```python
class N(Z, Y, X):
    pass

N.__mro__
```

Vous devriez voir la sortie suivante :

```
(<class '__main__.N'>, <class '__main__.Z'>, <class '__main__.Y'>, <class '__main__.X'>, <class '__main__.Base'>, <class 'object'>)
```

Maintenant, créez une instance de la classe `N` et appelez sa méthode `spam()` :

```python
n = N()
n.spam()
```

Vous devriez voir la sortie suivante :

```
Z.spam
Y.spam
X.spam
Base.spam
```

Cela montre un concept important : dans l'héritage multiple de Python, l'ordre des classes parentes dans la définition de la classe détermine l'ordre de résolution de méthode. La fonction `super()` suit cet ordre, peu importe depuis quelle classe elle est appelée.

Lorsque vous avez terminé d'explorer ces concepts, vous pouvez quitter l'interpréteur Python en tapant le code suivant :

```python
exit()
```
