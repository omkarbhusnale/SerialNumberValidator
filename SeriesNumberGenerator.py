import re

def generate_next_serial(series_number):
    if series_number == 'SZZZZZZZZ':
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
        if prefix.startswith('S') and len(prefix) == 1:
            next_prefix = 'SA'
        elif prefix.isalpha() and len(prefix) == 2 and chr(ord(prefix[-1])) != 'Z':
            next_prefix = prefix[:-1]+chr(ord(prefix[-1]) + 1)
        elif prefix == 'SZ':
            next_prefix = 'SZA'
        else:
            return None 

        return next_prefix + (9 - len(next_prefix)) * "0"
    
    if number == 999999:
        if prefix.startswith('SZ') and len(prefix) == 2:
            next_prefix = 'SZA'
        elif prefix.isalpha() and len(prefix) == 3 and chr(ord(prefix[-1])) != 'Z':
            next_prefix = prefix[:-1]+chr(ord(prefix[-1]) + 1)
        elif prefix == 'SZZ':
            next_prefix = 'SZZA'
        else:
            return None 

        return next_prefix + (9 - len(next_prefix)) * "0"
    
    if number == 99999:
        if prefix.startswith('SZZ') and len(prefix) == 3:
            next_prefix = 'SZZA'
        elif prefix.isalpha() and len(prefix) == 4 and chr(ord(prefix[-1])) != 'Z':
            next_prefix = prefix[:-1]+chr(ord(prefix[-1]) + 1)
        elif prefix == 'SZZZ':
            next_prefix = 'SZZZA'
        else:
            return None 

        return next_prefix + (9 - len(next_prefix)) * "0"

    if number == 9999:
        if prefix.startswith('SZZZ') and len(prefix) == 4:
            next_prefix = 'SZZZA'
        elif prefix.isalpha() and len(prefix) == 5 and chr(ord(prefix[-1])) != 'Z':
            next_prefix = prefix[:-1]+chr(ord(prefix[-1]) + 1)
        elif prefix == 'SZZZZ':
            next_prefix = 'SZZZZA'
        else:
            return None 

        return next_prefix + (9 - len(next_prefix)) * "0"
    
    if number == 999:
        if prefix.startswith('SZZZZ') and len(prefix) == 5:
            next_prefix = 'SZZZZA'
        elif prefix.isalpha() and len(prefix) == 6 and chr(ord(prefix[-1])) != 'Z':
            next_prefix = prefix[:-1]+chr(ord(prefix[-1]) + 1)
        elif prefix == 'SZZZZZ':
            next_prefix = 'SZZZZZA'
        else:
            return None 

        return next_prefix + (9 - len(next_prefix)) * "0"
    
    if number == 99:
        if prefix.startswith('SZZZZZ') and len(prefix) == 6:
            next_prefix = 'SZZZZZA'
        elif prefix.isalpha() and len(prefix) == 7 and chr(ord(prefix[-1])) != 'Z':
            next_prefix = prefix[:-1]+chr(ord(prefix[-1]) + 1)
        elif prefix == 'SZZZZZZ':
            next_prefix = 'SZZZZZZA'
        else:
            return None 

        return next_prefix + (9 - len(next_prefix)) * "0"
    
    if number == 9:
        if prefix.startswith('SZZZZZZ') and len(prefix) == 7:
            next_prefix = 'SZZZZZA'
        elif prefix.isalpha() and len(prefix) == 8 and chr(ord(prefix[-1])) != 'Z':
            next_prefix = prefix[:-1]+chr(ord(prefix[-1]) + 1)
        elif prefix == 'SZZZZZZZ':
            next_prefix = 'SZZZZZZZA'
        else:
            return None 

        return next_prefix + (9 - len(next_prefix)) * "0"
    
    
    if len(prefix) == 9 and prefix.isalpha() and chr(ord(prefix[-1])) != 'Z':
        next_prefix = prefix[:-1]+chr(ord(prefix[-1]) + 1)
        
        return next_prefix + (9 - len(next_prefix)) * "0"

    no_of_zeros = (9 - len(prefix)) * "0"
    return f'{prefix}{(9 - len(prefix)-1) * "0"}{int(str(int(no_of_zeros) + number).zfill(len(no_of_zeros)))+1}'

# Example Usage:
current_serial = 'SZZZZZZZY'
next_serial = generate_next_serial(current_serial)
print(next_serial)

# def test_generate_next_serial():
#     # Test Case 1: Valid input with increment in the number part
#     assert generate_next_serial('S00000001') == 'S00000002'

#     # Test Case 2: Valid input with increment in the prefix and reset the number part
#     assert generate_next_serial('SZZZZZZZZ') is None  # The function should return None for the maximum value

#     # Test Case 3: Valid input with increment in the number part, testing for different lengths
#     assert generate_next_serial('SA0000000') == 'SA0000001'
#     assert generate_next_serial('SZA000000') == 'SZA000001'
#     assert generate_next_serial('SZZA00000') == 'SZZA00001'
#     assert generate_next_serial('SZZZA0000') == 'SZZZA0001'
#     assert generate_next_serial('SZZZZA000') == 'SZZZZA001'
#     assert generate_next_serial('SZZZZZA00') == 'SZZZZZA01'
#     assert generate_next_serial('SZZZZZZA0') == 'SZZZZZZA1'

#     # Test Case 4: Invalid input
#     #assert generate_next_serial('XYZ123') is None  # Invalid input, no match with the defined pattern

#     # Test Case 5: Testing for the maximum number in different prefix lengths
#     assert generate_next_serial('SZZZZZZZA') == 'SZZZZZZZB'
#     assert generate_next_serial('SZZZZZZZB') == 'SZZZZZZZC'


#     # Test Case 6: Testing for the maximum number with the maximum prefix length
#     #assert generate_next_serial('SZZZZZZZZZZZZZ') is None  # Invalid input, maximum prefix length exceeded

#     print("All test cases passed!")

# # Run the test cases
# test_generate_next_serial()
