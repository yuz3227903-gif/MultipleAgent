from __future__ import annotations

import warnings

import pytest

from openharness.auth import deobfuscate, decrypt, encrypt, obfuscate


def test_obfuscate_deobfuscate_round_trip():
    plaintext = "openharness-session-token-123"
    assert deobfuscate(obfuscate(plaintext)) == plaintext


def test_obfuscate_is_not_plaintext():
    plaintext = "openharness-session-token-123"
    assert obfuscate(plaintext) != plaintext


def test_deobfuscate_accepts_stripped_padding():
    plaintext = "openharness-session-token-123"
    token = obfuscate(plaintext).rstrip("=")
    assert deobfuscate(token) == plaintext


def test_encrypt_decrypt_are_deprecated_aliases():
    plaintext = "legacy-value"
    with pytest.warns(DeprecationWarning, match="encrypt.*obfuscate"):
        token = encrypt(plaintext)
    with pytest.warns(DeprecationWarning, match="decrypt.*deobfuscate"):
        assert decrypt(token) == plaintext


def test_encrypt_emits_warning_only_when_called():
    # Merely importing the deprecated aliases must not warn.
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        from openharness.auth import encrypt as _encrypt  # noqa: F401
