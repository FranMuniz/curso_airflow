## 🚀 Curso de Apache Airflow

Este repositório contém o conteúdo prático e teórico do **Curso de Apache Airflow**, voltado para o desenvolvimento de pipelines de dados escaláveis, automação de workflows e orquestração de tarefas.

---

### 📚 Conteúdo

Este curso abrange os seguintes tópicos:

- 🔧 Instalação e configuração do Airflow com Docker Compose
- 📂 Estrutura recomendada de pastas para projetos Airflow
- ✈️ Conceitos fundamentais:
  - DAGs
  - Operadores (Python, Bash, etc.)
  - Sensors
  - XComs
- 🔄 Agendamento com CRON Expressions
- 📡 Integração com APIs
- 🗃️ Conexões com bancos de dados (PostgreSQL)
- 🐘 Exemplo de uso com PostgreSQL
- 📤 Envio de dados para o Amazon S3
- 🧹 Boas práticas na criação de DAGs
- 📈 Monitoramento e Logging

---

## 🗂️ Estrutura do Projeto

```bash
curso_airflow/
│
├── dags/                  # DAGs definidas em Python
│   ├── exemplo_simples.py
│   └── ingestao_postgres_s3.py
│
├── plugins/               # Plugins customizados (se houver)

├── docker-compose.yaml    # Arquivo para subir o ambiente com Docker
│
├── .env                   # Variáveis de ambiente sensíveis
│
└── README.md              # Documentação do projeto
