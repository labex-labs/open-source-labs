# Templates de Texto

Neste laboratório, você deve demonstrar o uso do pacote `text/template` para gerar conteúdo dinâmico.

- Use o pacote `text/template` para gerar conteúdo dinâmico.
- Use a função `template.Must` para entrar em pânico caso `Parse` retorne um erro.
- Use a ação `{{.FieldName}}` para acessar campos de struct.
- Use a ação `{{if . -}} yes {{else -}} no {{end}}\n` para fornecer execução condicional para templates.
- Use a ação `{{range .}}{{.}} {{end}}\n` para iterar sobre slices, arrays, mapas ou canais.

```sh
$ go run templates.go
Value: some text
Value: 5
Value: [Go Rust C++ C#]
Name: Jane Doe
Name: Mickey Mouse
yes
no
Range: Go Rust C++ C#
```

A seguir, o código completo:

```go
// Go oferece suporte integrado para criar conteúdo dinâmico ou mostrar saídas personalizadas
// ao usuário com o pacote `text/template`. Um pacote irmão
// chamado `html/template` fornece a mesma API, mas possui recursos de segurança adicionais
// e deve ser usado para gerar HTML.

package main

import (
	"os"
	"text/template"
)

func main() {

	// Podemos criar um novo template e analisar seu corpo a partir de
	// uma string.
	// Templates são uma mistura de texto estático e "ações" contidas em
	// `{{...}}` que são usadas para inserir conteúdo dinamicamente.
	t1 := template.New("t1")
	t1, err := t1.Parse("Value is {{.}}\n")
	if err != nil {
		panic(err)
	}

	// Alternativamente, podemos usar a função `template.Must` para
	// entrar em pânico caso `Parse` retorne um erro. Isso é especialmente
	// útil para templates inicializados no escopo global.
	t1 = template.Must(t1.Parse("Value: {{.}}\n"))

	// Ao "executar" o template, geramos seu texto com
	// valores específicos para suas ações. A ação `{{.}}` é
	// substituída pelo valor passado como um parâmetro para `Execute`.
	t1.Execute(os.Stdout, "some text")
	t1.Execute(os.Stdout, 5)
	t1.Execute(os.Stdout, []string{
		"Go",
		"Rust",
		"C++",
		"C#",
	})

	// Função auxiliar que usaremos abaixo.
	Create := func(name, t string) *template.Template {
		return template.Must(template.New(name).Parse(t))
	}

	// Se os dados forem uma struct, podemos usar a ação `{{.FieldName}}` para acessar
	// seus campos. Os campos devem ser exportados para serem acessíveis quando um
	// template estiver executando.
	t2 := Create("t2", "Name: {{.Name}}\n")

	t2.Execute(os.Stdout, struct {
		Name string
	}{"Jane Doe"})

	// O mesmo se aplica a mapas; com mapas, não há restrição sobre o
	// caso dos nomes das chaves.
	t2.Execute(os.Stdout, map[string]string{
		"Name": "Mickey Mouse",
	})

	// if/else fornecem execução condicional para templates. Um valor é considerado
	// falso se for o valor padrão de um tipo, como 0, uma string vazia,
	// ponteiro nil, etc.
	// Este exemplo demonstra outra
	// característica dos templates: usar `-` em ações para aparar espaços em branco.
	t3 := Create("t3",
		"{{if . -}} yes {{else -}} no {{end}}\n")
	t3.Execute(os.Stdout, "not empty")
	t3.Execute(os.Stdout, "")

	// blocos range nos permitem iterar sobre slices, arrays, mapas ou canais. Dentro
	// do bloco range `{{.}}` é definido para o item atual da iteração.
	t4 := Create("t4",
		"Range: {{range .}}{{.}} {{end}}\n")
	t4.Execute(os.Stdout,
		[]string{
			"Go",
			"Rust",
			"C++",
			"C#",
		})
}
```
