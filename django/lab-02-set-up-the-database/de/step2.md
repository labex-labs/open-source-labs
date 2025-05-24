# Modelle erstellen

Nun werden wir Ihre Modelle definieren - im Wesentlichen die Layout Ihrer Datenbank mit zusätzlichen Metadaten.

Ein Modell ist die einzige, definitive Informationsquelle über Ihre Daten. Es enthält die wesentlichen Felder und Verhaltensweisen der Daten, die Sie speichern. Django folgt dem `DRY-Prinzip <dry>`. Das Ziel ist, Ihr Datenmodell an einem Ort zu definieren und daraus automatisch Dinge abzuleiten.

Dies umfasst auch die Migrationen - im Gegensatz zu Ruby On Rails beispielsweise werden die Migrationen vollständig aus Ihrer Models-Datei abgeleitet und sind im Wesentlichen eine Geschichte, die Django durchlaufen kann, um Ihren Datenbank-Schema zu aktualisieren, um es Ihrem aktuellen Modell zu entsprechen.

In unserer Umfrage-App werden wir zwei Modelle erstellen: `Question` und `Choice`. Eine `Question` hat eine Frage und ein Veröffentlichungsdatum. Eine `Choice` hat zwei Felder: den Text der Wahl und eine Stimmenzählung. Jede `Choice` ist mit einer `Question` assoziiert.

Diese Konzepte werden durch Python-Klassen dargestellt. Bearbeiten Sie die Datei `polls/models.py`, so dass sie wie folgt aussieht:

```python
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

Hier wird jedes Modell durch eine Klasse dargestellt, die von `django.db.models.Model` abgeleitet wird. Jedes Modell hat eine Reihe von Klassenvariablen, von denen jede ein Datenbankfeld im Modell repräsentiert.

Jedes Feld wird durch eine Instanz einer `~django.db.models.Field`-Klasse dargestellt - z.B. `~django.db.models.CharField` für Zeichenfelder und `~django.db.models.DateTimeField` für Datums- und Uhrzeitangaben. Dies sagt Django, welchen Datentyp jedes Feld aufnimmt.

Der Name jeder `~django.db.models.Field`-Instanz (z.B. `question_text` oder `pub_date`) ist der Feldname im maschinenlesbaren Format. Sie werden diesen Wert in Ihrem Python-Code verwenden, und Ihre Datenbank wird ihn als Spaltennamen verwenden.

Sie können einen optionalen ersten Positionsargument für eine `~django.db.models.Field` verwenden, um einen menschenlesbaren Namen zu 指定。Dies wird in einigen introspektiven Teilen von Django verwendet und dient gleichzeitig als Dokumentation. Wenn dieses Feld nicht angegeben wird, wird Django den maschinenlesbaren Namen verwenden. In diesem Beispiel haben wir nur einen menschenlesbaren Namen für `Question.pub_date` definiert. Für alle anderen Felder in diesem Modell wird der maschinenlesbare Name des Felds als menschenlesbarer Name ausreichen.

Einige `~django.db.models.Field`-Klassen haben erforderliche Argumente. `~django.db.models.CharField` erfordert beispielsweise, dass Sie ihm eine `~django.db.models.CharField.max_length` angeben. Dies wird nicht nur im Datenbank-Schema verwendet, sondern auch bei der Validierung, wie wir bald sehen werden.

Eine `~django.db.models.Field` kann auch verschiedene optionale Argumente haben; in diesem Fall haben wir den `~django.db.models.Field.default`-Wert von `votes` auf 0 gesetzt.

Schließlich wird eine Beziehung definiert, indem `~django.db.models.ForeignKey` verwendet wird. Dies sagt Django, dass jede `Choice` mit einer einzelnen `Question` verknüpft ist. Django unterstützt alle gängigen Datenbankbeziehungen: Vielzu-ein, Vielzu-viel und Eindeutig-eindeutig.
