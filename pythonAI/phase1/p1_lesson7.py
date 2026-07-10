# Try/Except

def safe_get_experience(profile):
    try:
        return profile["experience"]
    except KeyError:
        return "Experience not found"
    
profile = {"name": "Yiyakazah", "experience": 1, "job_ready": True}
empty = {}   
print(safe_get_experience(profile))
print(safe_get_experience(empty))


