ROBLOX_GLOBALS = {
    'game', 'workspace', 'script', 'wait', 'spawn', 'delay',
    'print', 'warn', 'error', 'pcall', 'xpcall', 'pairs', 'ipairs',
    'tostring', 'tonumber', 'type', 'math', 'string', 'table',
    'Instance', 'Vector3', 'CFrame', 'Color3', 'UDim2', 'UDim',
    'Enum', 'task', 'Players', 'RunService', 'UserInputService',
    'ReplicatedStorage', 'TweenService', 'HttpService', 'loadstring'
}

LUA_KEYWORDS = {
    'function', 'local', 'return', 'if', 'then', 'else', 'elseif',
    'end', 'while', 'do', 'for', 'in', 'repeat', 'until', 'break',
    'true', 'false', 'nil', 'and', 'or', 'not'
}

def extract_strings(data):
    strings = []
    i = 0
    while i < len(data):
        if 0x20 <= data[i] <= 0x7E:
            j = i
            while j < len(data) and 0x20 <= data[j] <= 0x7E:
                j += 1
            if j - i >= 3:
                strings.append((i, data[i:j].decode('ascii')))
            i = j
        else:
            i += 1
    return strings

def parse_vm(data):
    strings = extract_strings(data)
    seen = set()
    api_calls = []
    constants = []
    for offset, s in strings:
        if s in seen:
            continue
        seen.add(s)
        if s in LUA_KEYWORDS:
            continue
        if s in ROBLOX_GLOBALS:
            api_calls.append(s)
        elif any(c.isalpha() for c in s):
            constants.append(s)
    return api_calls, constants
