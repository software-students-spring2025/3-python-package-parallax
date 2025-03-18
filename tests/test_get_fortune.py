import pytest
from fortune_teller.get_fortune import get_fortune

class TestGetFortune:
    @pytest.mark.parametrize("category", ["tech", "startup", "open source", "ai", "career"])
    def test_returns_str(self, category):
        """Check if the value that is returned is a string."""
        fortune_returned = get_fortune(category)
        assert isinstance(fortune_returned, str), f"String is expected here."

    def test_valid_tech(self):
        """Check if the valid only category tech returns one of the listed fortunes."""
        valid_only_tech = {
            "You will fix a bug... but create two new ones.",
            "Your commit messages will inspire thousands of developers.",
            "Your code will compile on the first try... eventually.",
            "Rubber duck debugging will save your day—just don't question the duck.",
            "A segfault in your future? Fear not, for logs will guide you.",
            "You will spend more time reading logs than writing code."
        }
        fortune_returned = get_fortune("tech")
        assert fortune_returned in valid_only_tech, (f"Valid fortunes are {valid_only_tech}, got {fortune_returned}")
    
    def test_value_error_raise(self):
        """Check if an invalid category raises a Valueerror and prompts the user to pick a valid one instead."""
        invalid_only = "internships"
        with pytest.raises(ValueError) as exc_info:
            get_fortune(invalid_only)
        error_text = str(exc_info.value)
        assert f"Sorry but '{invalid_only}' is not a category." in error_text
        assert f"Please pick on from this list:" in error_text


