from .settings import app
from .routes import router

from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

app.include_router(router)

@router.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="Custom Swagger UI"
    )

@router.get("/openapi.json", include_in_schema=False)
async def get_open_api_endpoint():
    return get_openapi(title="Custom Swagger UI", version="1", routes=app.routes)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
