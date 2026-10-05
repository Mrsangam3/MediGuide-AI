import json
from pathlib import Path


# ---------------------------------------------------------
# Load red flag configuration
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
RED_FLAGS_FILE = BASE_DIR / "red_flags.json"

with open(RED_FLAGS_FILE, "r", encoding="utf-8") as file:
    RED_FLAGS = json.load(file)


# ---------------------------------------------------------
# Emergency patterns
# ---------------------------------------------------------

RED_FLAG_PATTERNS = {

    "severe_difficulty_breathing": [
        "can't breathe",
        "cannot breathe",
        "difficulty breathing",
        "hard to breathe",
        "struggling to breathe",
        "trouble breathing",
        "shortness of breath"
    ],

    "unable_to_speak_due_to_breathlessness": [
        "can't speak because i can't breathe",
        "cannot speak because i can't breathe",
        "can't talk because i can't breathe",
        "unable to speak because of breathing"
    ],

    "choking_or_unable_to_get_air": [
        "choking",
        "i am choking",
        "can't get air",
        "cannot get air"
    ],

    "blue_or_gray_lips_or_face": [
        "blue lips",
        "blue lips or face",
        "lips are turning blue",
        "face is turning blue",
        "gray lips",
        "grey lips"
    ],

    "severe_or_crushing_chest_pain": [
        "crushing chest pain",
        "severe chest pain",
        "heavy chest pain",
        "pressure in my chest",
        "crushing pain in my chest"
    ],

    "chest_pain_with_severe_breathlessness": [
        "chest pain and difficulty breathing",
        "chest pain and shortness of breath",
        "chest pain and can't breathe",
        "chest pain with trouble breathing"
    ],

    "sudden_one_sided_weakness": [
        "one side is weak",
        "one side of my body is weak",
        "suddenly weak on one side",
        "sudden weakness on one side",
        "my right arm is suddenly weak",
        "my left arm is suddenly weak"
    ],

    "sudden_one_sided_numbness": [
        "one side is numb",
        "one side of my body is numb",
        "sudden numbness on one side",
        "my right side is numb",
        "my left side is numb"
    ],

    "sudden_facial_drooping": [
        "face is drooping",
        "facial drooping",
        "one side of my face is drooping",
        "my face suddenly drooped"
    ],

    "sudden_speech_difficulty": [
        "can't speak properly",
        "cannot speak properly",
        "suddenly can't speak",
        "suddenly cannot speak",
        "slurred speech",
        "speech is slurred"
    ],

    "sudden_confusion": [
        "suddenly confused",
        "sudden confusion",
        "i am suddenly confused",
        "became confused suddenly"
    ],

    "new_loss_of_consciousness": [
        "i passed out",
        "i fainted",
        "i lost consciousness",
        "unconscious",
        "passed out suddenly"
    ],

    "new_seizure": [
        "i am having a seizure",
        "i had a seizure",
        "seizure",
        "convulsion"
    ],

    "sudden_vision_loss": [
        "suddenly can't see",
        "suddenly cannot see",
        "lost my vision",
        "sudden vision loss",
        "suddenly lost vision"
    ],

    "sudden_extremely_severe_headache": [
        "worst headache of my life",
        "worst headache i've ever had",
        "sudden severe headache",
        "sudden extremely severe headache",
        "thunderclap headache"
    ],

    "suspected_medication_overdose": [
        "overdose",
        "took too many pills",
        "took too much medicine",
        "took too many tablets",
        "took more medicine than I should"
    ],

    "intentional_medication_overdose": [
        "intentionally took too many pills",
        "deliberately took too many pills",
        "took an overdose intentionally",
        "overdosed on purpose"
    ],

    "immediate_intent_to_self_harm": [
        "i want to kill myself",
        "i am going to kill myself",
        "i plan to kill myself",
        "i am going to hurt myself",
        "i want to hurt myself"
    ]
}


# ---------------------------------------------------------
# Urgent patterns
# ---------------------------------------------------------

URGENT_PATTERNS = {

    "persistent_vomiting": [
        "vomiting for more than 24 hours",
        "vomiting for over 24 hours",
        "been vomiting all day",
        "vomiting repeatedly",
        "vomiting won't stop",
        "vomiting does not stop"
    ],

    "unable_to_keep_fluids_down": [
        "can't keep fluids down",
        "cannot keep fluids down",
        "can't keep water down",
        "cannot keep water down",
        "unable to keep fluids down"
    ],

    "persistent_abdominal_pain": [
        "stomach pain for several days",
        "abdominal pain for several days",
        "stomach pain that is getting worse",
        "abdominal pain that is getting worse",
        "stomach pain that won't go away",
        "abdominal pain that won't go away"
    ],

    "persistent_diarrhea": [
        "diarrhea for more than 5 days",
        "diarrhea for over 5 days",
        "diarrhea that won't stop"
    ],

    "persistent_fever": [
        "fever for more than 3 days",
        "fever for over 3 days",
        "fever that keeps coming back",
        "fever that won't go away"
    ],

    "possible_dehydration": [
        "i haven't urinated all day",
        "i have not urinated all day",
        "very dark urine and dizziness",
        "very dark urine and feeling dizzy",
        "i am very thirsty and dizzy"
    ]
}

