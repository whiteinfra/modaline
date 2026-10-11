def test_list_all_products(client):
    r = client.get("/api/products")
    assert r.status_code == 200
    assert r.get_json()["total"] == 4


def test_filter_by_category_and_size(client):
    r = client.get("/api/products?category=футболки&size=L")
    names = [p["name"] for p in r.get_json()["items"]]
    assert names == ["Футболка базова", "Футболка поло"]


def test_product_not_found(client):
    assert client.get("/api/products/999").status_code == 404
