📱 WhatsApp Bot em Python

Este projeto é um bot para WhatsApp desenvolvido em Python + Flask, utilizando a Meta Cloud API.
O objetivo é automatizar mensagens no WhatsApp, permitindo criar atendimentos automáticos, envio de promoções, respostas rápidas e muito mais.

🚀 Funcionalidades

Responde automaticamente mensagens recebidas no WhatsApp.

Reconhece palavras-chave como “oi” e “preço”.

Fácil de expandir para criar FAQ, lembretes, agendamento e vendas.

Hospedagem gratuita usando Render.

🛠️ Tecnologias

Python 3

Flask (API REST)

Requests (integração com WhatsApp API)

Gunicorn (servidor para deploy)

📂 Estrutura do Projeto
whatsapp-bot/
│── bot.py              # Código principal do bot
│── requirements.txt    # Dependências do projeto
│── Procfile            # Configuração para deploy no Render
│── README.md           # Documentação

⚙️ Como rodar localmente

Clone este repositório:

git clone https://github.com/seu-usuario/whatsapp-bot.git
cd whatsapp-bot


Crie um ambiente virtual e instale dependências:

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt


Configure variáveis de ambiente:

export WHATSAPP_TOKEN="seu_token_meta"
export PHONE_NUMBER_ID="seu_id_telefone"


Execute o bot:

python bot.py


O bot rodará em http://localhost:5000.

🌍 Deploy no Render

Suba o projeto no GitHub.

Crie um Web Service no Render
.

Configure as variáveis de ambiente:

WHATSAPP_TOKEN

PHONE_NUMBER_ID

O Render fornecerá uma URL pública, que você deve configurar como Webhook no Meta Developers
.

💡 Exemplos de uso

Cliente manda: oi
→ Bot responde: Olá! Seja bem-vindo 👋

Cliente manda: preço
→ Bot responde: Nossos preços começam em R$100

📌 Próximos Passos

 Adicionar banco de dados para salvar conversas

 Criar menus interativos (botões, listas)

 Integrar com Google Sheets / CRM

👨‍💻 Autor

Projeto desenvolvido por Filipe Bernardino 🚀
Se gostou, deixe uma ⭐ no repositório!
