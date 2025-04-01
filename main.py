from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routes import router as api_router  # Import your router
from database import get_db, engine  # Import get_db and engine from your database file
from sqlalchemy.future import select
from models import RouteInfo, User  # Import RouteInfo and User models
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from base import Base
from sqlalchemy import insert
import hashlib

# Initialize FastAPI app
app = FastAPI()

# Initialize Jinja2 templates for rendering HTML
templates = Jinja2Templates(directory="templates")

# Serve static files (for example, for JavaScript, CSS, etc.)
#app.mount("/static", StaticFiles(directory="static"), name="static")

# Include API routes (Make sure you have a routes.py file with your API routes)
app.include_router(api_router)

# Function to populate route data if the routes are empty
async def populate_routes_if_empty():
    async for session in get_db():
        # Check if routes already exist in the database
        result = await session.execute(select(RouteInfo))
        existing_routes = result.scalars().all()

        # If no routes exist, insert demo data
        if not existing_routes:
            route_data = [
                # Route 1: Panauti-Banepa
                {
                    "route_id": "route_1",
                    "route_name": "Panauti-Banepa",
                    "coordinates": [
                        {"lat": 27.594185, "lon": 85.519209},
                        {"lat": 27.594432, "lon": 85.519713},
                        {"lat": 27.594908, "lon": 85.520689},
                        {"lat": 27.595583, "lon": 85.521119},
                        {"lat": 27.596106, "lon": 85.521655},
                        {"lat": 27.596363, "lon": 85.521827},
                        {"lat": 27.596619, "lon": 85.522310},
                        {"lat": 27.597019, "lon": 85.522943},
                        {"lat": 27.597798, "lon": 85.523736},
                        {"lat": 27.598445, "lon": 85.524123},
                        {"lat": 27.598873, "lon": 85.524455},
                        {"lat": 27.599529, "lon": 85.524713},
                        {"lat": 27.599938, "lon": 85.524970},
                        {"lat": 27.600261, "lon": 85.525442},
                        {"lat": 27.600556, "lon": 85.526150},
                        {"lat": 27.600708, "lon": 85.526526},
                        {"lat": 27.600907, "lon": 85.527352},
                        {"lat": 27.601221, "lon": 85.528221},
                        {"lat": 27.602239, "lon": 85.529144},
                        {"lat": 27.602952, "lon": 85.529530},
                        {"lat": 27.603560, "lon": 85.529648},
                        {"lat": 27.604425, "lon": 85.529541},
                        {"lat": 27.605167, "lon": 85.529401},
                        {"lat": 27.605956, "lon": 85.529777},
                        {"lat": 27.606546, "lon": 85.530131},
                        {"lat": 27.607040, "lon": 85.530313},
                        {"lat": 27.607696, "lon": 85.530775},
                        {"lat": 27.608428, "lon": 85.530549},
                        {"lat": 27.609131, "lon": 85.530957},
                        {"lat": 27.609721, "lon": 85.531021},
                        {"lat": 27.610177, "lon": 85.530485},
                        {"lat": 27.611394, "lon": 85.530185},
                        {"lat": 27.612640, "lon": 85.529836},
                        {"lat": 27.613329, "lon": 85.530093},
                        {"lat": 27.613861, "lon": 85.530120},
                        {"lat": 27.614184, "lon": 85.529718},
                        {"lat": 27.615672, "lon": 85.528827},
                        {"lat": 27.616808, "lon": 85.528302},
                        {"lat": 27.617982, "lon": 85.527534},
                        {"lat": 27.618729, "lon": 85.526853},
                        {"lat": 27.619579, "lon": 85.525737},
                        {"lat": 27.620991, "lon": 85.524922},
                        {"lat": 27.621680, "lon": 85.524160},
                        {"lat": 27.622213, "lon": 85.524037},
                        {"lat": 27.623154, "lon": 85.523908},
                        {"lat": 27.624698, "lon": 85.523366},
                        {"lat": 27.625663, "lon": 85.523034},
                        {"lat": 27.626752, "lon": 85.522889},
                        {"lat": 27.627840, "lon": 85.522814},
                        {"lat": 27.628073, "lon": 85.523286},
                        {"lat": 27.629941, "lon": 85.523908},
                    ],
                },
                # Route 2: Banepa-Panauti (reverse of Route 1)
                {
                    "route_id": "route_2",
                    "route_name": "Banepa-Panauti",
                    "coordinates": [
                        {"lat": 27.629941, "lon": 85.523908},
                        {"lat": 27.628073, "lon": 85.523286},
                        {"lat": 27.627840, "lon": 85.522814},
                        {"lat": 27.626752, "lon": 85.522889},
                        {"lat": 27.625663, "lon": 85.523034},
                        {"lat": 27.624698, "lon": 85.523366},
                        {"lat": 27.623154, "lon": 85.523908},
                        {"lat": 27.622213, "lon": 85.524037},
                        {"lat": 27.621680, "lon": 85.524160},
                        {"lat": 27.620991, "lon": 85.524922},
                        {"lat": 27.619579, "lon": 85.525737},
                        {"lat": 27.618729, "lon": 85.526853},
                        {"lat": 27.617982, "lon": 85.527534},
                        {"lat": 27.616808, "lon": 85.528302},
                        {"lat": 27.615672, "lon": 85.528827},
                        {"lat": 27.614184, "lon": 85.529718},
                        {"lat": 27.613861, "lon": 85.530120},
                        {"lat": 27.613329, "lon": 85.530093},
                        {"lat": 27.612640, "lon": 85.529836},
                        {"lat": 27.611394, "lon": 85.530185},
                        {"lat": 27.610177, "lon": 85.530485},
                        {"lat": 27.609721, "lon": 85.531021},
                        {"lat": 27.609131, "lon": 85.530957},
                        {"lat": 27.608428, "lon": 85.530549},
                        {"lat": 27.607696, "lon": 85.530775},
                        {"lat": 27.607040, "lon": 85.530313},
                        {"lat": 27.606546, "lon": 85.530131},
                        {"lat": 27.605956, "lon": 85.529777},
                        {"lat": 27.605167, "lon": 85.529401},
                        {"lat": 27.604425, "lon": 85.529541},
                        {"lat": 27.603560, "lon": 85.529648},
                        {"lat": 27.602952, "lon": 85.529530},
                        {"lat": 27.602239, "lon": 85.529144},
                        {"lat": 27.601221, "lon": 85.528221},
                        {"lat": 27.600907, "lon": 85.527352},
                        {"lat": 27.600708, "lon": 85.526526},
                        {"lat": 27.600556, "lon": 85.526150},
                        {"lat": 27.600261, "lon": 85.525442},
                        {"lat": 27.599938, "lon": 85.524970},
                        {"lat": 27.599529, "lon": 85.524713},
                        {"lat": 27.598873, "lon": 85.524455},
                        {"lat": 27.598445, "lon": 85.524123},
                        {"lat": 27.597798, "lon": 85.523736},
                        {"lat": 27.597019, "lon": 85.522943},
                        {"lat": 27.596619, "lon": 85.522310},
                        {"lat": 27.596363, "lon": 85.521827},
                        {"lat": 27.596106, "lon": 85.521655},
                        {"lat": 27.595583, "lon": 85.521119},
                        {"lat": 27.594908, "lon": 85.520689},
                        {"lat": 27.594432, "lon": 85.519713},
                        {"lat": 27.594185, "lon": 85.519209},
                        {"lat": 27.593672, "lon": 85.518458},
                        {"lat": 27.592816, "lon": 85.517117},
                        {"lat": 27.591998, "lon": 85.516870},
                        {"lat": 27.591437, "lon": 85.516934},
                        {"lat": 27.590677, "lon": 85.516816},
                        {"lat": 27.590410, "lon": 85.516731},
                        {"lat": 27.590173, "lon": 85.516645},
                        {"lat": 27.589459, "lon": 85.515840},
                        {"lat": 27.588994, "lon": 85.514703},
                        {"lat": 27.603475, "lon": 85.529637},
                        {"lat": 27.602578, "lon": 85.529511},
                        {"lat": 27.5987, "lon": 85.5364},
                    ],
                },
                # Route 3: Panauti-Ratnapark
                {
                    "route_id": "route_3",
                    "route_name": "Panauti-Ratnapark",
                    "coordinates": [
                        {"lat": 27.5987, "lon": 85.5364},
                        {"lat": 27.5965, "lon": 85.5377},
                        {"lat": 27.5950, "lon": 85.5391},
                        {"lat": 27.5938, "lon": 85.5405},
                        {"lat": 27.5915, "lon": 85.5420},
                        {"lat": 27.5890, "lon": 85.5433},
                        {"lat": 27.5872, "lon": 85.5442},
                        {"lat": 27.5858, "lon": 85.5450},
                        {"lat": 27.5841, "lon": 85.5460},
                        {"lat": 27.5827, "lon": 85.5473},
                        {"lat": 27.5815, "lon": 85.5480},
                        {"lat": 27.5802, "lon": 85.5492},
                        {"lat": 27.5788, "lon": 85.5503},
                    ],
                },
                # Route 4: Ratnapark-Panauti (reverse of Route 3)
                {
                    "route_id": "route_4",
                    "route_name": "Ratnapark-Panauti",
                    "coordinates": [
                        {"lat": 27.5788, "lon": 85.5503},
                        {"lat": 27.5802, "lon": 85.5492},
                        {"lat": 27.5815, "lon": 85.5480},
                        {"lat": 27.5827, "lon": 85.5473},
                        {"lat": 27.5841, "lon": 85.5460},
                        {"lat": 27.5858, "lon": 85.5450},
                        {"lat": 27.5872, "lon": 85.5442},
                        {"lat": 27.5890, "lon": 85.5433},
                        {"lat": 27.5915, "lon": 85.5420},
                        {"lat": 27.5938, "lon": 85.5405},
                        {"lat": 27.5950, "lon": 85.5391},
                        {"lat": 27.5965, "lon": 85.5377},
                        {"lat": 27.5987, "lon": 85.5364},
                    ],
                },
            ]

            # Insert demo data into the RouteInfo table
            for route in route_data:
                db_route = RouteInfo(**route)
                session.add(db_route)

            # Commit the changes
            await session.commit()

