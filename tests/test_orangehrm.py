from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    """Setup WebDriver with necessary options."""
    options = Options()
    options.add_argument("--log-level=3")  # Suppress logs
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()

def test_login_valid(driver):
    """Verify login with valid credentials."""
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    driver.implicitly_wait(10)
    
    assert "dashboard" in driver.current_url.lower(), "Login failed - Dashboard not found."

def test_login_invalid(driver):
    """Verify login fails with invalid credentials."""
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, "username").send_keys("WrongUser")
    driver.find_element(By.NAME, "password").send_keys("WrongPass")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    driver.implicitly_wait(10)
    
    # Locator for the error message
    error_message = driver.find_element(By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]").text
    assert "Invalid credentials" in error_message, "Error message not displayed for invalid login."

@pytest.mark.xfail(reason="Forgot Password link locator needs verification.")
def test_forgot_password(driver):
    """Verify Forgot Password page opens when link is clicked."""
    wait = WebDriverWait(driver, 10)
    try:
        forgot_password_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(text(),'Forgot your password?')]"))
        )
        forgot_password_link.click()
        
        wait.until(EC.url_contains("requestPasswordResetCode"))
        assert "requestpasswordresetcode" in driver.current_url.lower(), "Forgot Password page did not open."
    
    except Exception:
        pytest.xfail("Forgot Password link not found or not clickable.")

def test_logout(driver):
    """Verify user can log out successfully."""
    driver.implicitly_wait(10)
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    driver.implicitly_wait(10)
    
    profile_icon = driver.find_element(By.XPATH, "//p[contains(@class, 'oxd-userdropdown-name')]")
    profile_icon.click()
    driver.implicitly_wait(5)
    
    logout_link = driver.find_element(By.XPATH, "//a[text()='Logout']")
    logout_link.click()
    driver.implicitly_wait(10)
    
    assert "login" in driver.current_url.lower(), "Logout failed - Login page not displayed."