# 🤖 J.A.R.V.I.S - Chatbot OpenAI

Este projeto é uma aplicação interativa desenvolvida com **Python** e **Streamlit** que permite conversar com modelos de IA da **OpenAI (GPT-3.5 e GPT-4)**, simulando um assistente pessoal chamado **J.A.R.V.I.S**.

---

## 🚀 Funcionalidades

- Integração com modelos da **OpenAI API**: GPT-3.5-Turbo e GPT-4
- Interface leve e amigável com **Streamlit**
- Histórico de conversas salvos localmente
- Reabertura e continuidade de conversas anteriores
- Configuração fácil da API Key via interface
- Controle do modelo escolhido e chave diretamente na aplicação

---

## 🎯 Como usar

### 1. Clone o repositório

bash
git clone https://github.com/seu-usuario/jarvis-chatbot.git
cd jarvis-chatbot

# 2. Instale as dependências
De preferência, utilize um ambiente virtual:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Depois instale os pacotes:

bash
Copy
Edit
pip install -r requirements.txt
# 3. Configure sua API Key
A aplicação precisa da sua API Key da OpenAI para funcionar. Você pode obtê-la em: https://platform.openai.com/api-keys

Assim que iniciar o app, vá até a aba Configurações e cole sua chave.

# 4. Execute o projeto
bash
Copy
Edit
streamlit run app.py
# 🧩 Estrutura do projeto
bash
Copy
Edit
├── app.py                      # Código principal da aplicação
├── utils_openai.py             # Funções de comunicação com API OpenAI
├── utils_file.py               # Funções para salvar, ler e gerenciar conversas e API Key
├── conversas/                  # Pasta onde ficam salvos os históricos de conversas
├── .env (opcional)             # Para guardar a API Key localmente
└── requirements.txt            # Dependências do projeto
# 🎥 Funcionalidades Principais
✅ Envie perguntas no chat e receba respostas instantâneas
✅ Escolha entre GPT-3.5-Turbo e GPT-4
✅ Salve automaticamente o histórico de cada conversa
✅ Acesse e continue conversas anteriores
✅ Gerencie sua API Key diretamente pela interface

# 👨‍💻 Tecnologias
Python

Streamlit

OpenAI API

# 🔐 Requisitos
Para usar este projeto, é necessário:

Conta na OpenAI

Chave de API válida

# 🧑‍🏫 Desenvolvido por
Leandro Souza

# ⭐️ Licença
Uso livre para fins acadêmicos, pessoais ou estudos.
Sinta-se à vontade para contribuir com melhorias!
