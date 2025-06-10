# Langchain FAISS QA

Este projeto utiliza Langchain, FAISS e OpenAI para responder perguntas sobre documentos de texto, com interface interativa no terminal.

## Funcionalidades
- Carregamento de documentos de texto
- Indexação e busca semântica com FAISS
- Geração de respostas usando modelos OpenAI (GPT)
- Loop interativo para múltiplas perguntas

## Pré-requisitos
- Python 3.10+
- Conta e chave de API da OpenAI

## Instalação

1. Clone o repositório:
   ```powershell
   git clone https://github.com/edugitQA/docs_Langchain_FAISS.git
   cd docs_Langchain_FAISS
   ```

2. Crie e ative o ambiente virtual:
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

3. Instale as dependências:
   ```powershell
   pip install -r requirements.txt
   ```

4. Configure sua chave OpenAI:
   - Crie um arquivo `.env` na raiz do projeto com o conteúdo:
     ```env
     OPENAI_API_KEY=sua-chave-aqui
     ```

5. Adicione seu documento de texto em `doc/exemplo.txt`.

## Como usar

Execute o script principal:
```powershell
python main.py
```

Você poderá digitar perguntas sobre o conteúdo do documento. Para encerrar, digite `sair`.

## Estrutura do Projeto
```
├── main.py              # Script principal
├── requirements.txt     # Dependências do projeto
├── .env                 # Chave da OpenAI (NÃO subir para o git)
├── doc/
│   └── exemplo.txt      # Documento de exemplo
└── README.md            # Este arquivo
```

## Observações
- O projeto utiliza as versões mais recentes das bibliotecas Langchain e OpenAI.
- Caso encontre avisos de depreciação, mantenha as dependências atualizadas.
- Não compartilhe sua chave OpenAI publicamente.
- As bibliotecas `pypdf` e `unstructured` estão presentes para possíveis expansões de leitura de PDF e outros formatos, mas não são obrigatórias para o funcionamento básico.

## Licença
Este projeto é open-source e está sob a licença MIT.

