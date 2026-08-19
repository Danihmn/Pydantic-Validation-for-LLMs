from app.data.order_db import order_db
from app.models.check_order_status_args import CheckOrderStatusArgs


def check_order_status(args: CheckOrderStatusArgs):
    """Simulate checking the status of a customer's order by
    order_id and email."""
    order = order_db.get(args.order_id)
    if not order:
        return {
            "order_id": args.order_id,
            "status": "not found",
            "estimated_delivery": None,
            "note": "order_id not found"
        }
    if args.email.lower() != order.get("email", "").lower():
        return {
            "order_id": args.order_id,
            "status": order["status"],
            "estimated_delivery": order["estimated_delivery"],
            "note": "order_id found but email mismatch"
        }
    return {
        "order_id": args.order_id,
        "status": order["status"],
        "estimated_delivery": order["estimated_delivery"],
        "note": "order_id and email match"
    }
