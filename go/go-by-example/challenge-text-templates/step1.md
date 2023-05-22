# Golang Challenge: Text Templates

## Problem

In this challenge, you are required to demonstrate the use of the `text/template` package to generate dynamic content.

## Requirements

- Use the `text/template` package to generate dynamic content.
- Use the `template.Must` function to panic in case `Parse` returns an error.
- Use the `{{.FieldName}}` action to access struct fields.
- Use the `{{if . -}} yes {{else -}} no {{end}}\n` action to provide conditional execution for templates.
- Use the `{{range .}}{{.}} {{end}}\n` action to loop through slices, arrays, maps, or channels.

## Example

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
