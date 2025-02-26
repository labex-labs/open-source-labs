# Fermeture d'un générateur

Une question courante concernant les générateurs est leur durée de vie et la collecte des ordures mémoire. Par exemple, le générateur `follow()` tourne indéfiniment dans une boucle `while` infinie. Que se passe-t-il si la boucle d'itération qui le dirige s'arrête? De plus, existe-t-il un moyen de terminer prématurément le générateur?

Modifiez la fonction `follow()` de sorte que tout le code soit inclus dans un bloc `try-except` comme ceci :

```python
def follow(filename):
    try:
        with open(filename,'r') as f:
            f.seek(0,os.SEEK_END)
            while True:
                 line = f.readline()
                 if line == '':
                     time.sleep(0.1)    # Dormez brièvement pour éviter de boucler inutilement
                     continue
                 yield line
    except GeneratorExit:
        print('Following Done')
```

Maintenant, essayez quelques expériences :

```python
>>> from follow import follow
>>> # Expérience : Collecte des ordures mémoire d'un générateur en cours d'exécution
>>> f = follow('stocklog.csv')
>>> next(f)
'"MO",70.29,"6/11/2007","09:30.09",-0.01,70.25,70.30,70.29,365314\n'
>>> del f
Following Done
>>> # Expérience : Fermeture d'un générateur
>>> f = follow('stocklog.csv')
>>> for line in f:
        print(line,end='')
        if 'IBM' in line:
            f.close()

"VZ",42.91,"6/11/2007","09:34.28",-0.16,42.95,42.91,42.78,210151
"HPQ",45.76,"6/11/2007","09:34.29",0.06,45.80,45.76,45.59,257169
"GM",31.45,"6/11/2007","09:34.31",0.45,31.00,31.50,31.45,582429
...
"IBM",102.86,"6/11/2007","09:34.44",-0.21,102.87,102.86,102.77,147550
Following Done
>>> for line in f:
        print(line, end='')    # Aucune sortie : le générateur est terminé

>>>
```

Dans ces expériences, vous pouvez constater qu'une exception `GeneratorExit` est levée lorsqu'un générateur est collecté ou fermé explicitement via sa méthode `close()`.

Un autre domaine d'exploration est de savoir si vous pouvez reprendre l'itération sur un générateur si vous sortez d'une boucle `for`. Par exemple, essayez ceci :

```python
>>> f = follow('stocklog.csv')
>>> for line in f:
        print(line,end='')
        if 'IBM' in line:
            break

"CAT",78.36,"6/11/2007","09:37.19",-0.16,78.32,78.36,77.99,237714
"VZ",42.99,"6/11/2007","09:37.20",-0.08,42.95,42.99,42.78,268459
...
"IBM",102.91,"6/11/2007","09:37.31",-0.16,102.87,102.91,102.77,190859
>>> # Reprendre l'itération
>>> for line in f:
        print(line,end='')
        if 'IBM' in line:
            break

"AA",39.58,"6/11/2007","09:39.28",-0.08,39.67,39.58,39.31,243159
"HPQ",45.94,"6/11/2007","09:39.29",0.24,45.80,45.94,45.59,408919
...
"IBM",102.95,"6/11/2007","09:39.44",-0.12,102.87,102.95,102.77,225350
>>> del f
Following Done
>>>
```

En général, vous pouvez sortir de l'itération en cours d'exécution et la reprendre plus tard si nécessaire. Vous devez juste vous assurer que l'objet générateur n'est pas fermé de force ou collecté des ordures mémoire d'une manière ou d'une autre.
