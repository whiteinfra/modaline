"""Каталог товарів (FR-01, FR-02)."""
from flask import Blueprint, jsonify, request

bp = Blueprint("catalog", __name__, url_prefix="/api/products")

PRODUCTS = [
    {"id": 1, "name": "Футболка базова", "category": "футболки", "sizes": ["S", "M", "L"], "price": 399},
    {"id": 2, "name": "Худі оверсайз", "category": "худі", "sizes": ["M", "L", "XL"], "price": 1290},
    {"id": 3, "name": "Джинси slim", "category": "джинси", "sizes": ["S", "M"], "price": 1550},
    {"id": 4, "name": "Футболка поло", "category": "футболки", "sizes": ["L", "XL"], "price": 690},
]


@bp.get("")
def list_products():
    category = request.args.get("category")
    size = request.args.get("size")
    items = [p for p in PRODUCTS
             if (not category or p["category"] == category) and (not size or size in p["sizes"])]
    return jsonify(items=items, total=len(items))


@bp.get("/<int:product_id>")
def get_product(product_id):
    for p in PRODUCTS:
        if p["id"] == product_id:
            return jsonify(p)
    return jsonify(error="Товар не знайдено"), 404
