from hello_world import app


def test_root_path_returns_404():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 404
    assert b"Not Found" in response.data


def test_greeting_returns_200():
    client = app.test_client()
    response = client.get("/greeting")
    assert response.status_code == 200


def test_greeting_returns_html_content_type():
    client = app.test_client()
    response = client.get("/greeting")
    assert response.mimetype == "text/html"


def test_greeting_contains_expected_html():
    client = app.test_client()
    response = client.get("/greeting")
    assert b"Welcome to CI/CD 101 using GitHub Actions!" in response.data
