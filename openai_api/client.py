import os
from openai import OpenAI

key=os.environ.get("API_KEY_OPEN_IA")
client = OpenAI(
    api_key=key
)

def get_car_ai_bio(model, brand, year):
    message = '''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 50 palavras. Fale coisas específicas desse modelo.
    Descreva especificações técnicas desse modelo de carro.
    '''
    message = message.format(brand, model, year)
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
     messages=[
        {"role": "user", "content": message}
    ]
    )
    return completion.choices[0].message.content
