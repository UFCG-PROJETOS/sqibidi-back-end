# sqibidi-back-end
Entrega as perguntas valida e pontua as respostas do jogo Sqibidi.
## Como rodar o banco de dados:

Estando na raíz do projeto.

Para subir o container:
```bash
docker compose up -d
```

Para fechar o container apagando seu volume de dados
```bash
docker compose down -v
```
## Como rodar a API
### Instalação
- Instale o [UV](https://docs.astral.sh/uv/getting-started/installation/): `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Instale as dependências com `uv sync`

### Rodando
- Modo dev com `uv run fastapi dev`
- Modo produção com `uv run fastapi run`
- Testes com `uv run -m unittest`
