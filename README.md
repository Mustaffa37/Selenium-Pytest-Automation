# 🚀 Selenium Pytest Automation

## 📌 Overview
This project automates **login, logout, and forgot password** functionalities for the **OrangeHRM demo site** using **Selenium WebDriver** and **Pytest**.

## ✅ Requirements
Before running the tests, ensure you have the following installed:

- 🐍 **Python (>=3.7)**
- 🌐 **Google Chrome**
- 🛠️ **Chrome WebDriver** (Handled automatically via `webdriver_manager`)
- 📦 Required Python packages (listed in `requirements.txt`)

## 📥 Installation

### 1️⃣ Clone the Repository
```sh
git clone 
cd selenium-pytest-automation
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

## 🏃 Running Tests

Run all tests:
```sh
pytest tests/test_orangehrm.py
```

Run tests with detailed output:
```sh
pytest -v
```

Run only a specific test:
```sh
pytest tests/test_orangehrm.py -k test_login_valid
```

## 🔎 Test Cases

### 1️⃣ **Login Test (Valid Credentials)**
- **Test:** `test_login_valid`
- **Expected Result:** User successfully logs in and reaches the dashboard.

### 2️⃣ **Login Test (Invalid Credentials)**
- **Test:** `test_login_invalid`
- **Expected Result:** Error message `"Invalid credentials"` is displayed.

### 3️⃣ **Forgot Password Test** (Expected to Fail - `xfail` Marked)
- **Test:** `test_forgot_password`
- **Expected Result:** Clicking **"Forgot your password?"** redirects to the password reset page.

### 4️⃣ **Logout Test**
- **Test:** `test_logout`
- **Expected Result:** User successfully logs out and is redirected to the login page.

## 📝 Notes
- **❌ `xfail` Marking**: The Forgot Password test is marked with `@pytest.mark.xfail` because the locator may need verification.
- **⏳ Implicit & Explicit Waits:** Used to handle timing issues for element loading.
- **🔧 WebDriverManager:** Automatically installs the correct version of ChromeDriver.

## 🤝 Contributions
Feel free to contribute by improving test cases, adding new functionalities, or optimizing existing code.  
Create a **pull request** with your changes! 🚀

## 📜 License
This project is licensed under the **MIT License**.
```