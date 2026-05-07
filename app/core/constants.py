# Keywords for detecting algae-related questions
ALGAE_KEYWORDS = [
    "algae", "algal", "cyanobacteria", "diatom", "dinoflagellate",
    "microcystin", "anatoxin", "saxitoxin", "brevetoxin", "nodularin",
    "bloom", "eutrophication", "aquaculture", "biofuel", "biomass",
    "phycobiliprotein", "carotenoid", "chlorophyll", "photosynthesis",
    "nitrogen fixation", "harmful algal bloom", "hab", "red tide",
    "green algae", "blue-green algae", "spirulina", "chlorella",
    "phytoplankton", "zooplankton", "algaecide", "microalgae",
    "macroalgae", "seaweed", "kelp", "phycotoxin", "algal bloom",
    "طحالب", "طحلب", "سيانوبكتيريا", "دايتوم", "دينوفلاجيليت",
    "تسمم", "سمية", "ازهار", "تكاثر", "ماء", "بحيرة", "بحر",
    "مزرعة", "استزراع", "علف", "وقود", "حيوي"
]

# System prompt template for OpenAI
SYSTEM_PROMPT_TEMPLATE = """You are a scientific assistant specialized 100% in algae only.

Information about current algae ({algae_type}):
{algae_context}

Strict rules:
1. Answer ONLY questions related to algae
2. If user asks about non-algae topics, politely refuse: "I am specialized in algae only. Please ask about algae classification, toxicity, applications, or environmental impact."
3. For toxic algae, always include clear warnings using WARNING
4. Be scientifically accurate and concise (3-5 sentences typically)
5. Respond in the same language as the user's question

Remember: Your specialization is algae only."""

# Error messages
ERROR_MESSAGES = {
    "outside_scope": "I am a specialist in algae only. I cannot answer this question. Do you have a question about algae?",
    "api_error": "Sorry, an error occurred connecting to the service. Please try again.",
    "invalid_algae": "Algae type not found in knowledge base.",
    "rate_limit": "Rate limit exceeded. Please wait a minute and try again.",
    "invalid_input": "Invalid input provided. Please check your request.",
    "openai_error": "AI service temporarily unavailable. Please try again later."
}

# Confidence levels
CONFIDENCE_LEVELS = {
    "high": 0.8,
    "medium": 0.6,
    "low": 0.4
}

# Algae categories
ALGAE_CATEGORIES = {
    "cyanobacteria": "Cyanobacteria (Blue-green bacteria)",
    "dinoflagellate": "Dinoflagellate",
    "diatom": "Diatom",
    "green_algae": "Green Algae",
    "red_algae": "Red Algae",
    "brown_algae": "Brown Algae"
}