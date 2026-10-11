"""Кошик (FR-05) — у розробці, запланований на версію 1.1.0."""
from flask import Blueprint, jsonify, request

bp = Blueprint("cart", __name__, url_prefix="/api/cart")
CART = []


@bp.post("")
def add_to_cart():
    item = request.get_json(silent=True) or {}
    if "product_id" not in item or "size" not in item:
        return jsonify(error="product_id і size обов'язкові"), 400
    CART.append({"product_id": item["product_id"], "size": item["size"], "qty": int(item.get("qty", 1))})
    return jsonify(items=CART), 201
