# XML

`Plant`라는 이름의 구조체를 생성하여 XML 에 매핑해야 합니다. 이 구조체는 다음과 같은 필드를 가져야 합니다.

- `Id` (int) - XML 속성 (attribute)
- `Name` (string) - 중첩된 XML 요소 (element)
- `Origin` ([]string) - 중첩된 XML 요소

또한 `Plant` 구조체의 슬라이스를 포함하는 `Nesting`이라는 이름의 구조체를 생성해야 합니다. `Nesting` 구조체는 `nesting`이라는 XML 요소에 매핑되어야 하며, `Plant` 구조체는 `<parent><child>...` 아래에 중첩되어야 합니다.

그런 다음 `Plant` 및 `Nesting` 구조체를 XML 로 마샬링 (marshalling) 하고 XML 데이터를 `Plant` 구조체로 언마샬링 (unmarshalling) 하는 코드를 작성해야 합니다.

- `Plant` 구조체는 `plant`라는 XML 요소에 매핑되어야 합니다.
- `Plant` 구조체의 `Id` 필드는 `id`라는 XML 속성에 매핑되어야 합니다.
- `Plant` 구조체의 `Name` 필드는 `name`이라는 중첩된 XML 요소에 매핑되어야 합니다.
- `Plant` 구조체의 `Origin` 필드는 `origin`이라는 중첩된 XML 요소에 매핑되어야 합니다.
- `Nesting` 구조체는 `nesting`이라는 XML 요소에 매핑되어야 합니다.
- `Nesting` 슬라이스의 `Plant` 구조체는 `<parent><child>...` 아래에 중첩되어야 합니다.

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

전체 코드는 다음과 같습니다.

```go
// Go 는 `encoding.xml` 패키지를 사용하여 XML 및 XML 과 유사한
// 형식에 대한 내장 지원을 제공합니다.

package main

import (
	"encoding/xml"
	"fmt"
)

// Plant 는 XML 에 매핑됩니다. JSON 예제와 유사하게,
// 필드 태그는 인코더 (encoder) 및 디코더 (decoder) 에 대한 지시문을 포함합니다. 여기서는 XML 패키지의 몇 가지 특수 기능을 사용합니다.
// `XMLName` 필드 이름은 이 구조체를 나타내는 XML 요소의 이름을 결정합니다.
// `id,attr` 는 `Id` 필드가 중첩된 요소가 아닌 XML
// _속성_임을 의미합니다.
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

	// 식물을 나타내는 XML 을 출력합니다.
	// `MarshalIndent` 를 사용하여 더
	// 사람이 읽을 수 있는 출력을 생성합니다.
	out, _ := xml.MarshalIndent(coffee, " ", "  ")
	fmt.Println(string(out))

	// 출력에 일반적인 XML 헤더를 추가하려면
	// 명시적으로 추가합니다.
	fmt.Println(xml.Header + string(out))

	// `Unmarshal` 을 사용하여 XML 이 있는 바이트 스트림을
	// 데이터 구조로 구문 분석합니다. XML 이 잘못되었거나
	// Plant 에 매핑할 수 없는 경우 설명적인 오류가
	// 반환됩니다.
	var p Plant
	if err := xml.Unmarshal(out, &p); err != nil {
		panic(err)
	}
	fmt.Println(p)

	tomato := &Plant{Id: 81, Name: "Tomato"}
	tomato.Origin = []string{"Mexico", "California"}

	// `parent>child>plant` 필드 태그는 인코더에게
	// 모든 `plant` 를 `<parent><child>...` 아래에 중첩하도록 지시합니다.
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
