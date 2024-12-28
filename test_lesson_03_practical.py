import subprocess

def test_lesson_03_practical():
    result = subprocess.run(['python3', 'lesson_03_practical.py'], capture_output=True, text=True)
    output = result.stdout.strip().splitlines()

    # Detailed checks for each TODO
    try:
        assert "eligible" in output[0], "TODO 1 Failed: Eligibility checker didn't print correct message."
        print("TODO 1 Passed: Eligibility checker works.")
    except AssertionError as e:
        print(e)

    try:
        assert "final price" in output[1], "TODO 2 Failed: Discount calculator didn't return final price."
        print("TODO 2 Passed: Discount calculator works.")
    except AssertionError as e:
        print(e)

    try:
        assert any(status in output[2] for status in ["Hot", "Warm", "Cold"]), "TODO 3 Failed: Temperature warning incorrect."
        print("TODO 3 Passed: Temperature warning works.")
    except AssertionError as e:
        print(e)

    try:
        assert "tax" in output[3], "TODO 4 Failed: Tax bracket calculator did not return tax details."
        print("TODO 4 Passed: Tax bracket calculator works.")
    except AssertionError as e:
        print(e)

    try:
        assert any(word in output[4] for word in ["wins", "Draw"]), "TODO 5 Failed: Rock-Paper-Scissors game logic incorrect."
        print("TODO 5 Passed: Rock-Paper-Scissors game works.")
    except AssertionError as e:
        print(e)

    print("Testing completed for Lesson 3 Practical Examples.")

if __name__ == "__main__":
    test_lesson_03_practical()
