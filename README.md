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

Next:

- Context and prompt construction
- LLM question answering


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
