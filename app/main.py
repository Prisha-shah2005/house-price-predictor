from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Import prediction function
from app.predict import predict_price


# Create FastAPI app
app = FastAPI()


# Configure templates folder
templates = Jinja2Templates(directory="templates")


# Serve static files (CSS, images, favicon)
app.mount("/static", StaticFiles(directory="static"), name="static")


# Home page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "prediction": None
        }
    )


# Prediction endpoint
@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    location: str = Form(...),
    sqft: float = Form(...),
    bath: int = Form(...),
    bhk: int = Form(...)
):

    try:
        price = predict_price(location, sqft, bath, bhk)
    except Exception as e:
        print("Prediction Error:", e)
        price = None

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "prediction": price
        }
    )