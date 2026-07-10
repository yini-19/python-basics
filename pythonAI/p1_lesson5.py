# Loops
tools = ["requests", "json", "os"]
tools.append("openai")
profile = {"name": "Yiyakazah", "experience": 1, "job_ready": True}
profile["target_role"] = "AI Engineer"

for i, tool in enumerate(tools):
    print(i, tool)

for key, value in profile.items():
    print(f"{key}: {value}")