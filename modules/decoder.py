def decode_bytecode(encoded_string, key):
    char_to_index = {}
    result = []
    rolling_key = key
    pos = -1
    str_index = 1
    while True:
        pos += 1
        char_to_index[encoded_string[str_index - 1]] = pos
        str_index += 1
        if pos == 15:
            pair_index = 0
            break
    total_len = len(encoded_string)
    current_pair = {}
    while str_index < total_len + 1:
        current_pair[pair_index] = encoded_string[str_index - 1]
        str_index += 1
        pair_index += 1
        if pair_index % 2 == 0:
            pair_index = 0
            try:
                high = char_to_index[current_pair[0]] or 0x00
            except:
                high = 0
            try:
                low = char_to_index[current_pair[1]] or 0x00
            except:
                low = 0
            result.append((((high) * 0x10) + (low) + rolling_key) % 0x100)
            rolling_key = key + rolling_key
    return bytes(result)

def find_key_and_decode(encoded):
    for key in range(100000):
        if key % 1000 == 0:
            print(f"[~] Trying key: {key}", end="\r")
        try:
            decoded = decode_bytecode(encoded, key)
            if b"MoonSec" in decoded:
                print(f"\n[+] Key found: {key}")
                return key, decoded
        except:
            pass
    return None, None
