from fastapi import FastAPI

app = FastAPI()

@app.post("/calculator")
def calculator(num1: int, num2: int, op: str):
    if op == "+":
        return {num1 + num2}
    if op == "-":
        return {num1 - num2}
    if op == "*":
        return {num1 * num2}
    if op == "/":
        return {num1 / num2}
    return {"Ошибка"}
