# XML

Требуется создать структуру под названием `Plant`, которая может быть сопоставлена с XML. Структура должна иметь следующие поля:

- `Id` (int) - XML-атрибут
- `Name` (string) - вложенный XML-элемент
- `Origin` ([]string) - вложенный XML-элемент

Также необходимо создать структуру под названием `Nesting`, которая содержит срез структур `Plant`. Структура `Nesting` должна быть сопоставлена с XML-элементом под названием `nesting`, а структуры `Plant` должны быть вложены под `<parent><child>...`.

Затем необходимо написать код для маршалинга структур `Plant` и `Nesting` в XML и демаршалинга XML-данных в структуру `Plant`.

- Структура `Plant` должна быть сопоставлена с XML-элементом под названием `plant`.
- Поле `Id` структуры `Plant` должно быть сопоставлено с XML-атрибутом под названием `id`.
- Поле `Name` структуры `Plant` должно быть сопоставлено с вложенным XML-элементом под названием `name`.
- Поле `Origin` структуры `Plant` должно быть сопоставлено с вложенным XML-элементом под названием `origin`.
- Структура `Nesting` должна быть сопоставлена с XML-элементом под названием `nesting`.
- Структуры `Plant` в срезе `Nesting` должны быть вложены под `<parent><child>...`.

```sh
$ go run xml.go
 <plant id="27">
   <name>Coffee</name>
   <origin>Ethiopia</origin>
   <origin>Brazil</origin>
 </plant>
<?xml version="1.0" encoding="UTF-8"?>
 <plant id="27">
   <name>Coffee</name>
   <origin>Ethiopia</origin>
   <origin>Brazil</origin>
 </plant>
Plant id=27, name=Coffee, origin=[Ethiopia Brazil]
 <nesting>
   <parent>
     <child>
       <plant id="27">
         <name>Coffee</name>
         <origin>Ethiopia</origin>
         <origin>Brazil</origin>
       </plant>
       <plant id="81">
         <name>Tomato</name>
         <origin>Mexico</origin>
         <origin>California</origin>
       </plant>
     </child>
   </parent>
 </nesting>

```

Ниже представлен полный код:

```go
// Go предоставляет встроенную поддержку для XML и XML-подобных
// форматов с использованием пакета `encoding.xml`.

package main

import (
	"encoding/xml"
	"fmt"
)

// Plant будет сопоставлена с XML. Аналогично примерам с JSON,
// теги полей содержат директивы для кодировщика и декодировщика.
// Здесь мы используем некоторые особые функции пакета XML:
// поле `XMLName` определяет имя XML-элемента, представляющего
// эту структуру; `id,attr` означает, что поле `Id` является
// XML-_атрибутом_, а не вложенным элементом.
type Plant struct {
	XMLName xml.Name `xml:"plant"`
	Id      int      `xml:"id,attr"`
	Name    string   `xml:"name"`
	Origin  []string `xml:"origin"`
}

func (p Plant) String() string {
	return fmt.Sprintf("Plant id=%v, name=%v, origin=%v",
		p.Id, p.Name, p.Origin)
}

func main() {
	coffee := &Plant{Id: 27, Name: "Coffee"}
	coffee.Origin = []string{"Ethiopia", "Brazil"}

	// Генерируем XML, представляющий нашу растительность;
	// используем `MarshalIndent`, чтобы получить более
	// человекочитаемый вывод.
	out, _ := xml.MarshalIndent(coffee, " ", "  ")
	fmt.Println(string(out))

	// Чтобы добавить общий XML-заголовок к выводу, добавьте его явно.
	fmt.Println(xml.Header + string(out))

	// Используем `Unmarshal`, чтобы разобрать поток байтов с XML
	// в структуру данных. Если XML имеет неправильный формат или
	// не может быть сопоставлен с Plant, будет возвращена
	// описательная ошибка.
	var p Plant
	if err := xml.Unmarshal(out, &p); err!= nil {
		panic(err)
	}
	fmt.Println(p)

	tomato := &Plant{Id: 81, Name: "Tomato"}
	tomato.Origin = []string{"Mexico", "California"}

	// Тег `parent>child>plant` сообщает кодировщику
	// вкладывать все `plant` под `<parent><child>...`
	type Nesting struct {
		XMLName xml.Name `xml:"nesting"`
		Plants  []*Plant `xml:"parent>child>plant"`
	}

	nesting := &Nesting{}
	nesting.Plants = []*Plant{coffee, tomato}

	out, _ = xml.MarshalIndent(nesting, " ", "  ")
	fmt.Println(string(out))
}

```
