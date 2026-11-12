from openai import OpenAI
from google import genai
from google.genai import types


def generate_openai(
    prompt, api_key, temperature, model, max_tokens
):

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_completion_tokens=max_tokens
    )

    return response.choices[0].message.content or ""


def generate_gemini(
    prompt, api_key, temperature, model, max_tokens
):

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=temperature,
            max_output_tokens=max_tokens
        )
    )

    return response.text or ""