# Importation des bibliothèques

Tout d'abord, nous devons importer les bibliothèques nécessaires. Nous allons utiliser Matplotlib, GTK3 et le module Gtk du gi.repository.

```python
import matplotlib
matplotlib.use('GTK3Agg')  # ou 'GTK3Cairo'
import gi
import matplotlib.pyplot as plt
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
```
