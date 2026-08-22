# RISify

[![release](https://img.shields.io/gitea/v/release/parcifal/RISify?gitea_url=https%3A%2F%2Fscm.parcifal.dev&label=latest+release)][release]
[![pypi](https://img.shields.io/pypi/v/RISify?label=pypi+release)][pypi]
[![develop](https://scm.parcifal.dev/parcifal/RISify/badges/workflows/push.yml/badge.svg?label=develop&branch=develop)][develop]
[![master](https://scm.parcifal.dev/parcifal/RISify/badges/workflows/push.yml/badge.svg?label=master&branch=master)][master]
[![gitlab](https://img.shields.io/gitlab/last-commit/parcifal%2FRISify?label=gitlab+mirror)][gitlab]
[![github](https://img.shields.io/github/last-commit/parcifal%2FRISify?label=github+mirror)][github]

![RISify logo](https://scm.parcifal.dev/parcifal/RISify/raw/branch/develop/assets/logo.png)

RISify is a Python library and CLI for working with Regional Indicator Symbols 
(RIS): the Unicode characters used to represent country and region flags. 

It provides:

 - Encoding and decoding between RIS, ASCII, and HTML entities
 - Upper- and lowercase ASCII variants
 - Safe HTML output using markupsafe
 - Concatenation and comparison support

 > Licensed under the [AGPLv3.0][license]
 
 > The RISify logo uses the Faroese flag from the [Twemoji][twemoji] project 
 > &copy; 2017 Twitter, licensed under [CC-BY 4.0][cc-by-4.0].

## Installation

RISify is available on [PyPI][pypi]:

```bash
pip install RISify
```

Or install directly from source:

```bash
git clone git@scm.parcifal.dev:parcifal/RISify.git
cd RISify
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
[the Forgejo repository](https://scm.parcifal.dev/parcifal/RISify). All 
contributions are welcome.

[license]: https://scm.parcifal.dev/parcifal/RISify/src/branch/master/LICENSE

[twemoji]: https://github.com/twitter/twemoji
[cc-by-4.0]: https://creativecommons.org/licenses/by/4.0/

[release]: https://scm.parcifal.dev/parcifal/RISify/releases/latest
[gitlab]: https://gitlab.com/parcifal/RISify
[github]: https://github.com/parcifal/RISify
[develop]: https://scm.parcifal.dev/parcifal/RISify/src/branch/develop
[master]: https://scm.parcifal.dev/parcifal/RISify/src/branch/master

[pypi]: https://pypi.org/project/RISify/
