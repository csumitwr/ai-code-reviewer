from services.prompt_service import build_review_prompt
from services.ollama_service import generate_response

def generate_code_review(code, language, model):
    prompt = build_review_prompt(
        code=code,
        language=language
    )

    review = generate_response(
        prompt=prompt,
        model=model
    )

    return review