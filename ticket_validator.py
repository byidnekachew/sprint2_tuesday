def validate_ticket(code):
    if not(isinstance(code, str)):
        raise TypeError("Code not inputted in string format")
    else:
        return len(code) == 8 and code[0:2] == "TK" and if code[2:9].isdigit


def get_ticket_tier(code):
    pass


def calculate_total(prices, discount=0):
    pass
