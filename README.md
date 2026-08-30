# AI-Engineer-Roadmap

My journey from Electrical Engineering student to AI Engineer.

## About Me

I am an undergraduate student majoring in Electrical Engineering.

Currently transitioning into AI Application Development, focusing on:

- Large Language Model Applications
- RAG Systems
- AI Agent Development
- Backend Engineering


## Learning Roadmap

### Python Engineering

Current Progress:

- Python syntax
- Functions
- String processing
- File processing
- Object-oriented programming


### Backend Development

Current Progress:

- Git

Planned:

- FastAPI
- API Development
- Database


### LLM Application Development

Current Progress:

- Embedding
- Vector Database
- RAG retrieval

Planned:

- LLM API Integration
- Prompt Engineering
- RAG generation
- Agent


## Projects


### 1. Text Processing Module

Status:
Completed

Location:
00-Python-Basics/function

Features:

- Character counting
- Word counting
- Text cleaning
- Empty line removal
- Input validation


### 2. Personal Knowledge Base RAG System

Status:
In Progress

Location:
00-Python-Basics

Implemented:

- Document loading
- Text splitting with overlap
- Metadata construction
- BGE text embeddings
- Persistent Chroma vector storage
- Semantic Top K retrieval
- Separate document indexing and database query pipelines
- Context construction from retrieved documents
- Prompt construction with grounded-answer constraints
- DeepSeek LLM API integration
- Environment-based API key management
- End-to-end RAG question answering pipeline
- Prompt-based grounded answering when retrieved context is insufficient 
- Distance-based retrieval relevance filtering
- Early exit when no sufficiently relevant context is retrieved

Next:

- Improved text chunking
- Error handling and configuration cleanup
- Source citation in generated answers
- Basic automated testing


## Tech Stack

Learning:

- Python
- Git
- VS Code
- Conda
- FastAPI
- LLM API
- Vector Database


## Learning Progress


### 2026-08-25

Completed:

- Setup GitHub repository
- Learned Git workflow
- Learned Python functions
- Implemented text cleaning, counting, and empty-line removal
- Added input validation to the text processing module


### 2026-08-26

Completed:

- Built document metadata analysis for filename, lines, characters, and words
- Implemented TXT document loading with missing-file handling
- Built the first end-to-end document processing and text splitting pipeline
- Organized Python modules into reusable packages


### 2026-08-27

Completed:

- Added overlapping text chunks and chunk-level metadata
- Added chunk parameter validation and completed the TXT processing pipeline
- Loaded the BAAI BGE model with SentenceTransformer
- Implemented normalized text embeddings and manual cosine similarity
- Attached 512-dimensional embeddings to document chunks
- Built an in-memory semantic retriever with Top K ranking

Reflection:

- Strengthen understanding of function inputs, outputs, and data flow as the project structure grows
- Keep functions focused and simplify implementations where possible
- Effective learning time: 8-9 hours


### 2026-08-28

Completed:

- Integrated ChromaDB for persistent local vector storage
- Implemented batch upsert with stable document chunk IDs
- Implemented semantic search with BGE query embeddings
- Verified persistent storage and distance-based Top K retrieval
- Separated document indexing from interactive database querying
- Learned Chroma Collection records and nested query result structures


### 2026-08-29

Completed:

- Unified Chroma database paths to `./chroma_db`
- Removed the duplicate local Chroma database and verified indexing and querying
- Implemented context construction from Chroma retrieval results
- Added numbered reference blocks for retrieved documents
- Implemented prompt construction with context, user query, and grounded-answer constraints
- Practiced `enumerate()`, `join()`, and multiline f-strings
- Integrated DeepSeek API using the OpenAI-compatible Python SDK
- Added secure API key loading with `.env` and environment variables
- Added API key validation before creating the LLM client
- Implemented `generate_answer()` for DeepSeek model responses
- Built an end-to-end RAG question answering pipeline
- Connected retrieval, context construction, prompt construction, and LLM generation
- Added optional debug output for inspecting Context and Prompt
- Verified RAG behavior with relevant, cross-domain, and out-of-knowledge-base questions
- Confirmed prompt-based grounded answering when retrieved context does not support the question

Observed:

- Top K retrieval may still return irrelevant chunks when no sufficiently relevant document exists
- Character-based text splitting can break words and reduce context quality
- Retrieval distance should be analyzed before introducing a relevance threshold


### 2026-08-30

Completed:

- Analyzed Chroma retrieval distances using relevant and irrelevant queries
- Compared retrieval distance patterns across RAG, battery, and out-of-knowledge-base questions
- Added `result_filter.py` for retrieval result post-processing
- Implemented distance-based retrieval filtering with an experimental threshold
- Preserved Chroma nested query result structure after filtering
- Integrated retrieval relevance filtering into the end-to-end RAG pipeline
- Added an early return when no sufficiently relevant documents are retrieved
- Avoided unnecessary Context construction, Prompt construction, and LLM API calls for unsupported questions
- Started ACM-style OJ input/output practice
- Practiced `input()`, `split()`, `map()`, `list()`, loops, and conditional checks
- Implemented basic array exercises for summation, min/max, and positive/negative/zero counting
- Implemented a basic string statistics exercise
- Learned basic HTTP Request/Response concepts and connected them to DeepSeek API calls
- Reviewed Client, Server, URL, Header, Body, API, and SDK concepts

Observed:

- The current `0.95` distance threshold is an experimental value based on the current embedding model, knowledge base, and test queries
- A relevance threshold should not be treated as a universal ChromaDB setting
- Character-based text splitting still breaks some words and remains a retrieval quality issue
- Algorithm/OJ practice has now become a fixed daily learning track alongside the AI project