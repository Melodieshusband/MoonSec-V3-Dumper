def extract_encoded_bytecode(lua_source):
    string_list = []
    current = ""
    quote_parity = 0
    for segment in lua_source.split('"'):
        if quote_parity % 2 == 1:
            current += segment
        quote_parity += 1
        if not current.endswith("\\"):
            string_list.append(current)
            current = ""
        else:
            current = current[:-1] + '"'
            quote_parity -= 1
    decoder_var = ""
    for string in string_list:
        is_key_arg = False
        if string == "":
            continue
        if all([ch.isdigit() for ch in lua_source.split(string)[0].split("(")[-1].split(',')[0]]):
            decoder_var = lua_source.split(string)[0].split("(")[-2][-1]
            is_key_arg = True
        if decoder_var != "" and f'{decoder_var}(' in lua_source[lua_source.find(f'"{string}')-6:lua_source.find(f'"{string}')] and len(string) > 300 and not is_key_arg:
            return string
    return None
