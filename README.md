# Assistente-DehAI
🧠 Assistente DehAI:
DehAI é um assistente de IA desenvolvido em Python, utilizando a Groq API e o modelo LLaMA 3.1, focado em oferecer respostas rápidas, diretas e naturais.
Foi criada por Débora Córdova (eu) como parte de seu portfólio técnico e estudos em Inteligência Artificial.

→ Recursos:

• Comunicação via terminal (CLI)

• Respostas geradas pelo modelo LLaMA 3.1 (Groq)

• Arquitetura simples e modular:

• main.py → interface com o usuário

• ia.py → lógica da IA e conexão com a API

• Ambiente seguro com uso de variáveis .env

• requirements.txt incluído para fácil instalação

🛠 Como executar:

1. Clone o repositório:
git clone https://github.com/DeboraCordova/Assistente-DehAI.git

2. Instale as dependências:
pip install -r requirements.txt

3. Crie seu arquivo .env e adicione:
GROQ_API_KEY=sua_chave_aqui

4. Execute o assistente:
python main.py

→ Estrutura do Projeto:📁

Assistente-DehAI/
│── main.py
│── ia.py
│── requirements.txt
│── .gitignore
└── README.md

→ Observações:

• A chave da API não é incluída no repositório por motivos de segurança.

• O nome "DehAI" ainda é provisório — aberto para sugestões e melhorias futuras.
