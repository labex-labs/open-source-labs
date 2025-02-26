# Ausnahmebehandlung

Ausnahmen breiten sich bis zu der ersten passenden `except` aus.

```python
def grok():
  ...
    raise RuntimeError('Whoa!')   # Exception raised here

def spam():
    grok()                        # Call that will raise exception

def bar():
    try:
       spam()
    except RuntimeError as e:     # Exception caught here
      ...

def foo():
    try:
         bar()
    except RuntimeError as e:     # Exception does NOT arrive here
      ...

foo()
```

Um die Ausnahme zu behandeln, legen Sie Anweisungen im `except`-Block fest. Sie können beliebige Anweisungen hinzufügen, um den Fehler zu behandeln.

```python
def grok():...
    raise RuntimeError('Whoa!')

def bar():
    try:
      grok()
    except RuntimeError as e:   # Exception caught here
        statements              # Use this statements
        statements
     ...

bar()
```

Nach der Behandlung setzt die Ausführung mit der ersten Anweisung nach dem `try-except` fort.

```python
def grok():...
    raise RuntimeError('Whoa!')

def bar():
    try:
      grok()
    except RuntimeError as e:   # Exception caught here
        statements
        statements
     ...
    statements                  # Resumes execution here
    statements                  # And continues here
 ...

bar()
```
