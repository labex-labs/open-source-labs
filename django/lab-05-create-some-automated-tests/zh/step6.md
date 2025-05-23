# 进一步测试

本教程仅介绍了测试的一些基础知识。你还可以做很多其他事情，并且有许多非常有用的工具可供你使用，以实现一些非常巧妙的功能。

例如，虽然我们这里的测试涵盖了模型的一些内部逻辑以及视图发布信息的方式，但你可以使用诸如 [Selenium](https://www.selenium.dev/) 这样的“浏览器内”框架来测试你的 HTML 在浏览器中的实际渲染方式。这些工具不仅可以让你检查 Django 代码的行为，还可以检查例如你的 JavaScript 的行为。看到测试启动一个浏览器，并开始与你的网站进行交互，就好像是一个人在操作它一样，这是非常了不起的！Django 包含 `~django.test.LiveServerTestCase` 以方便与 Selenium 等工具集成。

如果你有一个复杂的应用程序，你可能希望为了 [持续集成](https://en.wikipedia.org/wiki/Continuous_integration) 的目的，在每次提交时自动运行测试，以便质量控制本身——至少部分——实现自动化。

发现应用程序中未测试部分的一个好方法是检查代码覆盖率。这也有助于识别脆弱甚至无用的代码。如果你无法测试一段代码，通常意味着这段代码应该被重构或删除。代码覆盖率将有助于识别无用代码。有关详细信息，请参阅 `topics-testing-code-coverage`。

《Django 中的测试 </topics/testing/index>》包含有关测试的全面信息。
