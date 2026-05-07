from fastapi import FastAPI
from fastapi.responses import JSONResponse
import logging
from datetime import datetime

from app.core.config import settings
from app.middleware.cors import setup_cors
from app.api.routes import chat, algae, enhance

# Setup logging
logging.basicConfig(
    level=logging.INFO if not settings.debug_mode else logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="AI-powered algae classification assistant and knowledge base",
    docs_url="/docs" if settings.debug_mode else None,
    redoc_url="/redoc" if settings.debug_mode else None
)

# Setup CORS
setup_cors(app)

# Include routers
app.include_router(chat.router)
app.include_router(algae.router)
app.include_router(enhance.router)

@app.get("/")
async def root():
    return {
        "service": settings.app_name,
        "version": settings.app_version,
        "status": "operational",
        "endpoints": {
            "chat": "/chat/ - POST - Ask questions about algae",
            "chat_types": "/chat/types - GET - List available algae types",
            "algae_info": "/algae/info - POST - Get detailed algae information",
            "algae_toxicity": "/algae/toxicity/{algae_type} - GET - Get toxicity summary",
            "enhance_results": "/enhance/results - POST - Enhance classification results",
            "enhance_summary": "/enhance/summary - POST - Generate summary",
            "enhance_toxicity": "/enhance/toxicity/{algae_type} - GET - Quick toxicity check"
        },
        "available_algae_types": len(chat.router.routes) > 0  # Will be populated
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    openai_ok = True
    try:
        from openai import OpenAI
        client = OpenAI(api_key=settings.openai_api_key)
    except Exception as e:
        openai_ok = False
        logger.warning(f"OpenAI health check failed: {e}")
    
    return {
        "status": "healthy",
        "version": settings.app_version,
        "timestamp": datetime.now().isoformat(),
        "openai_available": openai_ok
    }

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    logger.error(f"Global error: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "detail": str(exc) if settings.debug_mode else "An error occurred"
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug_mode
    )