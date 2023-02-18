# ris-py

`ris-py` is a Python library that provides functions for encoding and decoding 
Regional Indicator Symbols (RIS), which are Unicode characters used to 
represent flags of countries and regions.

## Installation

You can install `ris-py` via pip:

```bash
pip install ris-py
```

## Usage

```python
from ris import RIS

# decode a country code to RIS
pt = RIS.decode("PT")
print(pt) # 🇵🇹

# decode HTML-symbols to RIT
de = RIS.decode("&#127465;&#127466;", encoding="html")
print(de) # 🇩🇪

# encode a RIS to country code
nl = RIS("🇳🇱")
print(nl.encode()) # NL

# encode a RIS to HTML-safe symbols
fo = RIS("🇫🇴")
print(fo.encode(encoding="html")) # &#127467;&#127476;
```

Note that `ris-py` also provides functions for encoding and decoding RIS as 
HTML-safe symbols, which can be useful for ensuring that the symbols are 
markup-safe when used in HTML

## Contributing

Contributions are welcome! If you find a bug or have an idea for a new 
feature, please open an issue on the GitHub repository. If you would like to 
contribute code, please fork the repository and submit a pull request.

## License

`ris-py` is released under the GPLv3 license. See [LICENSE](LICENCE) for
details.
