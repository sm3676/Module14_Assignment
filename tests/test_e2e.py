import time

BASE_PATH = "file:///C:/Users/Sharvani/OneDrive/Desktop/backend-assignment/module13-fastapi-jwt/frontend/"


def test_register(page):
    page.goto(BASE_PATH + "register.html")

    page.fill("#email", "test@test.com")
    page.fill("#password", "123456")

    page.click("button")

    page.wait_for_timeout(2000)

    assert "success" in page.inner_text("#msg").lower()


def test_login(page):
    page.goto(BASE_PATH + "login.html")

    page.fill("#email", "test@test.com")
    page.fill("#password", "123456")

    page.click("button")

    page.wait_for_timeout(2000)

    text = page.inner_text("#msg").lower()
    assert "success" in text

    # ⚠️ extract token from localStorage
    token = page.evaluate("localStorage.getItem('token')")
    assert token is not None



def test_calculation_flow(page):
    # 👉 open calculator page
    page.goto(BASE_PATH + "index.html")

    # 👉 login first to get token
    page.goto(BASE_PATH + "login.html")
    page.fill("#email", "test@test.com")
    page.fill("#password", "123456")
    page.click("button")
    page.wait_for_timeout(2000)

    token = page.evaluate("localStorage.getItem('token')")
    assert token is not None

    # 👉 go to calculator page
    page.goto(BASE_PATH + "index.html")

    # 👉 set token
    page.fill("#token", token)

    # ➕ ADD calculation
    page.fill("#op1", "5")
    page.fill("#op2", "3")
    page.select_option("#operation", "add")

    page.click("#addBtn")
    page.wait_for_timeout(2000)

    # 📄 LOAD calculations
    page.click("#loadBtn")
    page.wait_for_timeout(2000)

    content = page.content()

    # ✅ check result exists
    assert "8" in content

    # ❌ DELETE (click first delete button)
    page.click("text=Delete")
    page.wait_for_timeout(2000)