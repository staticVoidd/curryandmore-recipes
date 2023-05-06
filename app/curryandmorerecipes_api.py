from curryandmorerecipes import generate_recipes
from fastapi import FastAPI, HTTPException
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)

# uvicorn curryandmorerecipes_api:app --reload

@app.get("/generate_recipes")
async def generate_recipes_api(prompt: str):
    validate_user_input(prompt)
    recipe = generate_recipes(prompt)
    return {"recipe": f"{recipe}"}

def validate_user_input(prompt: str):
    if len(prompt) < 4 :
        raise HTTPException(
            status_code=400,
            detail=f"Input length must be more than 1 characters.",
        )