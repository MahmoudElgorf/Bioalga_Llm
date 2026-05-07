from typing import Dict, Any, List, Optional

ALGAE_KNOWLEDGE_BASE: Dict[str, Dict[str, Any]] = {
    'Anabaena': {
        'scientific_name': 'Anabaena spp. (or Dolichospermum)',
        'arabic_name': 'Anabaena',
        'category': 'Cyanobacteria (Blue-green bacteria)',
        'is_toxic': False,
        'toxicity_level': 'variable',
        'toxicity_warning': 'Toxin production depends on species/strain',
        'scientific_warning': 'Most planktonic Anabaena are now reclassified as Dolichospermum. Toxicity varies significantly between species and strains. Cannot determine without genetic/toxin analysis.',
        'potential_toxins': ['anatoxin-a (neurotoxin) - in some strains', 'Other toxins possible depending on species'],
        'co2_per_kg': 1.83,
        'sellable': 'Conditional - Only as controlled culture (e.g., Azolla-Anabaena symbiosis), NOT from wild blooms',
        'benefits': [
            'Atmospheric nitrogen fixation (via heterocysts)',
            'Used in Azolla-Anabaena symbiosis as green manure in rice fields',
            'Improves soil fertility (when using non-toxic strains)'
        ],
        'uses': [
            'Biofertilizers (with defined non-toxic strains)',
            'Scientific research',
            'Nitrogen fixation studies'
        ],
        'habitat': 'Freshwater lakes, ponds, slow-moving rivers',
        'treatment_methods': ['Copper sulfate (careful)', 'Hydrogen peroxide', 'Barley straw'],
        'health_effects': 'Neurotoxic effects: muscle twitching, paralysis, respiratory arrest in toxic strains'
    },
    
    'Aphanizomenon': {
        'scientific_name': 'Aphanizomenon spp.',
        'arabic_name': 'Aphanizomenon',
        'category': 'Cyanobacteria (Blue-green bacteria)',
        'is_toxic': False,
        'toxicity_level': 'variable',
        'toxicity_warning': 'Some strains produce toxins, others do not',
        'scientific_warning': 'Some Aphanizomenon strains produce saxitoxins (neurotoxins) or cylindrospermopsin (hepatotoxin/nephrotoxin). Commercial AFA from Klamath Lake risks Microcystis contamination. NOT safe for sale without toxin testing.',
        'potential_toxins': ['Saxitoxins (neurotoxins)', 'Cylindrospermopsin (hepatotoxin/nephrotoxin)', 'Risk of Microcystin contamination from environment'],
        'co2_per_kg': 1.83,
        'sellable': 'No - High regulatory risk without extensive toxin testing and controlled cultivation',
        'benefits': [
            'Nitrogen fixation',
            'Ecological role as primary producer'
        ],
        'uses': [
            'Scientific research',
            'Water quality monitoring',
            'Toxin studies'
        ],
        'habitat': 'Nutrient-rich freshwater systems, lakes',
        'treatment_methods': ['Activated carbon', 'UV treatment', 'Coagulation'],
        'health_effects': 'Neurotoxic effects from saxitoxins, liver/kidney damage from cylindrospermopsin'
    },
    
    'Microcystis': {
        'scientific_name': 'Microcystis spp.',
        'arabic_name': 'Microcystis',
        'category': 'Cyanobacteria (Blue-green bacteria)',
        'is_toxic': True,
        'toxicity_level': 'severe',
        'toxicity_warning': 'DANGER: Produces dangerous hepatotoxins (Microcystins)',
        'scientific_warning': 'One of the most notorious cyanobacteria genera for producing microcystins (liver toxins). WHO drinking water guideline: 1 microgram/L for microcystin-LR. NOT suitable for sale as food/feed/fertilizer.',
        'potential_toxins': ['Microcystins (hepatotoxins - liver toxins)'],
        'co2_per_kg': 1.83,
        'sellable': 'No - Not suitable for commercial sale as raw biomass. Used only for research and monitoring.',
        'benefits': [
            'No direct benefits - this is a hazardous genus',
            'Used for water quality studies and toxin research'
        ],
        'uses': [
            'Scientific research',
            'Environmental monitoring',
            'Water safety management',
            'Risk assessment'
        ],
        'habitat': 'Nutrient-rich freshwater lakes, reservoirs',
        'treatment_methods': ['Activated carbon', 'UV treatment', 'Coagulation', 'Ozonation', 'Chlorination'],
        'health_effects': 'Liver damage, nausea, fever, potential liver cancer risk',
        'symptoms_if_ingested': 'Nausea, vomiting, liver damage, fever within 30-60 minutes'
    },
    
    'Nodularia': {
        'scientific_name': 'Nodularia spp.',
        'arabic_name': 'Nodularia',
        'category': 'Cyanobacteria (Blue-green bacteria)',
        'is_toxic': True,
        'toxicity_level': 'high',
        'toxicity_warning': 'Produces Nodularin (hepatotoxin)',
        'scientific_warning': 'Nodularia spumigena is the most famous species, producing nodularin (cyclic peptide hepatotoxin similar to microcystins). Common in brackish waters like the Baltic Sea. Not a commercial product.',
        'potential_toxins': ['Nodularin (hepatotoxin - liver toxin)'],
        'co2_per_kg': 1.83,
        'sellable': 'No - Not commercially viable. Research and monitoring only.',
        'benefits': [
            'Nitrogen fixation (ecological role in low-nitrogen brackish systems)',
            'No direct economic benefits'
        ],
        'uses': [
            'Scientific research',
            'Toxin monitoring',
            'Bloom studies',
            'Genomic research'
        ],
        'habitat': 'Brackish waters, estuaries, Baltic Sea',
        'treatment_methods': ['Activated carbon', 'UV treatment', 'Ozonation'],
        'health_effects': 'Liver damage, similar to microcystins but less studied',
        'symptoms_if_ingested': 'Nausea, abdominal pain, liver toxicity within hours'
    },
    
    'Nostoc': {
        'scientific_name': 'Nostoc spp.',
        'arabic_name': 'Nostoc - Star jelly',
        'category': 'Cyanobacteria (Blue-green bacteria)',
        'is_toxic': False,
        'toxicity_level': 'low',
        'toxicity_warning': 'Generally safe for known edible species, but some strains can produce toxins',
        'scientific_warning': 'Some Nostoc strains can produce microcystins or nodularin under certain conditions. Traditional edible species (e.g., Nostoc flagelliforme "Facai" in China) have long safety history, but modern products require strain identification and safety testing.',
        'potential_toxins': ['Microcystins (in some strains)', 'Nodularin (reported in some cases)'],
        'co2_per_kg': 1.83,
        'sellable': 'Conditional - Only defined non-toxic strains with safety documentation',
        'benefits': [
            'Nitrogen fixation',
            'Soil improvement and biofertilizer potential',
            'Protein source (traditional edible species)'
        ],
        'uses': [
            'Biofertilizers (non-toxic strains)',
            'Scientific research',
            'Traditional food (specific species)',
            'Soil reclamation'
        ],
        'habitat': 'Freshwater and terrestrial environments',
        'treatment_methods': ['None needed for non-toxic strains'],
        'health_effects': 'Generally safe for traditional edible species'
    },
    
    'Oscillatoria': {
        'scientific_name': 'Oscillatoria spp.',
        'arabic_name': 'Oscillatoria - Oscillating algae',
        'category': 'Cyanobacteria (Blue-green bacteria)',
        'is_toxic': False,
        'toxicity_level': 'variable',
        'toxicity_warning': 'Some strains produce neurotoxins or skin irritants',
        'scientific_warning': 'Some Oscillatoria strains produce anatoxin-a (neurotoxin), microcystins, or aplysiatoxins (skin irritant). Not recommended for food/agriculture without laboratory identification and toxin testing.',
        'potential_toxins': ['Anatoxin-a (neurotoxin)', 'Microcystins (hepatotoxin)', 'Aplysiatoxins (skin irritant)'],
        'co2_per_kg': 1.83,
        'sellable': 'No - Not suitable for commercial products. Research and monitoring only.',
        'benefits': [
            'Used as environmental indicator in water pollution studies'
        ],
        'uses': [
            'Scientific research',
            'Environmental monitoring',
            'Toxin studies'
        ],
        'habitat': 'Freshwater, wastewater systems',
        'treatment_methods': ['Copper sulfate', 'Hydrogen peroxide', 'Barley straw'],
        'health_effects': 'Neurotoxic effects, skin irritation, liver damage depending on strain'
    },
    
    'Gymnodinium': {
        'scientific_name': 'Gymnodinium spp.',
        'arabic_name': 'Gymnodinium',
        'category': 'Dinoflagellate',
        'is_toxic': False,
        'toxicity_level': 'variable',
        'toxicity_warning': 'Some species (e.g., G. catenatum) produce paralytic shellfish toxins',
        'scientific_warning': 'Gymnodinium catenatum is known to produce saxitoxins causing Paralytic Shellfish Poisoning (PSP). Not all Gymnodinium species are toxic. Red tide (HAB) does not automatically mean toxicity.',
        'potential_toxins': ['Saxitoxins (PST/PSP) - in some species like G. catenatum'],
        'co2_per_kg': 1.83,
        'sellable': 'No - Not a commercial biomass product. Relevant for monitoring only.',
        'benefits': [
            'Part of marine food web',
            'Marine ecology studies'
        ],
        'uses': [
            'Scientific research',
            'Shellfish monitoring',
            'Early warning systems for toxins'
        ],
        'habitat': 'Marine and brackish waters worldwide',
        'treatment_methods': ['Clay flocculation', 'Ozone treatment (small scale)'],
        'health_effects': 'Paralytic shellfish poisoning: tingling, numbness, paralysis'
    },
    
    'Karenia': {
        'scientific_name': 'Karenia spp.',
        'arabic_name': 'Karenia - Red tide algae',
        'category': 'Dinoflagellate (unarmored)',
        'is_toxic': True,
        'toxicity_level': 'severe',
        'toxicity_warning': 'DANGER: Produces Brevetoxins (neurotoxins) - causes Red Tide',
        'scientific_warning': 'Karenia brevis produces brevetoxins causing Neurotoxic Shellfish Poisoning (NSP), fish kills, marine mammal deaths, and respiratory irritation from aerosolized toxins. Major public health and environmental concern.',
        'potential_toxins': ['Brevetoxins (neurotoxins)'],
        'co2_per_kg': 1.83,
        'sellable': 'No - Highly toxic. Not a commercial product. Critical for monitoring only.',
        'benefits': [
            'No economic benefits - this is a hazardous genus',
            'Environmental change studies'
        ],
        'uses': [
            'Scientific research',
            'Environmental monitoring',
            'Public health protection',
            'Fisheries management'
        ],
        'habitat': 'Coastal marine waters, warm temperate regions, Gulf of Mexico',
        'treatment_methods': ['Clay flocculation (experimental)', 'Ozone treatment (small scale)'],
        'health_effects': 'Neurotoxic shellfish poisoning, respiratory irritation, asthma aggravation',
        'symptoms_if_ingested': 'Nausea, vomiting, neurological symptoms within 3 hours'
    },
    
    'Prorocentrum': {
        'scientific_name': 'Prorocentrum spp.',
        'arabic_name': 'Prorocentrum',
        'category': 'Dinoflagellate (armored/thecate)',
        'is_toxic': False,
        'toxicity_level': 'variable',
        'toxicity_warning': 'Some species produce Okadaic acid (DSP - Diarrhetic Shellfish Poisoning)',
        'scientific_warning': 'Some Prorocentrum species (especially benthic/mixed) produce okadaic acid and dinophysistoxins causing Diarrhetic Shellfish Poisoning (DSP). EU regulatory limit: ~160 microgram OA equivalents/kg shellfish.',
        'potential_toxins': ['Okadaic acid', 'Dinophysistoxins (DSP)'],
        'co2_per_kg': 1.83,
        'sellable': 'No - Not a commercial biomass product. Monitoring only.',
        'benefits': [
            'Marine ecology studies'
        ],
        'uses': [
            'Scientific research',
            'Shellfish monitoring',
            'Toxin analysis (LC-MS/MS)'
        ],
        'habitat': 'Coastal marine waters, coral reefs',
        'treatment_methods': ['Monitoring only'],
        'health_effects': 'Diarrhetic shellfish poisoning: diarrhea, nausea, vomiting, abdominal pain'
    },
    
    'Noctiluca': {
        'scientific_name': 'Noctiluca scintillans',
        'arabic_name': 'Noctiluca - Glowing algae',
        'category': 'Dinoflagellate (heterotrophic)',
        'is_toxic': False,
        'toxicity_level': 'low',
        'toxicity_warning': 'Not a known producer of human toxins, but blooms can cause hypoxia and fish kills',
        'scientific_warning': 'Mostly heterotrophic (feeds on plankton), not photosynthetic. Does NOT fix CO2 like photosynthetic organisms. "Green form" contains photosynthetic symbiont in some regions. Blooms can cause anoxia and ammonia release leading to marine life deaths.',
        'potential_toxins': ['No known human toxins', 'Environmental damage: hypoxia, ammonia'],
        'co2_per_kg': 0.0,
        'sellable': 'No - Not for commercial biomass. Valued for ecotourism (bioluminescence) only.',
        'benefits': [
            'Bioluminescence (creates glowing sea phenomenon)',
            'Educational value',
            'Ecotourism attraction'
        ],
        'uses': [
            'Scientific research',
            'Ecotourism',
            'Science education',
            'Nature photography'
        ],
        'habitat': 'Coastal marine waters worldwide',
        'treatment_methods': ['None needed - natural phenomenon'],
        'health_effects': 'No human toxins, but blooms can cause fish kills via hypoxia'
    },
    
    'Skeletonema': {
        'scientific_name': 'Skeletonema spp.',
        'arabic_name': 'Skeletonema',
        'category': 'Diatom (centric)',
        'is_toxic': False,
        'toxicity_level': 'none',
        'toxicity_warning': 'Generally safe. Not a human toxin producer.',
        'scientific_warning': 'Not known to produce human toxins. Dense blooms may cause environmental hypoxia after decay. One of the most practical and safe genera for aquaculture applications.',
        'potential_toxins': ['None known for humans', 'Environmental: possible hypoxia from dense blooms'],
        'co2_per_kg': 1.83,
        'sellable': 'Yes - Excellent for aquaculture (live feed in hatcheries)',
        'benefits': [
            'Rich in fatty acids',
            'Excellent live feed for aquatic larvae',
            'Important primary producer in coastal systems'
        ],
        'uses': [
            'Aquaculture - Hatcheries (shrimp, shellfish larvae)',
            'Scientific research',
            'Marine ecology'
        ],
        'habitat': 'Coastal and oceanic waters',
        'treatment_methods': [],
        'health_effects': 'None - considered safe as feed'
    },
    
    'nontoxic': {
        'scientific_name': 'Non-toxic Algae (general category)',
        'arabic_name': 'Non-toxic algae',
        'category': 'General category - requires species identification',
        'is_toxic': False,
        'toxicity_level': 'unknown',
        'toxicity_warning': 'Environmentally safe (based on general category)',
        'scientific_warning': 'This is a general category, not a scientific name. For commercial use, must specify exact species/strain and verify toxin-free status via LC-MS/MS or ELISA testing with source tracking (culture collection/barcode).',
        'potential_toxins': ['Should be tested to confirm absence of: Microcystins, Nodularin, Anatoxin-a, Saxitoxins, Cylindrospermopsin'],
        'co2_per_kg': 1.83,
        'sellable': 'Conditional - Requires species identification and toxin testing per batch',
        'benefits': [
            'Maintains ecological balance',
            'Oxygen production',
            'Food source for organisms'
        ],
        'uses': [
            'Hydroponics',
            'Scientific research',
            'Aquaculture (with identification)'
        ],
        'habitat': 'Various aquatic environments',
        'treatment_methods': ['Depends on species'],
        'health_effects': 'Depends on species - testing required'
    }
}

# List of all available algae types
ALGAE_TYPES = list(ALGAE_KNOWLEDGE_BASE.keys())

# Toxicity levels mapping
TOXICITY_LEVELS = {
    'none': 0,
    'low': 1,
    'variable': 2,
    'high': 3,
    'severe': 4,
    'unknown': 0
}

def get_algae_info(algae_type: str) -> Dict[str, Any]:
    """Retrieve algae information with case-insensitive fallback"""
    if algae_type in ALGAE_KNOWLEDGE_BASE:
        return ALGAE_KNOWLEDGE_BASE[algae_type].copy()
    
    # Try case-insensitive match
    for key in ALGAE_KNOWLEDGE_BASE:
        if key.lower() == algae_type.lower():
            return ALGAE_KNOWLEDGE_BASE[key].copy()
    
    # Return default
    return ALGAE_KNOWLEDGE_BASE['nontoxic'].copy()

def is_toxic_type(algae_type: str) -> bool:
    """Check if algae type is considered toxic"""
    info = get_algae_info(algae_type)
    return info.get('is_toxic', False)

def get_toxicity_level(algae_type: str) -> str:
    """Get toxicity level string"""
    info = get_algae_info(algae_type)
    return info.get('toxicity_level', 'unknown')