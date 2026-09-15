"""Unified authentication management for OpenHarness."""

from openharness.auth.flows import ApiKeyFlow, BrowserFlow, DeviceCodeFlow
from openharness.auth.manager import AuthManager
from openharness.auth.storage import (
    clear_provider_credentials,
    decrypt,
    deobfuscate,
    encrypt,
    load_credential,
    load_external_binding,
    obfuscate,
    store_credential,
    store_external_binding,
)

__all__ = [
    "AuthManager",
    "ApiKeyFlow",
    "BrowserFlow",
    "DeviceCodeFlow",
    "store_credential",
    "load_credential",
    "store_external_binding",
    "load_external_binding",
    "clear_provider_credentials",
    "obfuscate",
    "deobfuscate",
    # Deprecated — use obfuscate/deobfuscate instead.
    # Kept for backward compatibility; will be removed in a future version.
    "encrypt",
    "decrypt",
]
