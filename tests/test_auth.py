def test_login_success(client):
    r = client.post("/api/auth/login", json={"email": "student@modaline.ua", "password": "Passw0rd!"})
    assert r.status_code == 200
    assert r.get_json()["token_type"] == "bearer"


def test_login_wrong_password(client):
    r = client.post("/api/auth/login", json={"email": "student@modaline.ua", "password": "wrong"})
    assert r.status_code == 401
