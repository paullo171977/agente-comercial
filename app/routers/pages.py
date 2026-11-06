from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={"pagina": "dashboard", "titulo": "Dashboard"},
    )


@router.get("/leads", response_class=HTMLResponse)
async def listar_leads(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="leads/lista.html",
        context={"pagina": "leads", "titulo": "Leads"},
    )
