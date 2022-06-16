# Test Cases

- Video Demo: [youtube.com](https://www.youtube.com/watch?v=jVasRJYOZ2Q)
- Website: [demoblaze.com](https://www.demoblaze.com)

## Sign Up Flow

| No. | Test Case                                                | Outcome  |
| :-- | :------------------------------------------------------- | :------: |
| 1   | Verify user can sign up with username/password.          | Positive |
| 2   | Verify user cannot leave empty username when signing up. | Negative |
| 3   | Verify user cannot leave empty password when signing up. | Negative |
| 4   | Verify user cannot sign up with existing username.       | Negative |

## Login Flow

| No. | Test Case                                            | Outcome  |
| :-- | :--------------------------------------------------- | :------: |
| 1   | Verify user can log in with valid username/password. | Positive |
| 2   | Verify user cannot log in with wrong password.       | Negative |
| 3   | Verify user cannot log in with empty username.       | Negative |
| 4   | Verify user cannot log in with empty password.       | Negative |
| 5   | Verify nonexistent user.                             | Negative |

## Usage

1. Set PATH variable (line 21 of login_signup.py).
2. Navigate to directory root and run following commands in terminal.

```powershell
# Set up virtual environment
py -m venv venv

# Activate venv linux
source venv/bin/activate

# Activate venv powershell
venv\Scripts\Activate.ps1

# Install required packages.
pip install -r requirements.txt

# Run tests
py test_login_signup.py

```

## Requirements

- Python 3.10.2
- Chrome Version: 102.0.5005.115
- [ChromeDriver 102.0.5005.61](https://chromedriver.chromium.org/downloads)
