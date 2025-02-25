# Bitmanipulationsoperationen

## Problem

Implementieren Sie die folgenden üblichen Bitmanipulationsoperationen in Python:

- `get_bit`: Gegeben eine Zahl und einen Index, geben Sie den Wert des Bits an dem angegebenen Index zurück.
- `set_bit`: Gegeben eine Zahl und einen Index, setzen Sie den Wert des Bits an dem angegebenen Index auf 1.
- `clear_bit`: Gegeben eine Zahl und einen Index, setzen Sie den Wert des Bits an dem angegebenen Index auf 0.
- `clear_bits_msb_to_index`: Gegeben eine Zahl und einen Index, setzen Sie alle Bits von dem höchstwertigen Bit bis zum angegebenen Index auf 0.
- `clear_bits_index_to_lsb`: Gegeben eine Zahl und einen Index, setzen Sie alle Bits vom angegebenen Index bis zum niedrigstwertigen Bit auf 0.
- `update_bit`: Gegeben eine Zahl, einen Index und einen Wert, aktualisieren Sie den Wert des Bits an dem angegebenen Index auf den angegebenen Wert.

## Anforderungen

Die Implementierung sollte die folgenden Anforderungen erfüllen:

- Die Eingaben können ungültig sein, und die Implementierung sollte solche Fälle elegant behandeln.
- Die Implementierung sollte im Speicher passen.

## Beispielverwendung

Hier sind einige Beispiele, wie die implementierten Funktionen verwendet werden können:

- `get_bit`:
  ```
  number   = 0b10001110
  index = 3
  expected = True
  ```
- `set_bit`:
  ```
  number   = 0b10001110
  index = 4
  expected = 0b10011110
  ```
- `clear_bit`:
  ```
  number   = 0b10001110
  index = 3
  expected = 0b10000110
  ```
- `clear_bits_msb_to_index`:
  ```
  number   = 0b10001110
  index = 3
  expected = 0b00000110
  ```
- `clear_bits_index_to_lsb`:
  ```
  number   = 0b10001110
  index = 3
  expected = 0b10000000
  ```
- `update_bit`:

  ```
  number   = 0b10001110
  index = 3
  value = 1
  expected = 0b10001110

  number   = 0b10001110
  index = 3
  value = 0
  expected = 0b10000110

  number   = 0b10001110
  index = 0
  value = 1
  expected = 0b10001111
  ```
