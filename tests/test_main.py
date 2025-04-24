from app.main import greet

def test_greet():
    assert greet() == "CI/CD is working beautifully!"
