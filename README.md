# Automatizador de Transmissão

Automatizador desenvolvido para auxiliar igrejas na inicialização de transmissões ao vivo no YouTube, simplificando o processo e economizando tempo. 

## 🚀 Sobre o Projeto

Este projeto foi criado para facilitar a vida de administradores e equipes técnicas de igrejas que precisam configurar transmissões ao vivo no YouTube. Com ele, é possível automatizar a criação e gerenciamento de transmissões diretamente através da API do YouTube, utilizando o protocolo OAuth para autenticação do usuário.

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal para o desenvolvimento da aplicação.
- **YouTube Data API v3**: Para interação com as funcionalidades do YouTube, como criar transmissões e gerenciar configurações.
- **OAuth 2.0**: Para autenticação e autorização segura do usuário.

## 📦 Funcionalidades

- Criação automatizada de transmissões ao vivo no YouTube.
- Autenticação segura via OAuth 2.0 para acessar a conta do usuário.
- Configuração prévia das transmissões, como título, descrição, data e hora.
- Facilidade para configurar e gerenciar várias transmissões rapidamente.

## 🚧 Pré-requisitos e Configuração

### Pré-requisitos

Antes de começar, você precisará ter o seguinte instalado na sua máquina:

- Python 3.7 ou superior
- Conta de desenvolvedor no Google Cloud para configurar o acesso à API do YouTube

### Configuração

**1. Clone o repositório:**

   bash
   git clone https://github.com/seu-usuario/AutomatizadorTransmissao.git
   cd AutomatizadorTransmissao

**2. Instale as dependências:**

bash
pip3 install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
pip3 install customtkinter

**3. Configure o acesso à API do YouTube:**

Crie um projeto no Google Cloud Console.
Ative a YouTube Data API v3.
Configure o OAuth 2.0 e baixe as credenciais JSON.
Renomeie o arquivo de credenciais para client_secrets.json e coloque-o na raiz do projeto.

**4. Execute a aplicação:**

bash
python main.py

**📚 Documentação da API**
Para mais informações sobre as funcionalidades utilizadas, consulte a documentação oficial da YouTube Data API.

**🤝 Contribuindo**
Contribuições são bem-vindas! Se você tiver sugestões de melhorias, abra uma issue ou envie um pull request.

Faça um fork do projeto.
Crie uma branch com sua funcionalidade (git checkout -b minha-funcionalidade).
Faça um commit das mudanças (git commit -m 'Adiciona minha funcionalidade').
Faça o push para a branch (git push origin minha-funcionalidade).
Abra um pull request.

✨ Agradecimentos
A equipe de suporte da YouTube Data API pelo guia inicial.

Desenvolvido com ❤️ por Cainã Giarola
