def is_weekend(day):
    match day:
        case "sunday":
            return True
        case "monday":
            return False
        case "tuesday":
            return False
        case "wednesdat":
            return False
        case "friday":
            return False
        case "saturday":
            return True
        case _:
            return False
        


print(is_weekend(input("enter a day:  ")))