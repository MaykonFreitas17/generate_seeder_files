from sqlalchemy import create_engine, inspect, text
import re

# Configuração do banco de dados
DATABASE_URL = "postgresql|mysql+mysqlconnector://seu_usuario:sua_senha@localhost:5432/seu_banco"
engine = create_engine(DATABASE_URL)
inspector = inspect(engine)

def formatar_nome_tabela(nome_tabela: str) -> str:
    """ Converte um nome de tabela do plural para o singular (PT-BR e EN) """
    
    regras_plural = [
        (r'oes$', 'ao'),   # Ações -> Ação
        (r'aes$', 'al'),   # Canais -> Canal
        (r'ies$', 'y'),    # Companies -> Company
        (r'zes$', 'z'),    # Narizes -> Nariz
        (r'is$', 'il'),    # Fuzis -> Fuzil
        (r'ns$', 'm'),     # Horizontes -> Horizonte
        (r'es$', ''),      # Boxes -> Box
        (r's$', ''),       # Carros -> Carro
    ]
    
    # Aplicar as regras de substituição
    for regra, substituicao in regras_plural:
        if re.search(regra, nome_tabela, re.IGNORECASE):
            return re.sub(regra, substituicao, nome_tabela, flags=re.IGNORECASE).capitalize()

    return nome_tabela  # Se nenhuma regra for aplicada, retorna o nome original

# Solicitar o nome da tabela ao usuário
nome_tabela = input("Digite o nome da tabela: ")

# Verificar se a tabela existe
if nome_tabela not in inspector.get_table_names():
    print("Tabela não encontrada no banco de dados.")
    exit()

# Obter colunas da tabela
colunas = [col["name"] for col in inspector.get_columns(nome_tabela)]

with engine.connect() as conn:
    registros = conn.execute(text(f"SELECT * FROM {nome_tabela}")).fetchall()

# Converter os registros em um formato de array associativo do PHP
dados_php = []
for registro in registros:
    item_php = "            [\n"
    for i, coluna in enumerate(colunas):
        valor = registro[i]
        # Verificar tipo e formatar corretamente
        if isinstance(valor, str):
            valor = f"'{valor}'"
        elif isinstance(valor, bool):
            valor = "true" if valor else "false"
        elif valor is None:
            valor = "null"
        item_php += f"                '{coluna}' => {valor},\n"
    item_php += "            ],"
    dados_php.append(item_php)

# Juntar os registros formatados
dados_php_string = "\n".join(dados_php)

# Carregar o modelo do seeder
with open("TemplateSeeder.php", "r", encoding="utf-8") as modelo:
    seeder_code = modelo.read()

# Substituir placeholders no modelo
seeder_code = seeder_code.replace("{{TABELA}}", nome_tabela)
seeder_code = seeder_code.replace("{{TABELA_CAPITALIZADA}}", f"{formatar_nome_tabela(nome_tabela)}Seeder")
seeder_code = seeder_code.replace("{{DADOS}}", dados_php_string)

# Salvar o novo seeder
nome_arquivo = f"{formatar_nome_tabela(nome_tabela)}Seeder.php"
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write(seeder_code)

print(f"Seeder PHP gerado com sucesso: {nome_arquivo}")