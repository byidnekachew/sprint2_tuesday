import pytest
from ticket_validator import validate_ticket, get_ticket_tier, calculate_total

def test_correct_ticket_start():
    valid = validate_ticket("TK573917")
    assert valid

def test_invalid_ticket_start():
    invalid = validate_ticket("JA573917")
    assert invalid == False

def test_invalid_code_length():
    invalid = validate_ticket("TK57397")
    assert invalid == False

def test_nonstring_code():
    with pytest.raises(TypeError):
        validate_ticket(57391767)


def test_ticket_tier_valerr():
    with pytest.raises(ValueError):
        get_ticket_tier("JA573917")

def test_ticket_tier_platinum_upper():
    tier = get_ticket_tier("TK973917")
    assert tier == "Platinum"

def test_ticket_tier_platinum_lower():
    tier = get_ticket_tier("TK773917")
    assert tier == "Platinum"

def test_ticket_tier_VIP_upper():
    tier = get_ticket_tier("TK673917")
    assert tier == "VIP"

def test_ticket_tier_VIP_lower():
    tier = get_ticket_tier("TK473917")
    assert tier == "VIP"

def test_ticket_tier_general_upper():
    tier = get_ticket_tier("TK373917")
    assert tier == "General"

def test_ticket_tier_general_lower():
    tier = get_ticket_tier("TK073917")
    assert tier == "General"


