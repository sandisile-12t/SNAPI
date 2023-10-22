from fastapi import FastAPI, Request, Depends, Form, status, Cookie, HTTPException
from starlette_csrf import CSRFMiddleware
from fastapi.templating import Jinja2Templates
from datetime import datetime
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import ValidationError
from models import Status, User, Company
from database import engine, SessionLocal

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Status.metadata.create_all(bind=engine)
User.metadata.create_all(bind=engine)
Company.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app.add_middleware(CSRFMiddleware, secret="__CHANGE_ME__")


@app.get("/")
async def home(request: Request, db: Session = Depends(get_db)):
    companies = db.query(Company).order_by(Company.id.asc()).all()
    return templates.TemplateResponse("index.html", {"request": request, "companies": companies})

@app.post("/add")
async def add(
    request: Request,
    name: str = Form(...),
    registration_number: int = Form(...),
    main_contact_number: int = Form(...),
    secondary_contact_number: int = Form(...),
    user_id: int = Form(...),
    db: Session = Depends(get_db)
):
    try:
        current_datetime = datetime.now()
        company = Company(
            name=name,
            registration_number=registration_number,
            main_contact_number=main_contact_number,
            secondary_contact_number=secondary_contact_number,
            created_at=current_datetime,
            updated_at=current_datetime,
            user_id=user_id
        )
        db.add(company)
        db.commit()
        return RedirectResponse(url=app.url_path_for("home"), status_code=status.HTTP_303_SEE_OTHER)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))

@app.get("/createnew")
async def createnew(request: Request, user_id: int = Cookie(None), db: Session = Depends(get_db)):
    if user_id is None:
        raise HTTPException(status_code=401, detail="User not authenticated")
    return templates.TemplateResponse("createnew.html", {"request": request, "user_id": user_id})

@app.get("/edit/{company_id}")
async def edit_company(request: Request, company_id: int, db: Session = Depends(get_db)):
    company = db.query(Company).filter(Company.id == company_id).first()
    return templates.TemplateResponse("edit.html", {"request": request, "company": company})

@app.post("/update/{company_id}")
async def update(
    request: Request,
    company_id: int,
    name: str = Form(...),
    registration_number: int = Form(...),
    main_contact_number: int = Form(...),
    secondary_contact_number: int = Form(...),
    db: Session = Depends(get_db)
):
    company = db.query(Company).filter(Company.id == company_id).first()
    if company:
        company.name = name
        company.registration_number = registration_number
        company.main_contact_number = main_contact_number
        company.secondary_contact_number = secondary_contact_number
        db.commit()
        return RedirectResponse(url=app.url_path_for("home"), status_code=status.HTTP_303_SEE_OTHER)
    else:
        raise HTTPException(status_code=404, detail="Company not found")

@app.get("/delete/{company_id}")
async def delete(
    request: Request,
    company_id: int,
    db: Session = Depends(get_db)
):
    company = db.query(Company).filter(Company.id == company_id).first()
    db.delete(company)
    db.commit()
    return RedirectResponse(url=app.url_path_for("home"), status_code=status.HTTP_303_SEE_OTHER)

if __name__ == "__app__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)