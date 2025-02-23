# Grundlegende Teststrategien

Es gibt viele Wege, um Tests zu schreiben.

Einige Programmierer folgen einer Disziplin namens "[testgetriebene Entwicklung](https://en.wikipedia.org/wiki/Test-driven_development)"; sie schreiben tatsächlich ihre Tests, bevor sie ihren Code schreiben. Dies mag zunächst gegenintuitive erscheinen, ist aber tatsächlich ähnlich dem, was die meisten Menschen sowieso oft tun: Sie beschreiben ein Problem und erstellen dann Code, um es zu lösen. Die testgetriebene Entwicklung formalisieren das Problem in einem Python-Testfall.

Oft werden Anfänger beim Testen zuerst Code erstellen und später entscheiden, dass dieser Tests benötigen sollte. Vielleicht wäre es besser gewesen, Tests früher zu schreiben, aber es ist nie zu spät, um zu beginnen.

Manchmal ist es schwierig, herauszufinden, wo man mit dem Schreiben von Tests beginnen soll. Wenn Sie bereits mehrere tausend Zeilen Python-Code geschrieben haben, kann es nicht einfach sein, etwas auszuwählen, das getestet werden soll. In einem solchen Fall lohnt es sich, Ihren ersten Test beim nächsten Codeänderungsschritt zu schreiben, sei es, wenn Sie eine neue Funktion hinzufügen oder einen Bug beheben.

Lassen Sie uns daher sofort loslegen.
