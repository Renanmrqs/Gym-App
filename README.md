# Gym App

🚧 Em desenvolvimento

## Demo 

[Demo Do Projeto](https://gym-app-eggj82u2wknfk48seq2tmy.streamlit.app/)

---

Evolução do projeto [Gym Register](https://github.com/Renanmrqs/Gym-Register) — que começou como projeto final do curso CS50P de Harvard em CLI — agora com frontend completo em Streamlit consumindo a [Gym API](https://github.com/Renanmrqs/Gym-Api), construída com FastAPI e SQLite durante o estudo do curso Introduction to SQL de Harvard.

---

## Sobre o projeto

Três fases de evolução:

- **Gym Register** — CLI em Python (CS50P final project)
- **Gym API** — API REST com FastAPI + SQLite (Introduction to SQL - Harvard)
- **Gym App** — Frontend em Streamlit consumindo a API ← você está aqui

---

## Páginas

### Login
Autenticação via JWT — token salvo no session_state e enviado no header das requisições protegidas. Páginas sensíveis bloqueiam acesso sem login.

![Login](img/login.png)

### Register
Cadastro de novo usuário. Senha hasheada com Argon2 antes de ser armazenada.

![Register](img/register.png)

### Dashboard
Visão geral dinâmica por usuário logado — exercícios cadastrados, treinos completos, séries realizadas e maior peso registrado.

![Dashboard](img/dashboard.png)

### Register Training
Fluxo completo para registrar um treino: seleção do usuário, escolha do exercício, quantidade de séries, peso e reps. Requer autenticação.

![Register Treino](img/register_treine.png)

### Historic
Consulta o histórico de treinos por usuário — exercício, data, peso e reps de cada série registrada.

![Historic](img/historic.png)

### Exercises
Cadastro e listagem de exercícios disponíveis. Requer autenticação para cadastrar.

![Exercises](img/add_exercices.png)

---

## Tecnologias

- Python 
- Streamlit
- Requests

---

## Como rodar

- **Deploy na nuvem do streamlit:**

[Deploy](https://gym-app-eggj82u2wknfk48seq2tmy.streamlit.app/)

- **Passo a passo para rodar localmente:**

```bash
# Clone o repositório
git clone https://github.com/Renanmrqs/Gym-App
cd Gym-App

# Instale as dependências
pip install streamlit requests

# Rode o app
streamlit run app.py
```

---

## API

O app consome a Gym API hospedada no Railway:

🔗 [https://web-production-7fb8d2.up.railway.app/docs](https://web-production-7fb8d2.up.railway.app/docs)

Repositório da API: [github.com/Renanmrqs/Gym-Api](https://github.com/Renanmrqs/Gym-Api)

---

## Próximos passos

- Sistema de logout
- Refresh token automático
- Gráficos de evolução de carga por exercício
- Landpage na tela inicial apresentando o app
