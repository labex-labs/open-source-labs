# Дополнительное тестирование

Этот учебник представляет только некоторые основы тестирования. Вы можете сделать гораздо больше, и у вас есть ряд очень полезных инструментов, с помощью которых можно достичь очень умных вещей.

Например, в то время как наши тесты здесь охватывают некоторую внутреннюю логику модели и способ, которым наши представления публикуют информацию, вы можете использовать "фреймворк в браузере", такой как [Selenium](https://www.selenium.dev/), чтобы протестировать то, как ваше HTML на самом деле отображается в браузере. Эти инструменты позволяют вам проверять не только поведение вашего кода на Django, но и, например, и вашего JavaScript. Действительно впечатляет то, как тесты запускают браузер и начинают взаимодействовать с вашим сайтом, словно это делает человек! Django включает `~django.test.LiveServerTestCase`, чтобы облегчить интеграцию с такими инструментами, как Selenium.

Если у вас есть сложное приложение, вы, возможно, захотите автоматически запускать тесты при каждом коммите для целей [непрерывной интеграции](https://en.wikipedia.org/wiki/Continuous_integration), чтобы контроль качества был - по крайней мере, частично - автоматизирован.

Хороший способ выявить не протестированные части вашего приложения - это проверить покрытие кода. Это также помогает выявить неустойчивый или даже мертвый код. Если вы не можете протестировать часть кода, это обычно означает, что этот код следует переписать или удалить. Покрытие поможет выявить мертвый код. См. `topics-testing-code-coverage` для подробностей.

`Testing in Django </topics/testing/index>` содержит полную информацию о тестировании.
