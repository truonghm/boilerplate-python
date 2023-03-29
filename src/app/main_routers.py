from app.modules.healthcheck.routers import router as hc_router



def add_all_routers(app):
    app.include_router(hc_router, prefix="/healthcheck", tags=["test"])
