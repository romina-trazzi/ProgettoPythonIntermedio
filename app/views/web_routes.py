# app/views/web_routes.py

from flask import Blueprint, render_template, request

web_bp = Blueprint('web_bp', __name__)

@web_bp.route('/')
def home():
    return render_template('base.html')

#from fastapi import APIRouter, Request
#from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates # Decommenta se userai template HTML

# Se prevedi di avere template, configura Jinja2:
# templates = Jinja2Templates(directory="templates")

#web_router = APIRouter(prefix="/web", tags=["Web UI (Placeholder)"])

#@web_router.get("/", response_class=HTMLResponse)
#async def read_root_web(request: Request):
    """
    **Endpoint di esempio per la pagina web principale.**
    Questo endpoint è un segnaposto per un'eventuale interfaccia utente basata su template HTML.
    Al momento, restituisce un semplice messaggio HTML.
    """
    # return templates.TemplateResponse("index.html", {"request": request, "message": "Benvenuto!"})
    return "<h1>Benvenuto al Sistema di Raccomandazione! (Interfaccia Web - Placeholder)</h1><p>Visita /docs per la documentazione API interattiva.</p>"