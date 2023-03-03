"""
Definition of the RIS module.
"""

import re

from markupsafe import Markup

_ENCODING_ASCII = "ascii"
_ENCODING_HTML = "html"
_ENCODING_UNICODE = "unicode"

_ORD_A = ord("A")
_ORD_A_RIS = ord("🇦")
_ORD_Z_RIS = ord("🇿")


class _RISStr:
    """
    Wraps a RIS-string and provides several functions for encoding and decoding
    from and to plain alphabetic text and HTML.
    """

    def __init__(self, value: str, **kwargs):
        value = _RISStr._expand_html(value)
        value = _RISStr._expand_ascii(value)

        assert self._is_valid_ris(value), \
            f"specified ris-code \"{value}\" is invalid"

        self._value = value

        self._encoding = kwargs.pop("encoding", _ENCODING_UNICODE)
        self._uppercase = kwargs.pop("uppercase", True)

        assert self._encoding in (
            _ENCODING_ASCII, _ENCODING_HTML, _ENCODING_UNICODE
        ), f"specified encoding \"{self._encoding}\" unknown"

    def __str__(self):
        if self._encoding == _ENCODING_UNICODE:
            return self._value

        if self._encoding == _ENCODING_HTML:
            return Markup("".join([
                f"&#{ord(c)};" for c in self._value
            ]))

        if self._encoding == _ENCODING_ASCII:
            string = "".join([
                chr(_ORD_A + (ord(c) - _ORD_A_RIS))
                for c in self._value
            ])
            return string if self._uppercase else string.lower()

        return NotImplemented

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, _RISStr):
            return self._value == other._value
        if not isinstance(other, str):
            return NotImplemented

        other = _RISStr._expand_html(other)
        other = _RISStr._expand_ascii(other)

        if _RISStr._is_valid_ris(other):
            return self._value == other

        return NotImplemented

    def __ne__(self, other):
        return not other == self

    def __add__(self, other):
        if isinstance(other, _RISStr):
            return _RISStr(self._value + other._value)
        if _RISStr._is_valid_ris(other):
            return _RISStr(self._value + other)
        return self._value + other

    def __radd__(self, other):
        if isinstance(other, _RISStr):
            return _RISStr(other._value + self._value)
        if _RISStr._is_valid_ris(other):
            return _RISStr(other + self._value)
        return other + self._value

    def encode(self, encoding: str):
        """
        Return a RIS string of the same value as the current,
        to be encoded as specified.
        """
        return _RISStr(self._value,
                       encoding=encoding,
                       uppercase=self._uppercase)

    def upper(self):
        """
        Return a RIS string of the same value as the current,
        to be encoded in upper case. Only has effect
        if encoding is set to ASCII.
        """
        return _RISStr(self._value,
                       encoding=self._encoding,
                       uppercase=True)

    def lower(self):
        """
        Return a RIS string of the same value as the current,
        to be encoded in lower case. Only has effect
        if encoding is set to ASCII.
        """
        return _RISStr(self._value,
                       encoding=self._encoding,
                       uppercase=False)

    @staticmethod
    def _is_valid_ris(code: str) -> bool:
        """
        Indicate whether the specified string is a valid RIS-code.
        """
        return all(_ORD_A_RIS <= ord(c) <= _ORD_Z_RIS for c in code)

    @staticmethod
    def _expand_html(text: str) -> str:
        """
        Expand any occurrences of HTML-encoded RIS into actual RIS in the
        specified text.
        """
        return re.sub(r"&#(\d{6});", lambda m: chr(int(m.group(1))), text)

    @staticmethod
    def _expand_ascii(text: str) -> str:
        """
        Expand any occurrences of ASCII-encoded RIS (both upper and lower case)
        into actual RIS in the specified text.
        """
        return re.sub(r"[a-zA-Z]", lambda m: chr(ord(
            m.group(0).upper()) - _ORD_A + _ORD_A_RIS), text)


# pylint:disable = invalid-name
ris = _RISStr
