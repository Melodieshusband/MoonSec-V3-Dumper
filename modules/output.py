import os

def format_output(api_calls, constants, key):
    lines = []
    lines.append(f"--[[ MoonSec V3 Deobfuscated ]]")
    lines.append(f"--[[ Key: {key} ]]")
    lines.append("")
    if api_calls:
        lines.append("--[[ Roblox API Calls Detected ]]")
        for call in sorted(set(api_calls)):
            lines.append(f"-- {call}")
        lines.append("")
    if constants:
        lines.append("--[[ String Constants ]]")
        for const in constants:
            safe = const.replace('"', '\\"')
            lines.append(f'-- "{safe}"')
        lines.append("")
    lines.append("--[[ Raw Constant Table ]]")
    lines.append("local _constants = {")
    for const in constants:
        safe = const.replace('"', '\\"')
        lines.append(f'    "{safe}",')
    lines.append("}")
    lines.append("")
    lines.append("--[[ Roblox API Table ]]")
    lines.append("local _api = {")
    for call in sorted(set(api_calls)):
        lines.append(f'    "{call}",')
    lines.append("}")
    return "\n".join(lines)

def save_results(base_name, bytecode, formatted, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    raw_path = os.path.join(output_dir, f"{base_name}_bytecode.lua")
    with open(raw_path, "wb") as f:
        f.write(bytecode)
    parsed_path = os.path.join(output_dir, f"{base_name}_deobfuscated.lua")
    with open(parsed_path, "w", encoding="utf-8") as f:
        f.write(formatted)
    return raw_path, parsed_path
