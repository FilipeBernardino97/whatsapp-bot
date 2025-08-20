import requests
from flask import Flask, request
import os

app = Flask(__name__)

# Configuração via variáveis de ambiente
TOKEN = os.getenv("WHATSAPP_TOKEN", "SEU_TOKEN_AQUI")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID", "SEU_PHONE_ID_AQUI")
URL = f"https://graph.facebook.com/v17.0/{PHONE_NUMBER_ID}/messages"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# Função para enviar mensagem
def send_message(to, text):
    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": text}
    }
    response = requests.post(URL, headers=HEADERS, json=data)
    print(response.json())
    return response.json()

# Webhook para receber mensagens
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    print(data)

    if "messages" in str(data):
        user_number = data["entry"][0]["changes"][0]["value"]["messages"][0]["from"]
        user_text = data["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]

        # Respostas automáticas
        if "oi" in user_text.lower():
            send_message(user_number, "Olá! Seja bem-vindo 👋")
        elif "preço" in user_text.lower():
            send_message(user_number, "Nossos preços começam em R$100")
        else:
            send_message(user_number, "Desculpe, não entendi. Pode repetir?")

    return "OK", 200

# Rota inicial só para teste
@app.route("/", methods=["GET"])
def home():
    return "Bot de WhatsApp está rodando 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
