# Weitere Tests

In diesem Tutorial werden nur einige der Grundlagen des Testens vorgestellt. Es gibt noch viel mehr, was Sie tun können, und eine Reihe sehr nützlicher Tools, mit denen Sie sehr intelligente Dinge erreichen können.

Zum Beispiel haben unsere Tests hier einige der internen Logik eines Modells und die Art, wie unsere Ansichten Informationen veröffentlichen, abgedeckt, aber Sie können ein "in-browser"-Framework wie [Selenium](https://www.selenium.dev/) verwenden, um zu testen, wie Ihre HTML-Seite tatsächlich in einem Browser gerendert wird. Mit diesen Tools können Sie nicht nur das Verhalten Ihres Django-Codes, sondern auch beispielsweise das von Ihrem JavaScript überprüfen. Es ist ziemlich beeindruckend, zu sehen, wie die Tests einen Browser starten und mit Ihrer Website interagieren, als ob ein Mensch sie bediene! Django enthält `~django.test.LiveServerTestCase`, um die Integration mit Tools wie Selenium zu erleichtern.

Wenn Sie eine komplexe Anwendung haben, möchten Sie möglicherweise Tests automatisch mit jedem Commit für die Zwecke der [kontinuierlichen Integration](https://en.wikipedia.org/wiki/Continuous_integration) ausführen, so dass die Qualitätssicherung zumindest teilweise automatisiert ist.

Ein guter Weg, um ungetestete Teile Ihrer Anwendung zu entdecken, ist die Prüfung der Codeabdeckung. Dies hilft auch, fragiles oder sogar todes代码 zu identifizieren. Wenn Sie einen Codeausschnitt nicht testen können, bedeutet das normalerweise, dass der Code umgebaut oder entfernt werden sollte. Die Abdeckung wird helfen, todes代码 zu identifizieren. Einzelheiten finden Sie unter `topics-testing-code-coverage`.

`Testing in Django </topics/testing/index>` enthält umfassende Informationen zum Testen.
