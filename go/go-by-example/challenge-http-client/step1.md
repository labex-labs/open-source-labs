# Golang Challenge: HTTP Client

## Problem

You are required to write a program that sends an HTTP GET request to a server and prints the HTTP response status and the first 5 lines of the response body.

## Requirements

- The program should use the `net/http` package to issue an HTTP GET request.
- The program should print the HTTP response status.
- The program should print the first 5 lines of the response body.
- The program should handle errors gracefully.

## Example

```sh
$ go run http-clients.go
Response status: 200 OK
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Go by Example</title>

```
