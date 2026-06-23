"""Emergency detection and first aid utilities."""

from typing import Dict, List, Tuple


EMERGENCY_CONDITIONS = {
    'chest_pain': {
        'keywords': ['chest pain', 'chest tightness', 'chest discomfort', 'chest pressure'],
        'severity': 'critical',
        'response': '🚨 EMERGENCY: Possible Heart Attack\n\nCall 911/112 immediately!\n\nWhile waiting:\n- Sit down immediately\n- Chew an aspirin if available\n- Try to stay calm\n- Do not exert yourself'
    },
    'breathing_difficulty': {
        'keywords': ['breathing difficulty', 'shortness of breath', 'cannot breathe', 'gasping'],
        'severity': 'critical',
        'response': '🚨 EMERGENCY: Severe Breathing Difficulty\n\nCall 911/112 immediately!\n\nWhile waiting:\n- Sit up straight\n- Try to breathe slowly and deeply\n- Remove any tight clothing\n- Stay calm'
    },
    'severe_bleeding': {
        'keywords': ['severe bleeding', 'heavy bleeding', 'uncontrollable bleeding'],
        'severity': 'critical',
        'response': '🚨 EMERGENCY: Severe Bleeding\n\nCall 911/112 immediately!\n\nFirst Aid:\n1. Apply direct pressure with clean cloth\n2. Elevate the wound above heart level\n3. Do not remove the cloth, add more layers\n4. Apply pressure until bleeding stops\n5. Immobilize the area'
    },
    'stroke': {
        'keywords': ['stroke', 'face drooping', 'arm weakness', 'speech difficulty', 'sudden weakness'],
        'severity': 'critical',
        'response': '🚨 EMERGENCY: Possible Stroke\n\nCall 911/112 immediately!\n\nRemember F.A.S.T:\n- F: Face drooping on one side\n- A: Arm weakness or numbness\n- S: Speech difficulty\n- T: Time to call emergency\n\nTime is critical for stroke treatment!'
    },
    'unconscious': {
        'keywords': ['unconscious', 'unresponsive', 'collapsed', 'fainted', 'unconsciousness'],
        'severity': 'critical',
        'response': '🚨 EMERGENCY: Person Unconscious\n\nCall 911/112 immediately!\n\nFirst Aid:\n1. Check responsiveness\n2. Call emergency services\n3. Position on their side (recovery position)\n4. Check for breathing\n5. Be ready to perform CPR if needed'
    },
    'seizure': {
        'keywords': ['seizure', 'convulsion', 'epilepsy attack', 'seizing'],
        'severity': 'critical',
        'response': '🚨 EMERGENCY: Seizure\n\nCall 911/112 immediately!\n\nFirst Aid:\n1. Protect from injury - remove nearby objects\n2. Place something soft under head\n3. Do NOT restrain the person\n4. Turn on side to keep airway clear\n5. Stay with person until help arrives'
    },
    'overdose': {
        'keywords': ['overdose', 'poisoning', 'too much', 'intoxication'],
        'severity': 'critical',
        'response': '🚨 EMERGENCY: Possible Overdose/Poisoning\n\nCall 911/112 or Poison Control immediately!\n\nFirst Aid:\n1. Call emergency services\n2. Do not induce vomiting\n3. If conscious, get the substance information\n4. Monitor breathing\n5. Keep person awake if possible'
    }
}


