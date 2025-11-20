# Agente de Carreira Adaptativa (ACA) 🎯
Sistema inteligente de recomendação profissional que analisa competências e interesses para sugerir carreiras em tecnologia e inovação.

📋 Sobre o Projeto
O ACA é uma aplicação Python que avalia perfis profissionais baseado em 5 dimensões-chave e recomenda entre 26 carreiras diferentes no mercado de tecnologia.

Funcionalidades Principais
✅ Análise de Perfil: Avalia 5 competências (criatividade, interesse, lógica, afinidade, adaptabilidade)

✅ Recomendação Inteligente: Sugere carreiras adequadas ao perfil

✅ Gestão de Leads: Armazena e organiza perfis cadastrados

✅ Busca e Filtros: Localiza perfis por nome, e-mail ou área

# 🚀 Como Executar: 
> terminal
```
# Clone o repositório
git clone <url-do-repositorio>
cd PCP-G52

# Execute o programa
python app.py
```

> Menu Principal
```
Agente de Carreira Adaptativa (ACA)
[1] Adicionar Perfil
[2] Listar Perfis  
[3] Buscar Áreas
[4] Exibir Áreas Disponíveis
[0] Sair
```

# 📁 Estrutura do Projeto
> text
```
PCP-G52/
├── app.py              # Aplicação principal
├── stages.py           # Classes e sistema de carreiras
├── repo.py             # Persistência de dados
├── data/
│   └── profiles.json   # Armazenamento (auto-gerado)
└── README.md
```

Principais Classes

- *Perfil: Classe base com dados do usuário*

- *Competência: Adiciona dimensões de avaliação*

- *Carreira: Sistema de recomendação com 26 carreiras*

- *ModelRepository: Persistência em JSON*

# 🎯 Carreiras Disponíveis
O sistema mapeia 26 carreiras organizadas em grupos:

Área	Exemplos
Cientista de Dados, DevOps, Engenheiro de IA e etc...

# 💾 Armazenamento
Os dados são salvos automaticamente em data/profiles.json com a estrutura:

> json
```
{
  "name": "João Silva",
  "email": "joao@email.com", 
  "stage": "novo",
  "perfil_type": "Product Manager",
  "interesse": true
}
```

# Demonstração 1:
<img width="581" height="319" alt="image" src="https://github.com/user-attachments/assets/c64f28de-0e85-4ced-af11-a520dad3bb6a" />

# Demonstração 2:
<img width="677" height="281" alt="image" src="https://github.com/user-attachments/assets/8e77129b-44cd-412a-b6c4-e1b16e39d5cc" />

# Demonstração 3:
<img width="513" height="743" alt="image" src="https://github.com/user-attachments/assets/374452bd-9fac-4406-b29d-afa5fc14250c" />

# Demonstração 4:
<img width="677" height="396" alt="image" src="https://github.com/user-attachments/assets/67a94159-ffab-4f24-80f1-8ed558057310" />


