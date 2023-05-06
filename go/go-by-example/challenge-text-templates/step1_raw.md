# Golang Challenge: Text Templates

## Introduction
The Golang `text/template` package provides a way to create dynamic content or show customized output to the user. This package allows mixing static text and actions enclosed in `{{...}}` to insert dynamic content.

## Problem
In this challenge, you are required to demonstrate the use of the `text/template` package to generate dynamic content.

## Requirements
- Use the `text/template` package to generate dynamic content.
- Use the `template.Must` function to panic in case `Parse` returns an error.
- Use the `{{.FieldName}}` action to access struct fields.
- Use the `{{if . -}} yes {{else -}} no {{end}}\n` action to provide conditional execution for templates.
- Use the `{{range .}}{{.}} {{end}}\n` action to loop through slices, arrays, maps, or channels.

## TODO
```go
// TODO: Create a new template named "t5" that accepts a struct with two fields: "Name" and "Age".
// TODO: Parse the template body from the string "Name: {{.Name}}, Age: {{.Age}}\n".
// TODO: Execute the template with a struct that has the fields "Name" and "Age" set to "John" and 30, respectively.
```

## Example
```
Value is some text
Value: 5
Value: [Go Rust C++ C#]
Name: Jane Doe
Name: Mickey Mouse
yes
no
Range: Go Rust C++ C# 
```

## Summary
In this challenge, we learned how to use the `text/template` package to generate dynamic content. We demonstrated how to access struct fields, provide conditional execution for templates, and loop through slices, arrays, maps, or channels.