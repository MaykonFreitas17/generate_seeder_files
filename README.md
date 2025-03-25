# 🚀 Gerador de Seeders PHP com Python

Este projeto permite gerar arquivos de **Seeder PHP** a partir dos dados de um banco de dados PostgreSQL, utilizando **Python** e **SQLAlchemy**.

## 🛠️ Pré-requisitos
Antes de começar, certifique-se de ter instalado:
- **Python 3.10+**
- **PostgreSQL**
- **pip** (gerenciador de pacotes do Python)
- **Virtualenv** (para isolamento de dependências)

## 📥 Clonando o repositório
```bash
git clone https://github.com/MaykonFreitas17/generate_seeder_files.git
cd seu-repositorio
```

## 🌍 Criando e ativando um ambiente virtual (venv)
Para garantir que as dependências sejam instaladas corretamente sem interferir em outros projetos, crie um ambiente virtual:

### **Linux/macOS**
```bash
python -m venv venv
source venv/bin/activate
```

### **Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

## 📦 Instalando as dependências
Depois de ativar o ambiente virtual, instale as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```

## ⚙️ Configuração do banco de dados
Antes de rodar o projeto, configure a conexão com o banco no arquivo **`.env`**:

```
DATABASE_URL=postgresql://usuario:senha@localhost:5432/seu_banco
```

Se necessário, edite o código para usar essas credenciais.

## ▶️ Executando o script
Para gerar um Seeder a partir de uma tabela do banco de dados, execute:
```bash
python app.py
```
Digite o nome da tabela quando solicitado.

## 🚀 Alternativa: Usando Poetry
Caso prefira gerenciar pacotes com **Poetry**, instale as dependências assim:
```bash
poetry install
```
E execute o projeto:
```bash
poetry run python app.py
```

## 🎯 Dúvidas?
Caso tenha dúvidas ou queira contribuir, sinta-se à vontade para abrir uma issue ou pull request no repositório!

---
Desenvolvido com ❤️ por Maykon Freitas

