def generate_diet(plan_title, duration):
    title = plan_title.lower()

    if "fat loss" in title:
        return {
            "diet_type": "Calorie Deficit",
            "calories": 1800,
            "protein": 140,
            "carbs": 150,
            "fats": 50
        }

    elif "muscle" in title or "gain" in title:
        return {
            "diet_type": "High Protein",
            "calories": 2800,
            "protein": 180,
            "carbs": 300,
            "fats": 80
        }

    elif "beginner" in title:
        return {
            "diet_type": "Balanced Diet",
            "calories": 2200,
            "protein": 120,
            "carbs": 250,
            "fats": 70
        }

    else:
        return {
            "diet_type": "General Fitness",
            "calories": 2400,
            "protein": 130,
            "carbs": 260,
            "fats": 75
        }
