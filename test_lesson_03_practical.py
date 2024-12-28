import lesson_03_practical
from unittest.mock import patch

def test_eligibility_checker():
    with patch('builtins.input', return_value="18"):
        result = lesson_03_practical.check_eligibility()
        assert result == "You are eligible to drive.", "Eligibility check failed for age 18."

    with patch('builtins.input', return_value="16"):
        result = lesson_03_practical.check_eligibility()
        assert result == "You are not eligible to drive.", "Eligibility check failed for age 16."

def test_discount_calculator():
    result = lesson_03_practical.calculate_discount(150)
    assert result == 135.0, "Discount calculation failed for amount > $100."

    result = lesson_03_practical.calculate_discount(50)
    assert result == 47.5, "Discount calculation failed for amount <= $100."

def test_temperature_warning():
    with patch('builtins.input', return_value="35"):
        result = lesson_03_practical.temperature_warning()
        assert result == "Hot", "Temperature warning failed for temperature > 30."

    with patch('builtins.input', return_value="20"):
        result = lesson_03_practical.temperature_warning()
        assert result == "Warm", "Temperature warning failed for 15 <= temperature <= 30."

    with patch('builtins.input', return_value="10"):
        result = lesson_03_practical.temperature_warning()
        assert result == "Cold", "Temperature warning failed for temperature < 15."

def test_tax_bracket_calculator():
    result = lesson_03_practical.calculate_tax(5000)
    assert result == 0, "Tax calculation failed for income < $10,000."

    result = lesson_03_practical.calculate_tax(30000)
    assert result == 3000, "Tax calculation failed for $10,000 <= income <= $50,000."

    result = lesson_03_practical.calculate_tax(75000)
    assert result == 15000, "Tax calculation failed for income > $50,000."

def test_rock_paper_scissors():
    with patch('builtins.input', return_value="Rock"), patch('random.choice', return_value="Scissors"):
        result = lesson_03_practical.rock_paper_scissors()
        assert result == "You win! Rock beats Scissors.", "Rock-Paper-Scissors failed for Rock vs Scissors."

    with patch('builtins.input', return_value="Paper"), patch('random.choice', return_value="Rock"):
        result = lesson_03_practical.rock_paper_scissors()
        assert result == "You win! Paper beats Rock.", "Rock-Paper-Scissors failed for Paper vs Rock."

    with patch('builtins.input', return_value="Scissors"), patch('random.choice', return_value="Scissors"):
        result = lesson_03_practical.rock_paper_scissors()
        assert result == "It's a tie!", "Rock-Paper-Scissors failed for Scissors vs Scissors."
