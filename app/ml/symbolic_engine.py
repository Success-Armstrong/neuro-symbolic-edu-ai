def get_learning_advice(area, confidence):
    advice = {
        "html_score": "You may need to review HTML structure, tags, and forms.",
        "css_score": "Brush up on CSS Flexbox, Grid, and basic styling concepts.",
        "js_score": "Revisit JavaScript variables, functions, loops, and DOM basics."
    }

    confidence_note = {
        "low": "Confidence is low. Start with beginner tutorials and exercises.",
        "medium": "Confidence is moderate. Try mini-projects and practice problems.",
        "high": "Great confidence! Challenge yourself with real-world projects."
    }

    area_advice = advice.get(area, "All areas look good!")
    confidence_advice = confidence_note.get(confidence.lower(), "")
    
    return f"{area_advice} {confidence_advice}"
