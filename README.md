# FLISOL-DF-2024: Explorando o Potencial da IA com OLLAMA e LangChain

Este repositório contém os materiais e recursos utilizados na apresentação do FLISOL-DF 2024 sobre como explorar o potencial da Inteligência Artificial com as ferramentas OLLAMA e LangChain.

## Conteúdo

1. **Código Fonte dos Exemplos:**
   Explore e experimente com os códigos para entender na prática como o OLLAMA e o LangChain funcionam.

2. **Instruções de Instalação:**
   Um guia passo a passo para configurar o ambiente necessário para executar os exemplos.

3. **Apresentação:**
   Os slides da apresentação para revisitar os conceitos e acompanhar o conteúdo.

## Instalação Básica

Para executar os exemplos e acompanhar a apresentação, é necessário instalar as seguintes dependências:

- [OLLAMA](https://ollama.com/download)
- [Tesseract-OCR](https://tesseract-ocr.github.io/tessdoc/Installation.html)
- [SQLite3](https://www.sqlite.org/)

Certifique-se de ter o Python e o pip instalados em seu sistema. Em seguida, siga estas etapas:

1. **Clone este repositório:**

   ```bash
   git clone https://github.com/mvdiogo/flisol-df-2024.git
   ```

2. **Navegue até o diretório `./flisol-df-2024/src/`:**

3. **Crie um ambiente virtual:**

   ```bash
   python -m venv venv
   ```

4. **Ative o ambiente virtual (Linux/Mac):**

   ```
   source venv/bin/activate
   ```

   **Ative o ambiente virtual (Windows):**

   ```
   venv\Scripts\activate
   ```

5. **Instale as dependências:**

   ```
   pip install -r requirements.txt
   ```

6. **Instale as LLMs no OLLAMA que você irá usar:**

   ```
   ollama pull llama2
   ollama pull llama3
   ollama pull llava
   ollama pull nomic-embed-text
   ```

7. **Abra o Jupyter Notebook:**

   ```bash
   jupyter notebook
   ```

8. **Acesse o seguinte link no seu navegador:**

   http://localhost:8888

## Próximos Passos

Explore o código fonte dos exemplos e experimente! Os slides da apresentação estarão disponíveis na pasta ./src/files deste repositorio.