# RISify

[![release](https://img.shields.io/gitea/v/release/parcifal/ris-py?gitea_url=https%3A%2F%2Fforgejo.parcifal.dev&label=latest+release)][release]
[![pypi](https://img.shields.io/pypi/v/RISify?label=pypi+release)][pypi]
[![develop](https://forgejo.parcifal.dev/parcifal/ris-py/badges/workflows/push.yml/badge.svg?label=develop&branch=develop)][develop]
[![master](https://forgejo.parcifal.dev/parcifal/ris-py/badges/workflows/push.yml/badge.svg?label=master&branch=master)][master]
[![gitlab](https://img.shields.io/gitlab/last-commit/parcifal%2Fris-py?label=gitlab+mirror)][gitlab]
[![github](https://img.shields.io/github/last-commit/parcifal%2Fris-py?label=github+mirror)][github]

RISify is a Python library and CLI for working with Regional Indicator Symbols 
(RIS) — the Unicode characters used to represent country and region flags. 

It provides:

 - Encoding and decoding between RIS, ASCII, and HTML entities
 - Upper- and lowercase ASCII variants
 - Safe HTML output using markupsafe
 - Concatenation and comparison support

 > Licensed under the [AGPLv3.0][license]
 
 > The RISify logo uses the [Twemoji](https://github.com/twitter/twemoji) 
 > project &copy; 2017 Twitter, licensed under
 > [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Installation

RISify is available on [PyPI][pypi]:

```bash
pip install RISify
```

Or install directly from source:

```bash
git clone git@forgejo.parcifal.dev:parcifal/ris-py.git
cd ris-py
pip install .
```

## Usage (API)

### Basic Conversion

```python
from ris import ris

# decode a country code to RIS
pt = ris("PT")
print(pt)  # 🇵🇹
```

### HTML to RIS

```python
de = ris("&#127465;&#127466;").encode("unicode")
print(de)  # 🇩🇪
```

### RIS to ASCII (upper/lower)

```python
nl = ris("🇳🇱").encode("ascii").upper()
print(nl)  # NL

eu = ris("🇪🇺").encode("ascii").lower()
print(eu)  # eu
```

### RIS to HTML

```python
fo = ris("🇫🇴").encode("html")
print(fo)  # &#127467;&#127476;
```

### Concatenation

```python
print("spam " + pt + " bacon " + de + " sausage " + nl + " eggs " + eu + " ham " + fo)
# spam 🇵🇹 bacon 🇩🇪 sausage 🇳🇱 eggs 🇪🇺 ham 🇫🇴
```

## Usage (CLI)

Installing RISify also provides a `ris` command-line tool:

```bash
ris NL  # 🇳🇱
```

### Options

```bash
usage: ris [-h] [-a | -A | -u | -H] [-v] [-l OUTPUT_LOG] [-V] value

Convert a country code to a RIS code.

positional arguments:
  value                 input text (ascii, ris or html) to convert

optional arguments:
  -h, --help            show this help message and exit
  -a, --ascii           output as a country code in lowercase ascii
  -A, --ASCII           output as a country code in uppercase ascii
  -u, --unicode         output as a ris code in unicode (default)
  -H, --html            output as a ris code in html
  -v, --verbose         increase verbosity
  -l OUTPUT_LOG, --output-log OUTPUT_LOG
                        output log file (defaults to stdout)
  -V, --version         show program's version number and exit
```

### Examples

```bash
# convert iso country code to ris
ris PT  # 🇵🇹

# convert ris to ascii uppercase
ris 🇳🇱 --ASCII  # NL

# convert ris to ascii lowercase
ris 🇪🇺 --ascii  # eu

# convert iso country code to html entities
ris FO --html  # &#127467;&#127476;

# increase verbosity and log to file
ris PT -vvv -l ris.log
```

## Contributing

Found a bug? Have a suggestion? Open an issue or submit a merge request at
[the Forgejo repository](https://forgejo.parcifal.dev/parcifal/ris-py). All 
contributions are welcome.

[license]: https://forgejo.parcifal.dev/parcifal/ris-py/src/branch/master/LICENSE

[release]: https://forgejo.parcifal.dev/parcifal/ris-py/releases/latest
[gitlab]: https://gitlab.com/parcifal/ris-py
[github]: https://github.com/parcifal/ris-py
[develop]: https://forgejo.parcifal.dev/parcifal/ris-py/src/branch/develop
[master]: https://forgejo.parcifal.dev/parcifal/ris-py/src/branch/master

[pypi]: https://pypi.org/project/RISify/
