import os
import openai
import argparse


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input
    print(f"User input: {user_input}")

    result = generate_recipes(user_input)
    print(result)

def validateInput(user_prompt: str):
    print()


def generate_recipes(user_prompt: str) -> str:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    final_prompt = f"Write a recipe based on these ingredients and instructions: {user_prompt}"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=final_prompt,
        temperature=0.3,
        max_tokens=120,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )


    #get response text with stripped spaces
    recipe_text: str = response["choices"][0]["text"].strip()
    last_char = recipe_text[-1]

    if last_char not in {".", "!", "?"}:
        recipe_text += "..."

    return recipe_text


if __name__ == "__main__":
    main()
