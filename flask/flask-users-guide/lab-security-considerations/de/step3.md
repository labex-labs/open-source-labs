# JSON-Sicherheit

In Flask ist es wichtig, die Sicherheit von JSON-Antworten sicherzustellen. In Versionen von Flask vor 0.10 wurden Top-Ebene-Arrays aufgrund einer Sicherheitslücke nicht in JSON serialisiert. Diese Verhalten hat sich jedoch geändert, und Top-Ebene-Arrays werden jetzt serialisiert. Es wird empfohlen, die neueste Version von Flask zu verwenden, um von dieser Sicherheitsverbesserung zu profitieren.
