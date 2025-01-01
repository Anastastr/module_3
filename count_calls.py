calls = 0

def count_calls():
    global calls
    calls +=1

def string_info(str):
    count_calls()
    return (len(str), str.upper(), str.lower())
    lower_case = str.lower()

def is_containt(str, search_list):
    count_calls()
    str_lower = str.lower()
    return str.upper() in [s.upper() for s in search_list]

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_containt('Urban', ['ban', 'Banan', 'urBAN']))
print(is_containt('cycle', ['recysle', 'cyclic']))
print(calls)