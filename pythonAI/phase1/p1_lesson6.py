# Functions

def describe_profile(profile):
    return f"{profile.get('name')} is job-ready: {profile.get('job_ready')}"

profile = {"name": "Yiyakazah", "experience": 1, "job_ready": True}
print(describe_profile(profile))