CAUTION_PATTERNS = {

    "headache": [
        "headache",
        "my head hurts",
        "pain in my head"
    ],

    "dizziness": [
        "dizzy",
        "i feel dizzy",
        "feeling dizzy",
        "lightheaded"
    ],

    "stomach_pain": [
        "stomach pain",
        "stomach ache",
        "abdominal pain",
        "my stomach hurts"
    ],

    "fever": [
        "i have a fever",
        "fever",
        "temperature"
    ],

    "rash": [
        "i have a rash",
        "skin rash",
        "rash on my skin"
    ],

    "weakness": [
        "i feel weak",
        "feeling weak",
        "weakness"
    ]
}

CAUTION_QUESTIONS = {

    "headache": [
        "How long have you had the headache?",
        "How severe is it?",
        "Is it getting worse or staying the same?",
        "Do you have any other symptoms such as fever, vomiting, vision changes, weakness, or confusion?"
    ],

    "dizziness": [
        "How long have you been feeling dizzy?",
        "Did the dizziness start suddenly?",
        "Are you having trouble walking or keeping your balance?",
        "Do you have any other symptoms?"
    ],

    "stomach_pain": [
        "Where exactly is the pain?",
        "How long have you had it?",
        "How severe is the pain?",
        "Is the pain getting worse?",
        "Do you have vomiting, diarrhea, fever, or blood in your stool?"
    ],

    "fever": [
        "What is your temperature, if you have measured it?",
        "How long have you had the fever?",
        "Do you have any other symptoms?",
        "Are you able to drink fluids normally?"
    ],

    "rash": [
        "When did the rash start?",
        "Where is the rash located?",
        "Is it spreading?",
        "Is it itchy or painful?",
        "Do you have fever, swelling, or difficulty breathing?"
    ],

    "weakness": [
        "When did the weakness start?",
        "Is the weakness affecting one side or your whole body?",
        "Is it getting worse?",
        "Do you have dizziness, difficulty speaking, numbness, or difficulty walking?"
    ]
}


# ---------------------------------------------------------
# Triage detection
# ---------------------------------------------------------

def detect_red_flags(message):
    """
    Analyze a user's message for safety signals.

    Returns:
        triage_level:
            emergency
            urgent
            routine

        signals:
            Detected safety signals.

        requires_immediate_action:
            True for emergency cases.

        normal_medication_flow_allowed:
            False when the normal medication/chat flow
            should be stopped.
    """

    message_lower = message.lower()

    detected_signals = []


    # -----------------------------------------------------
    # Check emergency signals first
    # -----------------------------------------------------

    for signal, patterns in RED_FLAG_PATTERNS.items():

        for pattern in patterns:

            if pattern.lower() in message_lower:

                detected_signals.append({
                    "signal": signal,
                    "matched_text": pattern,
                    "level": "emergency"
                })

                break


    # -----------------------------------------------------
    # Emergency always takes priority
    # -----------------------------------------------------

    if detected_signals:

        return {
            "triage_level": "emergency",
            "signals": detected_signals,
            "requires_immediate_action": True,
            "normal_medication_flow_allowed": False
        }


    # -----------------------------------------------------
    # Check urgent signals
    # -----------------------------------------------------

    for signal, patterns in URGENT_PATTERNS.items():

        for pattern in patterns:

            if pattern.lower() in message_lower:

                detected_signals.append({
                    "signal": signal,
                    "matched_text": pattern,
                    "level": "urgent"
                })

                break


    # -----------------------------------------------------
    # Urgent case
    # -----------------------------------------------------

    if detected_signals:

        return {
            "triage_level": "urgent",
            "signals": detected_signals,
            "requires_immediate_action": False,
            "normal_medication_flow_allowed": False
        }


    # -----------------------------------------------------
    # Routine case
    # -----------------------------------------------------

    return {
        "triage_level": "routine",
        "signals": [],
        "requires_immediate_action": False,
        "normal_medication_flow_allowed": True
    }


# ---------------------------------------------------------
# Local testing
# ---------------------------------------------------------