FIRST_AID_GUIDES = {
    'burns': {
        'title': 'Burns First Aid',
        'icon': '🔥',
        'steps': [
            'Immediately cool the burn with cool running water for 10-15 minutes',
            'Remove tight clothing or jewelry if possible',
            'Do NOT apply ice directly',
            'For minor burns: Apply antibiotic ointment',
            'Cover with sterile gauze or non-stick bandage',
            'Take over-the-counter pain reliever if needed',
            'Seek medical help for severe burns (blistering, large area)'
        ],
        'dont': [
            'Do NOT apply ice directly',
            'Do NOT use butter or oil',
            'Do NOT break blisters',
            'Do NOT apply ointments to severe burns'
        ]
    },
    'cuts': {
        'title': 'Cuts and Wounds First Aid',
        'icon': '✂️',
        'steps': [
            'Wash your hands with soap and water',
            'Stop the bleeding by applying direct pressure',
            'Rinse the wound with clean water',
            'Apply antibiotic ointment',
            'Cover with sterile gauze if needed',
            'Change bandage daily',
            'Watch for signs of infection (redness, swelling, pus)'
        ],
        'dont': [
            'Do NOT remove embedded objects',
            'Do NOT use dirty materials',
            'Do NOT ignore signs of infection'
        ]
    },
    'nosebleed': {
        'title': 'Nosebleed First Aid',
        'icon': '👃',
        'steps': [
            'Have the person sit upright',
            'Pinch the nose just below the bridge for 10-15 minutes',
            'Breathe through the mouth',
            'Apply a cold compress to the bridge',
            'Do NOT tilt head back',
            'Once bleeding stops, avoid blowing nose',
            'If bleeding persists beyond 20 minutes, seek medical help'
        ],
        'dont': [
            'Do NOT tilt head back',
            'Do NOT lie down',
            'Do NOT pack with cotton',
            'Do NOT blow nose forcefully'
        ]
    },
    'fractures': {
        'title': 'Fracture/Break First Aid',
        'icon': '🦴',
        'steps': [
            'Stop any bleeding with clean cloth',
            'Immobilize the injured area',
            'Apply ice wrapped in cloth for 15 minutes',
            'Elevate the injured limb if possible',
            'Do NOT move the injured area',
            'Get X-ray confirmation',
            'Follow medical advice for treatment'
        ],
        'dont': [
            'Do NOT move the injured area',
            'Do NOT apply ice directly',
            'Do NOT ignore swelling',
            'Do NOT continue using the injured limb'
        ]
    },
    'choking': {
        'title': 'Choking First Aid',
        'icon': '😮',
        'steps': [
            'Ask "Are you choking?" - if they cannot speak or cough, act immediately',
            'Stand behind the person',
            'Place fist just above navel, below ribcage',
            'Grasp fist with other hand',
            'Perform quick, upward thrusts (Heimlich maneuver)',
            'Repeat until object is expelled',
            'Seek medical help if unsuccessful'
        ],
        'dont': [
            'Do NOT leave them alone',
            'Do NOT perform back blows',
            'Do NOT delay if they cannot cough/speak'
        ]
    },
    'heat_stroke': {
        'title': 'Heat Stroke First Aid',
        'icon': '☀️',
        'steps': [
            'Move person to cool, shaded area immediately',
            'Call emergency services',
            'Remove excess clothing',
            'Cool the body with water, wet cloths, or ice packs',
            'Apply ice packs to armpits, groin, neck',
            'If conscious, give sips of water',
            'Monitor body temperature and breathing'
        ],
        'dont': [
            'Do NOT give ice water internally',
            'Do NOT leave them alone',
            'Do NOT delay medical help'
        ]
    },
    'snake_bite': {
        'title': 'Snake Bite First Aid',
        'icon': '🐍',
        'steps': [
            'Move away from the snake immediately',
            'Call emergency services or poison control',
            'Keep the bitten area immobilized',
            'Remove jewelry near the bite',
            'Wash bite area with soap and water',
            'Apply a pressure immobilization bandage',
            'Seek medical help immediately for antivenom'
        ],
        'dont': [
            'Do NOT cut or suck the bite',
            'Do NOT apply ice',
            'Do NOT use a tourniquet',
            'Do NOT try to catch the snake',
            'Do NOT delay medical treatment'
        ]
    },
    'allergic_reaction': {
        'title': 'Allergic Reaction First Aid',
        'icon': '🤧',
        'steps': [
            'Remove the allergen (food, substance, etc.)',
            'For severe reactions, call 911 immediately',
            'Give antihistamine if available',
            'For anaphylaxis, use EpiPen if available',
            'Have person lie down with legs elevated',
            'Monitor breathing and consciousness',
            'Seek medical help immediately'
        ],
        'dont': [
            'Do NOT ignore severe symptoms',
            'Do NOT delay emergency services for severe reactions',
            'Do NOT re-expose to allergen'
        ]
    }
}


def detect_emergency_condition(text: str) -> Tuple[bool, str, str]:
    """
    Detect if text contains emergency keywords.
    
    Args:
        text: User input text
    
    Returns:
        Tuple of (is_emergency, condition_type, response_message)
    """
    text_lower = text.lower()
    
    for condition_type, condition_info in EMERGENCY_CONDITIONS.items():
        for keyword in condition_info['keywords']:
            if keyword in text_lower:
                return True, condition_type, condition_info['response']
    
    return False, '', ''


def get_first_aid_guide(condition: str) -> Dict:
    """Get first aid guide for a specific condition."""
    return FIRST_AID_GUIDES.get(condition, {})


def get_all_first_aid_conditions() -> List[str]:
    """Get list of all available first aid conditions."""
    return list(FIRST_AID_GUIDES.keys())


def get_first_aid_condition_names() -> Dict:
    """Get dictionary of conditions with their titles and icons."""
    return {
        key: {
            'title': value['title'],
            'icon': value['icon']
        }
        for key, value in FIRST_AID_GUIDES.items()
    }
