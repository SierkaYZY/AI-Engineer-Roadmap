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
- Sentence-aware text chunking
- Sentence-level chunk overlap
- Word-boundary fallback for long sentences

Next:

- Retrieval threshold evaluation and relevance quality testing
- Source citation in generated answers
- Error handling and configuration cleanup
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


### 2026-08-31

Completed:

- Reworked the text splitting pipeline from fixed character slicing to sentence-aware chunking
- Added sentence boundary detection for both Chinese and English text
- Implemented sentence-level chunk grouping with configurable chunk size
- Added sentence-level overlap while preserving complete sentence boundaries
- Added long-sentence fallback that prioritizes word boundaries before character-level splitting
- Integrated the new chunking strategy into the existing RAG document processing pipeline
- Rebuilt the local ChromaDB index using the updated chunking strategy
- Compared retrieval behavior before and after the chunking update using RAG, battery, and out-of-knowledge-base queries
- Confirmed that improved chunk boundaries remove common word-splitting artifacts such as broken `lithium-ion` terms
- Practiced ACM-style duplicate detection using Python `set`
- Learned the basic idea of hashing and why `set` and `dict` support fast average-case lookup
- Practiced frequency counting with Python `dict` and `dict.items()`
- Introduced basic time complexity concepts including O(1), O(n), and O(n²)
- Learned HTTP GET and POST, JSON serialization, Header vs Body, and common HTTP status codes
- Connected HTTP concepts to the existing DeepSeek API integration
- Drafted the first resume-ready description of the RAG project

Observed:

- Better text boundaries do not necessarily make every embedding distance smaller because changing chunk contents changes embedding representations
- The experimental `0.95` retrieval distance threshold is sensitive to chunking strategy and should not be treated as a universal relevance threshold
- A fixed distance threshold alone cannot reliably separate all relevant and irrelevant retrieval results in the current small knowledge base
- Prompt grounding successfully acts as an additional safeguard when irrelevant retrieval results pass the distance filter
- More systematic retrieval evaluation or reranking may be needed in later iterations


### 2026-09-02

Completed:

- Extended RAG context construction to include retrieved document metadata such as filename and chunk ID
- Added numbered source blocks such as `[资料1]` and `[资料2]` to the generated context
- Updated prompt rules to require source citations for factual statements and conclusions
- Verified Source Citation V1 using a knowledge-base question and confirmed that generated answers can reference the supporting retrieved source
- Reviewed Python `sort()` and `sorted()` and their use in ranking and retrieval workflows
- Implemented standard binary search with `left`, `right`, and `mid` boundary control
- Implemented a lower-bound binary search to find the first position whose value is greater than or equal to the target
- Learned Domain, DNS, IP address, Port, localhost, and `127.0.0.1`
- Connected HTTP networking concepts to the existing DeepSeek API integration
- Learned the role of FastAPI in exposing Python application logic as HTTP APIs
- Practiced explaining the RAG project architecture, retrieval flow, technical choices, optimization decisions, and current limitations in an interview-oriented format

Observed:

- Source citations improve answer traceability and verifiability but do not by themselves guarantee answer correctness
- Top-K retrieval provides relative ranking rather than an absolute guarantee of relevance
- Distance filtering, Guard Clauses, Prompt Grounding, and Source Citation solve different reliability problems in the RAG pipeline
- A fixed retrieval distance threshold remains sensitive to the embedding model, chunking strategy, corpus, and query distribution
- Retrieval quality should eventually be evaluated with a labeled retrieval evaluation set rather than only manually tuning thresholds
- FastAPI is the next major engineering step for turning the current local RAG pipeline into an externally callable AI backend service