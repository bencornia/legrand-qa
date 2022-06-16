import random
import string
import pytest
from login_signup import login, signup

def create_unique_username(): 
    """Helper function to create unique username."""
    return "".join(random.choices(string.ascii_lowercase, k=20))

def get_url():
    """Helper function to pass in url"""
    return "https://www.demoblaze.com/"

class TestSignup:
    def test_valid_signup(self):
        assert signup(get_url(), create_unique_username(), "blah") == "Sign up successful."

    def test_empty_username_signup(self):
        assert signup(get_url(), "", "password") == "Please fill out Username and Password."

    def test_empty_password_signup(self):
        assert signup(get_url(), "username", "") == "Please fill out Username and Password."

    def test_existing_username_signup(self):
        assert signup(get_url(), "username", "password") == "This user already exist."

class TestLogin:
    def test_valid_login(self):
        # Sign up a user with a unique username
        username = create_unique_username()
        signup(get_url(), username, "password")

        # Log unique user in
        assert login(get_url(), username, "password") == f"Welcome {username}"
    
    def test_wrong_password(self):
        # Sign up a user with a unique username
        username = create_unique_username()
        password = create_unique_username()
        signup(get_url(), username, "password")

        # Attempt to sign in new user with wrong password.
        assert login(get_url(), username, password, False) == "Wrong password."

    def test_empty_username_login(self):
        assert login(get_url(), "", "password", False) == "Please fill out Username and Password."

    def test_empty_password_login(self):
        assert login(get_url(), "username", "", False) == "Please fill out Username and Password."

    def test_nonexistent_user_login(self):
        assert login(get_url(), create_unique_username(), "password", False) == "User does not exist."
 
if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", "test_login_signup.py"])
