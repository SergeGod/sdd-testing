"""Exercise 5: parametrize, for covering many cases with one test body."""

import pytest

from orderflow.pricing import calculate_total_price
from orderflow.validation import validate_email


class TestPytestFeatures:
    """Same assertions as Exercise 1, driven by a table of cases."""

    @pytest.mark.parametrize(
        "price,quantity,discount,expected",
        [
            (10.0, 5, 0, 50.0),
            (10.0, 5, 10, 45.0),
            (100.0, 2, 25, 150.0),
            (50.0, 10, 20, 400.0),
            (25.0, 4, 50, 50.0),
        ],
    )
    def test_calculate_total_price_parametrized(
        self, price, quantity, discount, expected
    ):
        """Test multiple pricing scenarios from one test body."""
        assert calculate_total_price(price, quantity, discount) == pytest.approx(
            expected
        )

    @pytest.mark.parametrize(
        "email,expected",
        [
            ("user@example.com", True),
            ("test@mail.example.org", True),
            ("invalid", False),
            ("no-at-sign.com", False),
            ("@example.com", False),
            ("user@", False),
            ("", False),
        ],
    )
    def test_validate_email_parametrized(self, email, expected):
        """Test email validation with multiple cases."""
        assert validate_email(email) is expected

    @pytest.mark.parametrize(
        "price,quantity,discount,message",
        [
            pytest.param(-10.0, 5, 0, "must be non-negative", id="negative-price"),
            pytest.param(10.0, -5, 0, "must be non-negative", id="negative-quantity"),
            pytest.param(10.0, 5, 101, "must be between 0 and 100", id="discount-over-100"),
            pytest.param(10.0, 5, -10, "must be between 0 and 100", id="negative-discount"),
        ],
    )
    def test_calculate_total_price_invalid_inputs(
        self, price, quantity, discount, message
    ):
        """Test every ValueError path from one test body."""
        with pytest.raises(ValueError, match=message):
            calculate_total_price(price, quantity, discount)
