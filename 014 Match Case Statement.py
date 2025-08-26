#01

day = 2
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid day")



#02
def check_vowel(char):
    match char.lower():
        case 'a' | 'e' | 'i' | 'o' | 'u':
            return "Vowel"
        case _:
            return "Consonant"

print(check_vowel("A"))  # Output: Vowel
print(check_vowel("B"))  # Output: Consonant






#03

def get_department(code):
    match code:
        case {"id": 101, "name": "HR"}:
            return "Human Resources"
        case {"id": 102, "name": "IT"}:
            return "Information Technology"
        case _:
            return "Unknown Department"

print(get_department({"id": 102, "name": "IT"}))  # Output: Information Technology






#04

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
