# 🧠 CORTEX - Linguistic Stealth Engine v1.0
**Invisible Data Embedding via Zero-Width Unicode Delimiters**

CORTEX is a specialized steganography tool designed to hide secret messages within ordinary text strings. It leverages non-printable Unicode characters (`\u200b` and `\u200c`) to encode binary data that remains invisible to the human eye and standard text editors.



## 🛡️ Technical Overview
* **Encoding:** Converts secret strings into binary, then maps bits to zero-width characters.
* **Invisibility:** The carrier text looks identical before and after encoding.
* **Compatibility:** Works across most modern platforms (WhatsApp, Discord, Email) that support UTF-8.

## 🚀 Installation
1. Clone the repo: `git clone https://github.com/your-username/CORTEX-STEALTH-ENGINE`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the engine: `python main.py`

## 🧪 Security Insight
Unlike standard encryption, CORTEX provides **security through obscurity**. Even if an adversary intercepts the message, they cannot see that a secret exists, bypassing linguistic analysis and standard surveillance filters.

> **Note:** For maximum security, combine with AES-256 encryption before encoding.
