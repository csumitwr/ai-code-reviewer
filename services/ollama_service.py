import ollama

def generate_response(prompt, model):
    try:
        response = ollama.chat(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        content = response["message"]["content"]

        if not content.strip():
            return "Error: Empty response received from the model."

        return content

    except Exception as e:
        return f"Error: {str(e)}"