# Das Template-System verwenden

Zurück zur `detail()`-Ansicht unserer Umfrageanwendung. Gegeben die Kontextvariable `question`, könnte das `polls/detail.html`-Template so aussehen:

```html+django
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```

Das Template-System verwendet die Punkt-Such-Syntax, um auf Variable-Attribute zuzugreifen. Im Beispiel von `{{ question.question_text }}` versucht Django zunächst eine Wörterbuchsuche auf dem Objekt `question`. Wenn das fehlschlägt, versucht es eine Attributsuche - was in diesem Fall funktioniert. Wenn die Attributsuche fehlgeschlagen wäre, hätte es eine Listenindexsuche versucht.

Methoden-Aufrufe erfolgen in der `{% for %}<for>`-Schleife: `question.choice_set.all` wird als Python-Code `question.choice_set.all()` interpretiert, der ein Iterable von `Choice`-Objekten zurückgibt und für die Verwendung im `{% for %}<for>`-Tag geeignet ist.
