# Classified Ipsum
A single Python script for easily sanitizing and redacting text.

## Usage
```py
str = String("hello, world")
# Redaction
print(str.redact()) # [REDACTED][REDACTED]
# Sanitization
print(str.sanitize()) # █████ █████
```

## Credits
This is a Python port of [this Ruby library](https://github.com/leereilly/classified-ipsum).

Licensed under [MIT License](LICENSE) (which is the same license as the original Ruby version).
