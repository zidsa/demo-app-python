"""Zid SDK Demo API."""

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse

# Simplified imports - all primary models at root level
from zid import ZidClient, Order, Customer, Store, Webhook, WebhookCreate

from app.auth import router as auth_router
from app.config import settings, get_tokens
from app.errors import register_exception_handlers
from app.templates import LANDING, DASHBOARD

app = FastAPI(title="Zid SDK Demo")
app.include_router(auth_router)
register_exception_handlers(app)


def get_client() -> ZidClient:
    """Create authenticated ZidClient."""
    tokens = get_tokens()
    if not tokens:
        raise HTTPException(401, "Not authenticated")
    return ZidClient(
        base_url=settings.zid_api_base_url,
        authorization=tokens["authorization_token"],
        store_token=tokens["access_token"],
    )


# =============================================================================
# SDK Examples
# =============================================================================

@app.get("/api/store")
def get_store():
    client = get_client()
    return client.stores.get_profile()


@app.get("/api/customers")
def get_customers():
    client = get_client()
    return {"data": list(client.customers.list())}


@app.get("/api/orders")
def get_orders():
    client = get_client()
    return {"data": list(client.orders.list())}


@app.get("/api/orders/{order_id}")
def get_order(order_id: int):
    client = get_client()
    return client.orders.get(order_id)


@app.get("/api/webhooks")
def list_webhooks():
    client = get_client()
    return {"data": list(client.webhooks.list())}


@app.post("/api/webhooks")
def create_webhook(body: WebhookCreate):
    """Create webhook using SDK model directly."""
    client = get_client()
    return client.webhooks.create(event=body.event, target_url=body.target_url)


@app.delete("/api/webhooks/{webhook_id}")
def delete_webhook(webhook_id: int):
    client = get_client()
    client.webhooks.delete(webhook_id)
    return {"status": "deleted"}


# =============================================================================
# Pages
# =============================================================================

@app.get("/", response_class=HTMLResponse)
async def landing():
    if get_tokens():
        return RedirectResponse("/dashboard")
    return LANDING


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    if not get_tokens():
        return RedirectResponse("/")
    return DASHBOARD
