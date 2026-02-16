"""OAuth flow."""

import secrets
from typing import Optional
from urllib.parse import urlencode

import httpx
from fastapi import APIRouter, Cookie, HTTPException
from fastapi.responses import RedirectResponse

from app.config import settings, save_tokens

router = APIRouter(prefix="/auth")


@router.get("/login")
async def login():
    """Start OAuth flow - redirects to Zid."""
    state = secrets.token_urlsafe(32)
    params = {
        "client_id": settings.zid_client_id,
        "redirect_uri": settings.zid_redirect_uri,
        "response_type": "code",
        "state": state,
    }
    response = RedirectResponse(f"{settings.zid_authorize_url}?{urlencode(params)}")
    response.set_cookie("oauth_state", state, max_age=600, httponly=True, samesite="none", secure=True)
    return response


@router.get("/callback")
async def callback(
    code: Optional[str] = None,
    state: Optional[str] = None,
    error: Optional[str] = None,
    oauth_state: Optional[str] = Cookie(None),
):
    """OAuth callback - exchanges code for tokens."""
    if error:
        raise HTTPException(400, f"OAuth error: {error}")
    if not code or not state or state != oauth_state:
        raise HTTPException(400, "Invalid OAuth callback")
    
    async with httpx.AsyncClient() as http:
        resp = await http.post(settings.zid_token_url, data={
            "grant_type": "authorization_code",
            "client_id": settings.zid_client_id,
            "client_secret": settings.zid_client_secret,
            "redirect_uri": settings.zid_redirect_uri,
            "code": code,
        })
        if resp.status_code != 200:
            raise HTTPException(400, f"Token exchange failed: {resp.text}")
        data = resp.json()
    
    save_tokens(
        authorization_token=data.get("authorization") or data.get("authorization_token", ""),
        access_token=data.get("access_token", ""),
    )
    
    return RedirectResponse("/dashboard")
