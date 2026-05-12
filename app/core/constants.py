# Expanded keywords for algae and related fields
ALGAE_KEYWORDS = [
    # English algae terms
    "algae", "algal", "cyanobacteria", "diatom", "dinoflagellate",
    "microcystin", "anatoxin", "saxitoxin", "brevetoxin", "nodularin",
    "bloom", "eutrophication", "aquaculture", "biofuel", "biomass",
    "phycobiliprotein", "carotenoid", "chlorophyll", "photosynthesis",
    "nitrogen fixation", "harmful algal bloom", "hab", "red tide",
    "green algae", "blue-green algae", "spirulina", "chlorella",
    "phytoplankton", "zooplankton", "algaecide", "microalgae",
    "macroalgae", "seaweed", "kelp", "phycotoxin", "algal bloom",
    "desmid", "euglena", "volvox", "ulva", "sargassum", "chlorella",
    "scenedesmus", "haematococcus", "dunaliella", "nannochloropsis",
    "phycology", "phycologist", "aquatic", "marine", "freshwater",
    "water quality", "oxygen production", "carbon capture", "co2",
    "bioremediation", "wastewater treatment", "fish kill",
    
    # Arabic algae terms
    "طحالب", "طحلب", "سيانوبكتيريا", "دايتوم", "دينوفلاجيليت",
    "تسمم", "سمية", "ازهار", "تكاثر", "ماء", "بحيرة", "بحر",
    "مزرعة", "استزراع", "علف", "وقود", "حيوي", "بيئي", "بيئة",
    "نبات", "مائي", "عوالق", "أكسجين", "كربون", "معالجة",
    
    # General helpful words (to allow greetings and casual conversation)
    "hello", "hi", "hey", "greetings", "thanks", "thank you",
    "help", "please", "tell me", "what is", "how to", "explain",
    "مرحبا", "اهلا", "سلام", "شكرا", "مساعده", "كيف", "ماذا"
]

# System prompt now encourages flexibility
SYSTEM_PROMPT_TEMPLATE = """You are BioAlga, a friendly and knowledgeable AI assistant specialized in algae and related fields.

Information about current user's algae interest: {algae_type}
Detailed context: {algae_context}

You can answer questions about algae, aquatic biology, environmental science, and related topics. 
Be warm and engaging. If a user greets you, respond politely. Keep answers scientifically accurate but approachable.

Remember: You are an algae expert. Help the user learn!

Current algae focus: {algae_type}"""

# Error messages (still used for rate limiting, etc.)
ERROR_MESSAGES = {
    "outside_scope": "I am specialized in algae, but I'm happy to help with related topics! Could you rephrase?",
    "api_error": "Sorry, an error occurred. Please try again in a moment.",
    "invalid_algae": "Algae type not found in my knowledge base, but I'll try my best to help.",
    "rate_limit": "Rate limit exceeded. Please wait and try again.",
    "invalid_input": "Invalid input. Please provide a clear question."
}