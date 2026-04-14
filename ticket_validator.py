def validate_ticket(code):
    if not(isinstance(code, str)):
        raise TypeError("Code not inputted in string format")
    else:
        return len(code) == 8 and code[0:2] == "TK" and code[2:9].isdigit


def get_ticket_tier(code):
    if validate_ticket(code) == False:
        raise ValueError("Inserted ticket code is invalid")
    else:
        if int(code[2]) <= 3 and int(code[2]) >= 0:
            return "General"
        elif int(code[2]) <= 6 and int(code[2]) >= 4:
            return "VIP"
        else:
            return "Platinum"
        

def calculate_total(prices, discount=0):
    pass
