"""SDK exception handlers."""

from fastapi import FastAPI
from fastapi.responses import JSONResponse

try:
    from zid.exceptions import (
        ZidAuthenticationError, ZidAuthorizationError, ZidConnectionError,
        ZidNotFoundError, ZidRateLimitError, ZidServerError, ZidValidationError,
    )
    SDK_EXCEPTIONS = True
except ImportError:
    SDK_EXCEPTIONS = False


def register_exception_handlers(app: FastAPI):
    if not SDK_EXCEPTIONS:
        return
    
    @app.exception_handler(ZidAuthenticationError)
    async def _(r, e): return JSONResponse(401, {"error": "auth_error", "message": str(e)})
    @app.exception_handler(ZidAuthorizationError)
    async def _(r, e): return JSONResponse(403, {"error": "forbidden", "message": str(e)})
    @app.exception_handler(ZidNotFoundError)
    async def _(r, e): return JSONResponse(404, {"error": "not_found", "message": str(e)})
    @app.exception_handler(ZidValidationError)
    async def _(r, e): return JSONResponse(422, {"error": "validation", "message": str(e)})
    @app.exception_handler(ZidRateLimitError)
    async def _(r, e): return JSONResponse(429, {"error": "rate_limit", "message": str(e)})
    @app.exception_handler(ZidServerError)
    async def _(r, e): return JSONResponse(502, {"error": "server_error", "message": str(e)})
    @app.exception_handler(ZidConnectionError)
    async def _(r, e): return JSONResponse(503, {"error": "connection", "message": str(e)})
