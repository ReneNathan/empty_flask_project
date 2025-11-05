# 🚀 Estrutura Básica de um Projeto Modular Flask  

Este repositório tem como objetivo fornecer uma **estrutura base moderna e modular** para projetos Flask, permitindo que desenvolvedores economizem tempo na etapa inicial de configuração e foquem diretamente na construção da aplicação.

---

## 🧰 Tecnologias Utilizadas  

| Tecnologia | Ícone | Descrição |
|-------------|:------:|-----------|
| **Python** | 🐍 | Linguagem principal do projeto |
| **Flask** | 🔥 | Microframework web leve e flexível |
| **HTML** | 🌐 | Estrutura e conteúdo das páginas |
| **CSS** | 🎨 | Estilização e responsividade |
| **JavaScript** | ⚡ | Interatividade e dinamismo |
| **UV** | 🧩 | Gerenciador de dependências e ambientes ([documentação oficial](https://docs.astral.sh/uv/)) |

---

## 🧭 Passos para Instalar as Dependências  

```bash
# 0️⃣ Caso ainda não tenha o UV instalado:
pip install uv

# 1️⃣ Clonar este repositório:
git clone https://github.com/ReneNathan/empty_flask_project.git
cd empty_flask_project

# 2️⃣ Criar o ambiente virtual e instalar dependências automaticamente:
uv sync

# 3️⃣ Executar o projeto dentro do ambiente virtual:
uv run

# 💡 Dica:
# O comando "uv sync" cria e ativa automaticamente o ambiente virtual,
# além de instalar todas as dependências listadas no arquivo "pyproject.toml".
```

---

## 📦 Dependências Incluídas no `.toml`

| Pacote | Descrição |
|---------|------------|
| **blinker** | Implementa sinais e eventos para Flask |
| **click** | Facilita a criação de comandos via terminal |
| **colorama** | Adiciona cores no terminal |
| **dotenv / python-dotenv** | Gerencia variáveis de ambiente a partir de arquivos `.env` |
| **flask** | Framework principal da aplicação |
| **itsdangerous** | Criptografia de dados e geração de tokens seguros |
| **jinja2** | Template engine para renderização HTML |
| **markupsafe** | Escapa HTML para maior segurança |
| **werkzeug** | Ferramentas WSGI e utilitários de servidor |

---

## 🎉 Pronto para Começar  

A estrutura já vem pronta para uso — basta iniciar o servidor Flask e começar a desenvolver sua aplicação modular.  

> 🧠 **Dica final:** mantenha suas rotas separadas em **Blueprints** e utilize um arquivo **.env** para armazenar variáveis sensíveis.  
> Dessa forma, seu projeto se mantém **limpo**, **escalável** e **profissional**.  
