# CadAluno — Sistema de Cadastro de Alunos

Projeto final do processo trainee da **ForceTech Jr.**

## O que é

Aplicação desktop em Python com interface gráfica (**Tkinter**) e persistência em **SQLite** para gerenciar cadastros de alunos (CRUD completo).

## Funcionalidades

- Cadastrar aluno (com validações de campos e idade numérica)
- Listar alunos (tabela Treeview + scrollbar)
- Procurar aluno por ID
- Editar dados de um aluno (busca + formulário pré-preenchido)
- Excluir aluno (com confirmação Sim/Não)

## Como executar

```bash
python Main.py
```

O arquivo `MeuBanco.db` será criado automaticamente na primeira execução.

## Estrutura do projeto

```
Main.py              → ponto de entrada
Menu.py              → janela principal com botões
Database.py          → conexão e funções CRUD (SQLite)
Telas/
  ├── Cadastro.py    → formulário de cadastro
  ├── Listar.py      → listagem em Treeview
  ├── Procurar.py    → busca por ID
  ├── Editar.py      → busca + formulário de edição
  └── Excluir.py     → exclusão com confirmação
```

## Tecnologias

- Python 3
- Tkinter (interface gráfica)
- SQLite 3 (arquivo `MeuBanco.db`)

## Estrutura da tabela Alunos

| Campo | Tipo     | Observação                  |
|-------|----------|-----------------------------|
| Id    | INTEGER  | PRIMARY KEY AUTOINCREMENT   |
| Nome  | TEXT     | NOT NULL                    |
| Idade | INTEGER  | —                           |
| Email | TEXT     | UNIQUE                      |

## ForceTech Jr. — Processo Trainee

Documentação completa (todas as etapas) está no arquivo `Documentacao_CadAluno_ForceTech.docx`.
