import subprocess

def test_lesson_03():
    result = subprocess.run(['python3', 'lesson_03.py'], capture_output=True, text=True)
    output = result.stdout.strip().splitlines()

    assert output[0] == "x is greater than 5", f"Failed TODO 1: {output[0]}"
    assert output[1] == "Adult", f"Failed TODO 2: {output[1]}"
    assert output[2] == "Good", f"Failed TODO 3: {output[2]}"
    assert output[3] == "Condition met", f"Failed TODO 4: {output[3]}"
    assert output[4] == "Hot", f"Failed TODO 5: {output[4]}"
    assert output[5] == "Take an umbrella", f"Failed TODO 6: {output[5]}"
    assert output[6] == "Odd and less than 30", f"Failed TODO 7: {output[6]}"
    assert output[7] == "Banana is available", f"Failed TODO 8: {output[7]}"
    assert output[8] == "You are eligible to vote", f"Failed TODO 9: {output[8]}"
    assert "corrected" in output[9], f"Failed TODO 10: {output[9]}"

    print("Lesson 3: All tests passed!")

if __name__ == "__main__":
    test_lesson_03()