if __name__ == "__main__":

    test_messages = [

        # Emergency tests
        "I have severe chest pain and I can't breathe",
        "My right arm suddenly became weak",
        "I suddenly can't see properly",
        "I took too many tablets",
        "I am having a seizure",
        "My lips are turning blue and I can't breathe",

        # Routine tests
        "I have a normal headache today",
        "I have a mild sore throat",
        "I have a stomach ache after eating",
        "I don't have difficulty breathing",

        # Urgent tests
        "I have been vomiting for more than 24 hours",
        "I can't keep fluids down",
        "My stomach pain has been getting worse",
        "I have had a fever for more than 3 days"
    ]


    for message in test_messages:

        result = detect_red_flags(message)

        print("\n" + "=" * 60)

        print("MESSAGE:", message)

        print("TRIAGE:", result["triage_level"])

        print("SIGNALS:", result["signals"])

        print(
            "IMMEDIATE ACTION:",
            result["requires_immediate_action"]
        )

        print(
            "NORMAL MEDICATION FLOW:",
            result["normal_medication_flow_allowed"]
        )

def detect_red_flags(message):
    """
    Analyze a user's message for safety signals.

    This version recognizes simple negation such as:
    - I don't have difficulty breathing
    - I do not have chest pain
    - No shortness of breath

    Emergency signals always take priority over urgent signals.
    """

    message_lower = message.lower()

    detected_signals = []

    # Common negation phrases
    negation_phrases = [
        "i don't have",
        "i do not have",
        "i dont have",
        "no",
        "without",
        "denies",
        "denying"
    ]

    def is_negated(pattern):
        """
        Check whether a matched symptom appears to be negated.
        This is intentionally simple and is not a clinical NLP system.
        """

        pattern_position = message_lower.find(pattern.lower())

        if pattern_position == -1:
            return False

        text_before = message_lower[:pattern_position]

        # Look at the nearby words before the symptom.
        words_before = text_before.split()[-5:]

        nearby_text = " ".join(words_before)

        for negation in negation_phrases:

            if negation in nearby_text:
                return True

        return False


    # -----------------------------------------------------
    # Check emergency signals
    # -----------------------------------------------------

    for signal, patterns in RED_FLAG_PATTERNS.items():

        for pattern in patterns:

            if pattern.lower() in message_lower:

                if not is_negated(pattern):

                    detected_signals.append({
                        "signal": signal,
                        "matched_text": pattern,
                        "level": "emergency"
                    })

                break


    # -----------------------------------------------------
    # Emergency always takes priority
    # -----------------------------------------------------

    if detected_signals:

        return {
            "triage_level": "emergency",
            "signals": detected_signals,
            "requires_immediate_action": True,
            "normal_medication_flow_allowed": False
        }


    # -----------------------------------------------------
    # Check urgent signals
    # -----------------------------------------------------

    for signal, patterns in URGENT_PATTERNS.items():

        for pattern in patterns:

            if pattern.lower() in message_lower:

                if not is_negated(pattern):

                    detected_signals.append({
                        "signal": signal,
                        "matched_text": pattern,
                        "level": "urgent"
                    })

                break


    # -----------------------------------------------------
    # Urgent case
    # -----------------------------------------------------

    if detected_signals:

        return {
            "triage_level": "urgent",
            "signals": detected_signals,
            "requires_immediate_action": False,
            "normal_medication_flow_allowed": False
        }

    # -----------------------------------------------------
    # Check caution signals
    # -----------------------------------------------------

    for signal, patterns in CAUTION_PATTERNS.items():

        for pattern in patterns:

            if pattern.lower() in message_lower:

                if not is_negated(pattern):

                    return {
                        "triage_level": "caution",
                        "signals": [
                            {
                                "signal": signal,
                                "matched_text": pattern,
                                "level": "caution"
                            }
                        ],
                        "requires_immediate_action": False,
                        "normal_medication_flow_allowed": False,
                        "follow_up_questions": CAUTION_QUESTIONS.get(
                            signal,
                            []
                        )
                    }

                break

    # -----------------------------------------------------
    # Routine case
    # -----------------------------------------------------

    return {
        "triage_level": "routine",
        "signals": [],
        "requires_immediate_action": False,
        "normal_medication_flow_allowed": True,
        "follow_up_questions": []
    }


if __name__ == "__main__":

    test_messages = [
        "I have a headache",
        "I feel dizzy",
        "I have stomach pain",
        "I have a rash",
        "I have a fever",
        "I feel weak"
    ]

    for message in test_messages:
        result = detect_red_flags(message)
        print(f"Message: {message}")
        print(f"Result: {result}\n")