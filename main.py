from fastapi import FastAPI
from pydantic import BaseModel
from random import choice

#We have this ExpressionModel to design our very own RequestBody using Pydantic BaseModel

class ExpressionModel(BaseModel):
    expression: str


app = FastAPI()


@app.post("/expression")
def eval_expr(expression: ExpressionModel):

    expr = expression.expression

    if expr.startswith("\'"):
        if isValidStrLiteral(expr):
            return expr
        else:
            return "You've entered an invalid string literal. a string literal is any set of characters except single quote between a pair of single quotes"
    elif is_function_invocation(expr):
        try:
            return eval(expr)
        except Exception as e:
            return "An error has occured. Kindly check your function invocation for syntax errors."
    else:
        return "You must have either entered a invalid string literal or made invalid function invocation. Kindly check your expression"


def concatenate(*words):
    if len(words) == 0:
        return "Minimum 1 parameter necessary for concatenate()"

    ans = ""

    for word in words:
        ans += word

    return ans


def join(*words):

    if len(words) < 3:
        return "Minimum of 3 parameters necessary for join()"

    return words[-1].join(words[:-1])


def pickRandom(*words):
    if len(words) < 1:
        return "Minimum of 1 parameter necessary for pickRandom()"

    return choice(words)


def isValidStrLiteral(str):
    return str.count("\'") % 2 == 0 and (str[0] == '\'' and str[-1] == '\'')


def is_function_invocation(functionCall: str):
    return functionCall.startswith("join") or functionCall.startswith("pickRandom") or functionCall.startswith("concatenate")
