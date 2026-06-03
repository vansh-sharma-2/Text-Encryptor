# Text-Encryptor

A terminal-based text encoder/decoder using a rotating substitution cipher.

## How It Works

Characters are scrambled through 4 shifting lookup lists, driven by a 6-digit numeric **code** that acts as a key. The code changes with every character encoded/decoded, so the same letter maps to something different each time.

## Usage

Run the script:
```
python main.py
```

Then pick an option:
```
1. encode
2. decode
3. quit
```

Enter your 8-digit code (e.g. `00120000`), then type any text to encode or decode it.

Type `"back"` to return to the menu, or `"quit"` to exit.

## Notes

- Supported characters: `a–z`, `0–9`, and space
- Both sides must use the **same starting code** to encode/decode correctly
- Codes are case-sensitive; unsupported characters pass through unchanged
