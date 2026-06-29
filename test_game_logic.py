from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"


def test_hint_direction_below_secret_says_go_higher():
    # Bug: a guess BELOW the secret must tell the player to go HIGHER.
    # The glitch returned "Go LOWER" for guesses below the secret.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()
    assert "LOWER" not in message.upper()


def test_hint_direction_above_secret_says_go_lower():
    # Bug: a guess ABOVE the secret must tell the player to go LOWER.
    # The glitch returned "Go HIGHER" for guesses above the secret.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()
    assert "HIGHER" not in message.upper()
