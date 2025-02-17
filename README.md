# 📌 Brasileirão 2025 - Tabelas da Série A e Série B

Este repositório contém arquivos JSON com a estrutura das tabelas do Campeonato Brasileiro de Futebol de 2025, incluindo times da **Série A** e **Série B**.

## 📂 Estrutura do Projeto

O projeto está organizado em dois arquivos JSON:

- `times_serie_a_2025.json` → Contém a lista de times da Série A
- `times_serie_b_2025.json` → Contém a lista de times da Série B

Cada arquivo possui uma estrutura padronizada para armazenar as estatísticas dos times ao longo da competição.

## 📜 Estrutura dos Arquivos JSON

Cada time segue o formato:

```json
{
  "times": {
    "SIGLA": {
      "nome": "Nome do Time",
      "vitorias": 0,
      "empates": 0,
      "derrotas": 0,
      "pontos": 0
    }
  }
}
```

### 🏆 Exemplo de Time:

```json
"FLA": {
  "nome": "Flamengo",
  "vitorias": 0,
  "empates": 0,
  "derrotas": 0,
  "pontos": 0
}
```

## 🚀 Como Usar

1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/brasileirao-2025.git
   ```
2. Acesse o diretório do projeto:
   ```sh
   cd brasileirao-2025
   ```
3. Utilize os arquivos JSON conforme necessário para análise ou integração com sistemas esportivos.

## 🖥️ Aplicação em Python

Este repositório inclui um programa em Python que gerencia a classificação do campeonato utilizando Firebase e PyQt5.

### 📜 Dependências

Instale as dependências necessárias com:
```sh
pip install firebase-admin PyQt5
```

### 🚀 Executando o Programa

1. Certifique-se de que possui um arquivo JSON com as credenciais do Firebase.
2. Atualize o caminho do arquivo no código.
3. Execute o programa

O programa permite exibir a classificação, atualizar pontuações, adicionar e remover equipes em uma interface gráfica.

---
📢 *Contribuições são bem-vindas! Caso tenha sugestões ou queira colaborar, sinta-se à vontade para abrir um Pull Request.*

