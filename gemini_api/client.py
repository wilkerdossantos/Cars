import google.generativeai as genai
import os

genai.configure(api_key=os.environ["API_KEY_GEMINI"])


def get_car_ai_bio(model, brand, year):
    model = genai.GenerativeModel('gemini-1.5-flash')
    message = 'Você é um gerente de marketing de uma revenda de carros e precisa criar uma descrição de venda para o carro Marca:{}, Modelo:{}, Ano:{}, informando suas especificações tecnicas, com 50 palavras, sem modelo, sem marca, sem markdown'
    message = message.format(brand, model, year)
    response = model.generate_content(message)
    return response.text