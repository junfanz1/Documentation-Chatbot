

<!-- TOC --><a name="langchain-documentation-chatot-"></a>
# LangChain Documentation Chatot 🤖

A sophisticated chatbot application that helps users navigate and understand LangChain documentation through an interactive, user-friendly interface.

![image](https://github.com/user-attachments/assets/ea5f488a-1a6f-4dea-8d46-e61284f5c41a)


<!-- TOC --><a name="-table-of-contents"></a>
## 📋 Contents
<!-- TOC start (generated with https://github.com/derlin/bitdowntoc) -->
   * [Purpose](#purpose)
   * [Features](#features)
      + [Input](#input)
      + [Output](#output)
   * [Technology Stack](#technology-stack)
   * [Challenges and Solutions](#challenges-and-solutions)
   * [Business Impact](#business-impact)
   * [Target Audience](#target-audience)
   * [System Analysis](#system-analysis)
      + [Advantages](#advantages)
      + [Disadvantages](#disadvantages)
      + [Tradeoffs](#tradeoffs)
   * [Technical Overview](#technical-overview)
      + [Prerequisites](#prerequisites)
      + [Setup](#setup)
   * [Code Documentation](#code-documentation)
      + [File Structure](#file-structure)
      + [Key Components](#key-components)
         - [1. Document Ingestion (ingestion.py)](#1-document-ingestion-ingestionpy)
         - [2. LLM Integration (core.py)](#2-llm-integration-corepy)
         - [3. User Interface (main.py)](#3-user-interface-mainpy)
      + [Crucial Functions](#crucial-functions)
         - [History-Aware Retrieval](#history-aware-retrieval)
   * [Future Improvements](#future-improvements)
   * [Cursor](#cursor)
   * [License](#license)
   * [Acknowledgments](#acknowledgments)

<!-- TOC end -->

<!-- TOC --><a name="purpose"></a>
## Purpose
This project creates an intelligent documentation assistant that helps developers understand LangChain's extensive documentation through natural language interactions. It combines document retrieval, embedding-based search, and conversational AI to provide accurate, context-aware responses.

<!-- TOC --><a name="features"></a>
## Features
<!-- TOC --><a name="input"></a>
### Input
- Natural language queries about LangChain
- User profile information
- Chat history for context-aware responses

<!-- TOC --><a name="output"></a>
### Output
- Detailed answers from documentation
- Source references for transparency
- Interactive chat interface
- User profile management

<!-- TOC --><a name="technology-stack"></a>
## Technology Stack
- **Frontend**: Streamlit
- **LLM Integration**: LangChain
- **Vector Store**: Pinecone
- **Embeddings**: OpenAI (text-embedding-3-small)
- **LLM**: OpenAI ChatGPT
- **Document Processing**: 
  - RecursiveCharacterTextSplitter
  - ReadTheDocsLoader
  - FireCrawlLoader

<!-- TOC --><a name="challenges-and-solutions"></a>
## Challenges and Solutions
1. **Document Processing**
   - Challenge: Handling large documentation efficiently
   - Solution: Implemented chunk-based processing with overlap

2. **Context Management**
   - Challenge: Maintaining conversation context
   - Solution: Integrated history-aware retriever

3. **Search Accuracy**
   - Challenge: Relevant document retrieval
   - Solution: Vector-based semantic search with Pinecone

<!-- TOC --><a name="business-impact"></a>
## Business Impact
- Reduced documentation navigation time
- Improved developer onboarding
- Enhanced documentation accessibility
- Potential for adaptation to other frameworks

<!-- TOC --><a name="target-audience"></a>
## Target Audience
- LangChain developers
- AI/ML engineers
- Technical documentation teams
- Software development teams

<!-- TOC --><a name="system-analysis"></a>
## System Analysis
<!-- TOC --><a name="advantages"></a>
### Advantages
- Real-time responses
- Source attribution
- Context-aware conversations
- User-friendly interface

<!-- TOC --><a name="disadvantages"></a>
### Disadvantages
- Dependency on external APIs
- Requires internet connectivity
- Initial setup complexity

<!-- TOC --><a name="tradeoffs"></a>
### Tradeoffs
- Accuracy vs. Speed
- Completeness vs. Conciseness
- Flexibility vs. Complexity

<!-- TOC --><a name="technical-overview"></a>
## Technical Overview
<!-- TOC --><a name="prerequisites"></a>
### Prerequisites
- Python 3.8+
- OpenAI API key
- Pinecone API key
- Streamlit
- LangChain packages

<!-- TOC --><a name="setup"></a>
### Setup
1. Clone the repository
```bash
git clone <repository-url>
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Set up environment variables in .env file
```bash
OPENAI_API_KEY=
PINECONE_API_KEY=
LANGCHAIN_API_KEY=
PYTHONRUNPATH=/Users/junfanzhu/Desktop/documentation-helper
PINECONE_ENVIRONMENT_REGION=northamerica-northeast1-gcp
FIRECRAWL_API_KEY=
```
4. Run Application
```bash
streamlit run main.py
```
![image](https://github.com/user-attachments/assets/05561edf-8e35-441c-b358-d3c7d7b4d946)


<!-- TOC --><a name="code-documentation"></a>
## Code Documentation

<!-- TOC --><a name="file-structure"></a>
### File Structure
├── main.py # Streamlit interface
├── ingestion.py # Document processing
└── backend/
└── core.py # LLM integration


<!-- TOC --><a name="key-components"></a>
### Key Components

<!-- TOC --><a name="1-document-ingestion-ingestionpy"></a>
#### 1. Document Ingestion (ingestion.py)

```python
def ingest_docs():
  # Loads and processes documentation
  # Splits into chunks
  # Stores in Pinecone
```


<!-- TOC --><a name="2-llm-integration-corepy"></a>
#### 2. LLM Integration (core.py)

```python
def run_llm():
  # Handles query processing
  # Manages conversation context
  # Returns formatted responses
```

<!-- TOC --><a name="3-user-interface-mainpy"></a>
#### 3. User Interface (main.py)
- Streamlit-based interface
- User profile management
- Chat history display
- Response formatting

<!-- TOC --><a name="crucial-functions"></a>
### Crucial Functions

<!-- TOC --><a name="history-aware-retrieval"></a>
#### History-Aware Retrieval

```python
history_aware_retriever = create_history_aware_retriever(
  llm=chat,
  retriever=docsearch.as_retriever(),
  prompt=rephrase_prompt
)
```

This function maintains conversation context for more accurate responses.

<!-- TOC --><a name="future-improvements"></a>
## Future Improvements
1. Multi-language support
2. Offline mode capability
3. Custom training data integration
4. Enhanced error handling
5. Performance optimization
6. API endpoint creation
7. Extended documentation coverage
8. User authentication
9. Response caching
10. Analytics dashboard

<!-- TOC --><a name="Cursor"></a>
## Cursor
With the polish of Cursor:
![image](https://github.com/user-attachments/assets/9b03160a-451b-42a5-a4e5-b96870312dd1)
![image](https://github.com/user-attachments/assets/6357212a-ff32-4111-b529-4ef8df2e1d31)

README generation prompt:

```bash
According to this project and all the coding files you have, generate a Github Readme for me, including: (1) purpose of the project, (2) input and output, (3) LLM Technology Stack, (4) Challenges and Difficulties, (5) Future Business Impact and Further Improvements, (6) Target Audience and Benefits, (7) Advantages and Disadvantages, (8) Tradeoffs, (9) Highlight and Summary, (10) Future Enhancements, then for the functionality to run my project, provide (11) Prerequisites, (12) Setup, (13) Code Explanation for each file and each function, (14) How it works for the whole project and each class/function, (15) Any function you think is crucial for handling the project make it detailed elaboration, (16) Future Improvements, (17) Anything else you think is important to add in this readme. Finally, generate the readme in markdown format
```

<!-- TOC --><a name="license"></a>
## License
This project is licensed under the MIT License - see the LICENSE file for details.

<!-- TOC --><a name="acknowledgments"></a>
## Acknowledgments

[Eden Marco: LangChain- Develop LLM powered applications with LangChain](https://www.udemy.com/course/langchain/?srsltid=AfmBOooPg0Xkc19q5W1430Dzq6MHGKWqHtq5a1WY4uUl9sQkrh_b_pej&couponCode=ST4MT240225B)









