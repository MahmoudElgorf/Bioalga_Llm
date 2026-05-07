from app.api.routes import chat, algae, enhance

# Export routers
chat_router = chat.router
algae_router = algae.router
enhance_router = enhance.router

__all__ = [
    'chat_router',
    'algae_router', 
    'enhance_router'
]