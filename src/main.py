from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def frontpage(request: Request):
    return templates.TemplateResponse("frontpage.html", {"request": request})


@app.get("/checkout", response_class=HTMLResponse)
async def checkout(request: Request):
    return templates.TemplateResponse("checkout.html", {"request": request})


@app.get("/products/{product_id}", response_class=HTMLResponse)
async def frontpage(request: Request, product_id: str):
    return templates.TemplateResponse("product.html", {"request": request, "product_id": product_id})
