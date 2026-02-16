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
    async def _(r, e): return JSONResponse({"error": "auth_error", "message": str(e)}, status_code=401)
    @app.exception_handler(ZidAuthorizationError)
    async def _(r, e): return JSONResponse({"error": "forbidden", "message": str(e)}, status_code=403)
    @app.exception_handler(ZidNotFoundError)
    async def _(r, e): return JSONResponse({"error": "not_found", "message": str(e)}, status_code=404)
    @app.exception_handler(ZidValidationError)
    async def _(r, e): return JSONResponse({"error": "validation", "message": str(e)}, status_code=422)
    @app.exception_handler(ZidRateLimitError)
    async def _(r, e): return JSONResponse({"error": "rate_limit", "message": str(e)}, status_code=429)
    @app.exception_handler(ZidServerError)
    async def _(r, e): return JSONResponse({"error": "server_error", "message": str(e)}, status_code=502)
    @app.exception_handler(ZidConnectionError)
    async def _(r, e): return JSONResponse({"error": "connection", "message": str(e)}, status_code=503)
