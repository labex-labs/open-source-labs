# Testes adicionais

Este tutorial apresenta apenas alguns dos conceitos básicos de teste. Há muito mais que você pode fazer e várias ferramentas muito úteis à sua disposição para realizar coisas muito inteligentes.

Por exemplo, embora nossos testes aqui tenham coberto parte da lógica interna de um modelo e a maneira como nossas views publicam informações, você pode usar um framework "in-browser" como [Selenium](https://www.selenium.dev/) para testar a forma como seu HTML realmente renderiza em um navegador. Essas ferramentas permitem que você verifique não apenas o comportamento do seu código Django, mas também, por exemplo, do seu JavaScript. É impressionante ver os testes lançarem um navegador e começar a interagir com seu site, como se um ser humano estivesse dirigindo! O Django inclui `~django.test.LiveServerTestCase` para facilitar a integração com ferramentas como Selenium.

Se você tiver uma aplicação complexa, pode querer executar testes automaticamente a cada commit para fins de [integração contínua](https://en.wikipedia.org/wiki/Continuous_integration), para que o controle de qualidade seja ele mesmo - pelo menos parcialmente - automatizado.

Uma boa maneira de detectar partes não testadas de sua aplicação é verificar a cobertura do código. Isso também ajuda a identificar código frágil ou até mesmo morto. Se você não pode testar um trecho de código, geralmente significa que esse código deve ser refatorado ou removido. A cobertura ajudará a identificar código morto. Consulte `topics-testing-code-coverage` para obter detalhes.

`Testando no Django </topics/testing/index>` tem informações abrangentes sobre testes.
