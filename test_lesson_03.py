import lesson_03

def test_basic_if_condition():
    assert lesson_03.x == 10, "Variable 'x' should be 10."
    assert lesson_03.if_result == "x is greater than 5", "Basic if condition result is incorrect."

def test_if_else_statement():
    assert lesson_03.age == 20, "Variable 'age' should be 20."
    assert lesson_03.if_else_result == "Adult", "if-else statement result is incorrect."

def test_if_elif_else_ladder():
    assert lesson_03.score == 75, "Variable 'score' should be 75."
    assert lesson_03.if_elif_else_result == "Good", "if-elif-else ladder result is incorrect."

def test_logical_operators_conditionals():
    assert lesson_03.a is True, "Variable 'a' should be True."
    assert lesson_03.b is False, "Variable 'b' should be False."
    assert lesson_03.logical_condition_result == "Condition met", "Logical operators conditional result is incorrect."

def test_nested_if():
    assert lesson_03.temperature == 30, "Variable 'temperature' should be 30."
    assert lesson_03.nested_if_result == "Hot", "Nested if condition result is incorrect."

def test_ternary_conditional_operator():
    assert lesson_03.is_raining is True, "Variable 'is_raining' should be True."
    assert lesson_03.ternary_result == "Take an umbrella", "Ternary conditional operator result is incorrect."

def test_complex_conditionals():
    assert lesson_03.number == 23, "Variable 'number' should be 23."
    assert lesson_03.complex_condition_result == "Odd and less than 30", "Complex conditionals result is incorrect."

def test_checking_membership():
    assert lesson_03.fruits == ['apple', 'banana', 'cherry'], "Variable 'fruits' should contain ['apple', 'banana', 'cherry']."
    assert lesson_03.membership_result == "Banana is available", "Checking membership result is incorrect."

def test_conditional_with_input(monkeypatch):
    # Simulate user input for testing
    monkeypatch.setattr('builtins.input', lambda _: "18")
    lesson_03.check_voting_eligibility()
    assert lesson_03.voting_result == "You are eligible to vote", "Conditional with input result is incorrect."

def test_debugging_conditional():
    assert lesson_03.debugged_condition_result == True, "Debugged conditional logic is incorrect."
