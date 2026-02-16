"""Zid SDK Demo API."""

from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel
from zid import ZidClient

from app.auth import router as auth_router
from app.config import settings, get_tokens
from app.errors import register_exception_handlers
from app.templates import LANDING, DASHBOARD

app = FastAPI(title="Zid SDK Demo")
app.include_router(auth_router)
register_exception_handlers(app)


# =============================================================================
# SDK Examples
# =============================================================================

@app.get("/api/store")
def get_store():
    tokens = get_tokens()
    if not tokens:
        raise HTTPException(401, "Not authenticated")
    
    client = ZidClient(
        base_url=settings.zid_api_base_url,
        authorization_token=tokens["authorization_token"],
        access_token=tokens["access_token"],
    )
    return client.stores.get_profile()


@app.get("/api/customers")
def get_customers():
    tokens = get_tokens()
    if not tokens:
        raise HTTPException(401, "Not authenticated")
    
    client = ZidClient(
        base_url=settings.zid_api_base_url,
        authorization_token=tokens["authorization_token"],
        access_token=tokens["access_token"],
    )
    return {"data": list(client.customers.list())}


@app.get("/api/orders")
def get_orders():
    tokens = get_tokens()
    if not tokens:
        raise HTTPException(401, "Not authenticated")
    
    client = ZidClient(
        base_url=settings.zid_api_base_url,
        authorization_token=tokens["authorization_token"],
        access_token=tokens["access_token"],
    )
    return {"data": list(client.orders.list())}


@app.get("/api/orders/{order_id}")
def get_order(order_id: int):
    tokens = get_tokens()
    if not tokens:
        raise HTTPException(401, "Not authenticated")
    
    client = ZidClient(
        base_url=settings.zid_api_base_url,
        authorization_token=tokens["authorization_token"],
        access_token=tokens["access_token"],
    )
    return client.orders.get(order_id)


class WebhookRequest(BaseModel):
    event: str
    target_url: Optional[str] = None


@app.get("/api/webhooks")
def list_webhooks():
    tokens = get_tokens()
    if not tokens:
        raise HTTPException(401, "Not authenticated")
    
    client = ZidClient(
        base_url=settings.zid_api_base_url,
        authorization_token=tokens["authorization_token"],
        access_token=tokens["access_token"],
    )
    return {"data": list(client.webhooks.list())}


@app.post("/api/webhooks")
def create_webhook(body: WebhookRequest):
    tokens = get_tokens()
    if not tokens:
        raise HTTPException(401, "Not authenticated")
    
    client = ZidClient(
        base_url=settings.zid_api_base_url,
        authorization_token=tokens["authorization_token"],
        access_token=tokens["access_token"],
    )
    return client.webhooks.create(event=body.event, target_url=body.target_url)


@app.delete("/api/webhooks/{webhook_id}")
def delete_webhook(webhook_id: int):
    tokens = get_tokens()
    if not tokens:
        raise HTTPException(401, "Not authenticated")
    
    client = ZidClient(
        base_url=settings.zid_api_base_url,
        authorization_token=tokens["authorization_token"],
        access_token=tokens["access_token"],
    )
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
