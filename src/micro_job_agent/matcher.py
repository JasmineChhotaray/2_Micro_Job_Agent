from micro_job_agent.parser import extract_text_from_pdf
from micro_job_agent.ai_engine import extract_keywords_with_ai

# A simulated local database of active job listings
MOCK_JOBS_DB = [
    {
        "id": 101,
        "title": "Junior Python Developer",
        "company": "TechCorp Solutions",
        "required_skills": ["python", "git", "sql", "django"]
    },
    {
        "id": 102,
        "title": "Data Analyst Intern",
        "company": "DataMetrics Analytics",
        "required_skills": ["python", "sql", "pandas", "excel"]
    },
    {
        "id": 103,
        "title": "Cloud Infrastructure Engineer",
        "company": "Skyward Cloud Systems",
        "required_skills": ["docker", "aws", "linux", "git", "kubernetes"]
    }
]


def calculate_match_score(ai_keywords: str, job_skills: list[str]) -> tuple[int, list[str]]:
    """Compares AI keywords against a job's requirements and returns a score from 1-10."""
    # Convert AI keywords into a clean list of lowercase strings
    resume_skills_list = [skill.strip().lower() for skill in ai_keywords.split(",")]
    
    # Track which specific skills overlap
    matching_skills = [skill for skill in job_skills if skill in resume_skills_list]
    
    # Calculate an alignment percentage score
    if not job_skills:
        return 1, []
        
    overlap_ratio = len(matching_skills) / len(job_skills)
    
    # Scale the percentage to a clean 1-10 ranking rating
    score = int(1 + (overlap_ratio * 9))
    return score, matching_skills

def run_job_matcher(pdf_path: str):
    """Orchestrates the entire micro-agent pipeline."""
    print("Step 1: Parsing PDF locally...")
    raw_text = extract_text_from_pdf(pdf_path)
    
    print("Step 2: Contacting Groq Cloud for keyword extraction...")
    ai_keywords = extract_keywords_with_ai(raw_text)
    print(f" -> AI Keywords Found: {ai_keywords}\n")
    
    print("Step 3: Calculating local match evaluations...")
    print("=" * 50)
    print(f"{'JOB TITLE':<30} | {'SCORE (1-10)':<12} | {'MATCHED SKILLS'}")
    print("=" * 50)
    
    # Evaluate matches against each database entry
    for job in MOCK_JOBS_DB:
        score, matched = calculate_match_score(ai_keywords, job["required_skills"])
        matched_str = ", ".join(matched) if matched else "None"
        
        print(f"{job['title']:<30} | {score:<12}/10  | {matched_str}")
    print("=" * 50)


if __name__ == "__main__":
    # Test the complete integrated workspace workflow
    test_pdf = "sample_resume.pdf"
    run_job_matcher(test_pdf)