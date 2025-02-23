# Anpassen der Admin-Änderungsliste

Jetzt, da die Frage-Admin-Seite gut aussieht, machen wir einige Anpassungen an der "Änderungsliste"-Seite - der Seite, die alle Fragen im System anzeigt.

So sieht sie derzeit aus:

![Polls change list page](../assets/admin04t.png)

Standardmäßig zeigt Django die `str()` jedes Objekts. Manchmal wäre es jedoch hilfreicher, wenn wir einzelne Felder anzeigen könnten. Um das zu tun, verwenden Sie die `~django.contrib.admin.ModelAdmin.list_display`-Admin-Option, die ein Tupel von Feldnamen ist, die als Spalten auf der Änderungsliste-Seite für das Objekt angezeigt werden sollen:

```python
class QuestionAdmin(admin.ModelAdmin):
    #...
    list_display = ["question_text", "pub_date"]
```

Als zusätzliche Verbesserung fügen wir auch die `was_published_recently()`-Methode aus **Set Up the Database** hinzu:

```python
class QuestionAdmin(admin.ModelAdmin):
    #...
    list_display = ["question_text", "pub_date", "was_published_recently"]
```

Jetzt sieht die Frage-Änderungsliste-Seite so aus:

![Question change list view](../assets/20230908-16-14-08-GNY2lggF.png)

Sie können auf die Spaltenüberschriften klicken, um nach diesen Werten zu sortieren - Ausnahme: die Spaltenüberschrift von `was_published_recently`, da das Sortieren nach der Ausgabe einer beliebigen Methode nicht unterstützt wird. Beachten Sie auch, dass die Spaltenüberschrift von `was_published_recently` standardmäßig der Name der Methode ist (mit Unterstrichen durch Leerzeichen ersetzt) und dass jede Zeile die Zeichenfolge-Darstellung der Ausgabe enthält.

Sie können dies verbessern, indem Sie den `~django.contrib.admin.display`-Decorator auf diese Methode (in `polls/models.py`) anwenden, wie folgt:

```python
from django.contrib import admin


class Question(models.Model):
    #...
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
```

Weitere Informationen zu den über den Decorator konfigurierbaren Eigenschaften finden Sie in `~django.contrib.admin.ModelAdmin.list_display`.

Bearbeiten Sie Ihre `polls/admin.py`-Datei erneut und fügen Sie eine Verbesserung zur Frage-Änderungsliste-Seite hinzu: Filter mit `~django.contrib.admin.ModelAdmin.list_filter`. Fügen Sie der `QuestionAdmin` die folgende Zeile hinzu:

```python
list_filter = ["pub_date"]
```

Das fügt eine "Filter"-Leiste hinzu, mit der Benutzer die Änderungsliste nach dem `pub_date`-Feld filtern können:

![Admin list filter sidebar](../assets/20230908-16-16-39-otfMNyYo.png)

Der angezeigte Filtertyp hängt vom Typ des zu filternden Felds ab. Da `pub_date` ein `~django.db.models.DateTimeField` ist, weiß Django, passende Filteroptionen anzuzeigen: "Jede beliebige Date", "Heute", "Letzte 7 Tage", "Dieser Monat", "Dieses Jahr".

Das sieht gut aus. Fügen wir noch eine Suchfunktion hinzu:

```python
search_fields = ["question_text"]
```

Das fügt eine Suchleiste oben auf der Änderungsliste hinzu. Wenn jemand Suchbegriffe eingibt, sucht Django im `question_text`-Feld. Sie können so viele Felder wie Sie möchten verwenden - obwohl es hinter den Kulissen eine `LIKE`-Abfrage verwendet, wird es für Ihre Datenbank einfacher, die Suche zu erledigen, wenn Sie die Anzahl der Suchfelder auf eine vernünftige Zahl begrenzen.

Es ist auch ein guter Zeitpunkt, zu beachten, dass Änderungslisten Ihnen eine kostenlose Seitenaufteilung bieten. Der Standardwert ist es, 100 Elemente pro Seite anzuzeigen. `Änderungslisten-Seitenaufteilung <django.contrib.admin.ModelAdmin.list_per_page>`, `Suchfelder <django.contrib.admin.ModelAdmin.search_fields>`, `Filter <django.contrib.admin.ModelAdmin.list_filter>`, `Datumshierarchien <django.contrib.admin.ModelAdmin.date_hierarchy>` und `Spaltenüberschriften-Sortierung <django.contrib.admin.ModelAdmin.list_display>` funktionieren alle zusammen, wie Sie es erwarten würden.
