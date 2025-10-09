import pytest

from dundie.utils.email import check_valid_email
from dundie.utils.user import generate_simple_password


@pytest.mark.unit
@pytest.mark.parametrize("address", ["bruno@rocha.com", "joe@doe.com"])
def test_positive_check_valid_email(address):
    """ensure email is valid"""
    assert check_valid_email(address) is True


@pytest.mark.unit
@pytest.mark.parametrize("address", [".@rocha.com", "joe@.com"])
def test_negative_check_valid_email(address):
    """ensure email is false"""
    assert check_valid_email(address) is False


@pytest.mark.unit
def test_generate_simple_password():
    """test generation of random simple passwords
    TODO: generate hashed complex passwords, encrypit it
    """
    passwords = []
    for _ in range(100):
        passwords.append(generate_simple_password(8))
    assert len(set(passwords)) == 100
