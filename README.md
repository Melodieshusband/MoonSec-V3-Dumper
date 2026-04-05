# MoonSec V3 Deobfuscator

> **Note:** Only README was written by Claude (AI by Anthropic) because the author is not great at writing descriptions in English.

A Python-based tool for deobfuscating Lua scripts protected with MoonSec V3.

## How It Works

1. Extracts the encrypted bytecode from the obfuscated script
2. Brute-forces the decryption key
3. Parses the MoonSec VM bytecode
4. Outputs readable constants, API calls, and string table

## Requirements

- Python 3.x

## Usage

1. Place your obfuscated `.lua` file in the project folder
2. Run:
```bash
python deobfuscator.py
```
3. Enter the file name or full path when prompted
4. Results are saved to the `deobfuscated/` folder

## Output Files

- `filename_bytecode.lua` — raw decoded bytecode
- `filename_deobfuscated.lua` — parsed constants and API calls

## File Structure

```
MoonSec-V3/
├── deobfuscator.py
├── README.md
├── modules/
│   ├── __init__.py
│   ├── extractor.py
│   ├── decoder.py
│   ├── vm_parser.py
│   └── output.py
└── deobfuscated/
```

## Notes

- Only works on scripts protected with MoonSec V3
- Key search limit is 100,000 iterations
- Does not fully reconstruct source code — outputs constants and API usage
- For educational and research purposes only
