import re

def generate_next_serial(series_number):
    if series_number == 'SZZZZZZZZ' or series_number == 'S00000000':
        return None

    number = None
    # Define a regular expression pattern to match the prefix and number
    pattern = re.compile(r'([A-Za-z]+)(\d+)')

    # Use the pattern to find matches in the input string
    match = pattern.match(series_number)

    if match:
        # Extract the prefix and number from the matched groups
        prefix = match.group(1)
        number_str = match.group(2)
        number = int(number_str)
    else:
        prefix = series_number
        number_str = ""

    #print("Prefix:", prefix)
    #print("Number:", number_str)

    if prefix == 'Z' and series_number != 'SZ':
        return None  # Invalid input

    if number == 9999999:
        next_prefix = prefix
        if prefix.startswith('S') and len(prefix) == 1:
            next_prefix = 'SA'
        elif prefix.isalpha() and len(prefix) == 2 and chr(ord(prefix[-1])) != 'Z':
            next_prefix = prefix[:-1]+chr(ord(prefix[-1]) + 1)
        elif prefix == 'SZ':
            next_prefix = 'SZA'
        elif prefix.isalpha() and chr(ord(prefix[-1])) != 'Z':
            no_of_zeros = (9 - len(prefix)) * "0"
            return f'{next_prefix}{str(int(no_of_zeros) + number + 1).zfill(len(no_of_zeros))}'

        return next_prefix + (9 - len(next_prefix)) * "0"
    
    if number == 999999:
        next_prefix = prefix
        if prefix.startswith('SZ') and len(prefix) == 2:
            next_prefix = 'SZA'
        elif prefix.isalpha() and len(prefix) == 3 and chr(ord(prefix[-1])) != 'Z':
            next_prefix = prefix[:-1]+chr(ord(prefix[-1]) + 1)
        elif prefix == 'SZZ':
            next_prefix = 'SZZA'
        elif prefix.isalpha() and chr(ord(prefix[-1])) != 'Z':
            no_of_zeros = (9 - len(prefix)) * "0"
            return f'{next_prefix}{str(int(no_of_zeros) + number + 1).zfill(len(no_of_zeros))}'

        return next_prefix + (9 - len(next_prefix)) * "0"
    
    if number == 99999:
        next_prefix = prefix
        if prefix.startswith('SZZ') and len(prefix) == 3:
            next_prefix = 'SZZA'
        elif prefix.isalpha() and len(prefix) == 4 and chr(ord(prefix[-1])) != 'Z':
            next_prefix = prefix[:-1]+chr(ord(prefix[-1]) + 1)
        elif prefix == 'SZZZ':
            next_prefix = 'SZZZA'
        elif prefix.isalpha() and chr(ord(prefix[-1])) != 'Z':
            no_of_zeros = (9 - len(prefix)) * "0"
            return f'{next_prefix}{str(int(no_of_zeros) + number + 1).zfill(len(no_of_zeros))}'

        return next_prefix + (9 - len(next_prefix)) * "0"

    if number == 9999:
        next_prefix = prefix
        if prefix.startswith('SZZZ') and len(prefix) == 4:
            next_prefix = 'SZZZA'
        elif prefix.isalpha() and len(prefix) == 5 and chr(ord(prefix[-1])) != 'Z':
            next_prefix = prefix[:-1]+chr(ord(prefix[-1]) + 1)
        elif prefix == 'SZZZZ':
            next_prefix = 'SZZZZA'
        elif prefix.isalpha() and chr(ord(prefix[-1])) != 'Z':
            no_of_zeros = (9 - len(prefix)) * "0"
            return f'{next_prefix}{str(int(no_of_zeros) + number + 1).zfill(len(no_of_zeros))}'

        return next_prefix + (9 - len(next_prefix)) * "0"
    
    if number == 999:
        next_prefix = prefix
        if prefix.startswith('SZZZZ') and len(prefix) == 5:
            next_prefix = 'SZZZZA'
        elif prefix.isalpha() and len(prefix) == 6 and chr(ord(prefix[-1])) != 'Z':
            next_prefix = prefix[:-1]+chr(ord(prefix[-1]) + 1)
        elif prefix == 'SZZZZZ':
            next_prefix = 'SZZZZZA'
        elif prefix.isalpha() and chr(ord(prefix[-1])) != 'Z':
            no_of_zeros = (9 - len(prefix)) * "0"
            return f'{next_prefix}{str(int(no_of_zeros) + number + 1).zfill(len(no_of_zeros))}'

        return next_prefix + (9 - len(next_prefix)) * "0"
    
    if number == 99:
        next_prefix = prefix
        if prefix.startswith('SZZZZZ') and len(prefix) == 6:
            next_prefix = 'SZZZZZA'
        elif prefix.isalpha() and len(prefix) == 7 and chr(ord(prefix[-1])) != 'Z':
            next_prefix = prefix[:-1]+chr(ord(prefix[-1]) + 1)
        elif prefix == 'SZZZZZZ':
            next_prefix = 'SZZZZZZA'
        elif prefix.isalpha() and chr(ord(prefix[-1])) != 'Z':
            no_of_zeros = (9 - len(prefix)) * "0"
            return f'{next_prefix}{str(int(no_of_zeros) + number + 1).zfill(len(no_of_zeros))}'

        return next_prefix + (9 - len(next_prefix)) * "0"
    
    if number == 9:
        next_prefix = prefix
        if prefix.startswith('SZZZZZZ') and len(prefix) == 7:
            next_prefix = 'SZZZZZA'
        elif prefix.isalpha() and len(prefix) == 8 and chr(ord(prefix[-1])) != 'Z':
            next_prefix = prefix[:-1]+chr(ord(prefix[-1]) + 1)
        elif prefix == 'SZZZZZZZ':
            next_prefix = 'SZZZZZZZA'
        elif prefix.isalpha() and chr(ord(prefix[-1])) != 'Z':
            no_of_zeros = (9 - len(prefix)) * "0"
            return f'{next_prefix}{str(int(no_of_zeros) + number + 1).zfill(len(no_of_zeros))}'

        return next_prefix + (9 - len(next_prefix)) * "0"
    
    
    if len(prefix) == 9 and prefix.isalpha() and chr(ord(prefix[-1])) != 'Z':
        next_prefix = prefix[:-1]+chr(ord(prefix[-1]) + 1)
        return next_prefix + (9 - len(next_prefix)) * "0"

    no_of_zeros = (9 - len(prefix)) * "0"
    return f'{prefix}{str(int(no_of_zeros) + number + 1).zfill(len(no_of_zeros))}'


# Example Usage:
li = [
    'S00000000', 'S00000001', 'S00000009', 'S09999999', 
    'SA0000000', 'SB0000099', 'SA9999999', 'SZ9999999', 
    'SZA000000', 'SZB000009', 'SZB999999', 'SZZ999999',
    'SZZA00000', 'SZZB00009', 'SZZA99999', 'SZZZ99999',
    'SZZZA0000', 'SZZZB0000', 'SZZZA9999', 'SZZZZ9999',
    'SZZZZA000', 'SZZZZB009', 'SZZZZA999', 'SZZZZ9999',
    'SZZZZZA00', 'SZZZZZB09', 'SZZZZZA99', 'SZZZZZZ99',
    'SZZZZZZA0', 'SZZZZZZA0', 'SZZZZZZA9', 'SZZZZZZZ0',
    'SZZZZZZZ9', 'SZZZZZZZA', 'SZZZZZZZY', 'SZZZZZZZZ'
    ]
res = []

for i in range(len(li)):
    serialNo = generate_next_serial(li[i])
    if serialNo is not None:
        res.append(serialNo)
    else: 
        res.append("Wrong Input")

for i in range(len(res)):
    print(li[i] + " --> " + res[i])
