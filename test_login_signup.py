import pytest
from login_signup import login

class TestLoginSignup:
    def test_login(self):
        assert login("https://www.demoblaze.com/", "bencor", "abc") == "Welcome bencor"

if __name__ == "__main__":
    pytest.main(["-v", "--tb=line", "-rN", "test_login_signup.py"])
