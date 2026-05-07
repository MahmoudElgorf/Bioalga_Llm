#!/usr/bin/env python3
"""
Run script for BioAlga Backend
Usage: python run.py
"""

import uvicorn
from app.core.config import settings

if __name__ == "__main__":
    print(f"Starting {settings.app_name} v{settings.app_version}")
    print(f"Debug mode: {settings.debug_mode}")
    print(f"Server: http://{settings.host}:{settings.port}")
    
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug_mode,
        log_level="info"
    )