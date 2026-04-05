import os
import sys
from modules.extractor import extract_encoded_bytecode
from modules.decoder import find_key_and_decode
from modules.vm_parser import parse_vm
from modules.output import format_output, save_results

def resolve_path(user_input):
    if os.path.isabs(user_input):
        return user_input
    local_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), user_input)
    if os.path.exists(local_path):
        return local_path
    return user_input

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "deobfuscated")

    raw_input = input("Enter .lua file path: ").strip()
    file_path = resolve_path(raw_input)

    if not os.path.exists(file_path):
        print(f"[-] File not found: {file_path}")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8") as f:
        lua_source = f.read()

    print("[~] Extracting encoded bytecode...")
    encoded = extract_encoded_bytecode(lua_source)
    if not encoded:
        print("[-] Encoded bytecode not found.")
        sys.exit(1)

    print("[~] Brute-forcing key...")
    key, bytecode = find_key_and_decode(encoded)
    if not bytecode:
        print("[-] Key not found.")
        sys.exit(1)

    print("[~] Parsing VM...")
    api_calls, constants = parse_vm(bytecode)

    print("[~] Formatting output...")
    formatted = format_output(api_calls, constants, key)

    base_name = os.path.splitext(os.path.basename(file_path))[0]
    raw_path, parsed_path = save_results(base_name, bytecode, formatted, output_dir)

    print(f"[+] Raw bytecode: {raw_path}")
    print(f"[+] Deobfuscated: {parsed_path}")
