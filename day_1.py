import re

def convert_word_to_number(word):
    match word:
        case "one":
            return "1"
        case "two":
            return "2"
        case "three":
            return "3"
        case "four":
            return "4"
        case "five":
            return "5"
        case "six":
            return "6"
        case "seven":
            return "7"
        case "eight":
            return "8"
        case "nine":
            return "9"
        case _:
            return word
        
def find_numbers(value):
    matches = re.finditer("(?=(\\d|one|two|three|four|five|six|seven|eight|nine))", value)
    return [str(match.group(1)) for match in matches]
        
        
def calibrtion_decoder(value):
    numbers = find_numbers(value)
    
    first_number = convert_word_to_number(numbers[0])
    last_number = convert_word_to_number(numbers[-1])

    combined_number = first_number + last_number

    return combined_number

total = 0

with open('day_1_input.txt', 'r') as file:
    for line in file:
        result = calibrtion_decoder(line)
        total += int(result)

print("total: " + str(total))