# Zid SDK Demo

A minimal FastAPI starter showing how to integrate the [Zid Python SDK](https://github.com/zid-sa/zid-python-sdk).

**Connect your store → See your data → Copy the code.**

## Quick Start

```bash
# Install
uv sync

# Configure (add your Zid OAuth credentials)
cp .env.example .env

# Run
uvicorn app.main:app --reload
```

Open http://localhost:8000 and click "Connect Your Zid Store".

## What You'll See

After authenticating, you get a dashboard showing:
- Your store profile
- Recent orders  
- Customer data

Plus the exact SDK code that powers it:

```python
from zid import ZidClient

client = ZidClient(
    authorization="...",
    store_token="...",
)

store = client.stores.get_profile()
customers = client.customers.list()
orders = client.orders.list()
```

## OAuth Setup with ngrok

Zid OAuth needs a public URL:

```bash
ngrok http 8000
```

Update `.env`:
```
ZID_REDIRECT_URI=https://your-ngrok-url.ngrok.io/auth/callback
```

Add the same URL to your Zid app settings.

## API Endpoints

| Endpoint | SDK Method |
|----------|------------|
| `GET /api/store` | `client.stores.get_profile()` |
| `GET /api/customers` | `client.customers.list()` |
| `GET /api/orders` | `client.orders.list()` |
| `GET /api/orders/{id}` | `client.orders.get(id)` |
| `GET /api/webhooks` | `client.webhooks.list()` |
| `POST /api/webhooks` | `client.webhooks.create()` |
| `DELETE /api/webhooks/{id}` | `client.webhooks.delete()` |

## Project Structure

```
├── app/
│   ├── main.py       # SDK examples + pages
│   ├── auth.py       # OAuth flow
│   ├── config.py     # Settings + token storage
│   ├── errors.py     # SDK exception handlers
│   └── templates.py  # HTML pages
├── .env.example
├── pyproject.toml
└── README.md
```

## License

MIT
