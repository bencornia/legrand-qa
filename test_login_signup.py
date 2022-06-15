import pytest
from login_signup import login, signup


class TestSignup:
    def test_valid_signup(self):
        assert signup("https://www.demoblaze.com/", "xxxxyyy1234", "blah") == "Sign up successful."

    def test_empty_username_signup(self):
        assert signup("https://www.demoblaze.com/", "", "password") == "Please fill out Username and Password."

    def test_empty_password_signup(self):
        assert signup("https://www.demoblaze.com/", "username", "") == "Please fill out Username and Password."

    def test_existing_username_signup(self):
        assert signup("https://www.demoblaze.com/", "bencor", "password") == "This user already exist."
    


class TestLogin:
    def test_valid_login(self):
        username = "bencor"
        assert login("https://www.demoblaze.com/", username, "abc") == f"Welcome {username}"
    
    def test_wrong_password(self):
        assert login("https://www.demoblaze.com/", "bencor", "password", False) == "Wrong password."

    def test_empty_username_login(self):
        assert login("https://www.demoblaze.com/", "", "password", False) == "Please fill out Username and Password."

    def test_empty_password_login(self):
        assert login("https://www.demoblaze.com/", "username", "", False) == "Please fill out Username and Password."


   

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", "test_login_signup.py"])