async def populate_users_if_empty():
    async for session in get_db():
        result = await session.execute(select(User))
        existing_users = result.scalars().all()

        if not existing_users:
            users_data = []
            for i in range(1, 5):
                for j in range(1, 6):
                    username = f"user_{i}_{j}"
                    bus_number = f"bus_{i}_{j}"
                    route_id = i
                    password = "password123"
                    password_hash = hashlib.sha256(password.encode()).hexdigest()

                    users_data.append({
                        "username": username,
                        "bus_number": bus_number,
                        "route_id": str(route_id),
                        "password_hash": password_hash,
                        "status": True
                    })

            for user in users_data:
                db_user = User(**user)
                session.add(db_user)

            await session.commit()

# Register the function to run on application startup
@app.on_event("startup")
async def startup():
    # Create tables in the database if they don't exist
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Populate route data if no routes are present
    await populate_routes_if_empty()
    await populate_users_if_empty()

# Render the map page (mainpage.html) when accessing the root URL
@app.get("/")
async def render_map(request: Request):
    return templates.TemplateResponse("mainpage.html", {"request": request})

@app.get("/create_bus")
async def render_cb(request: Request):
    return templates.TemplateResponse("bus_driver.html", {"request": request})

@app.get("/driver_location")
async def render_driver(request: Request):
    return templates.TemplateResponse("driver_location.html", {"request": request})

@app.get("/login")
async def render_login(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})