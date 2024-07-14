# KNOWLEDGE GRAPH 
- [1. Limitations of traditional RAG](#Limitations-of-traditional-RAG)
- [2. Overview of Knowledge Graph](#Overview-of-Knowledge-Graph)
- [3. Knowledge graph solutions](#Knowledge-graph-solutions)
- [4. GraphRAG](#GraphRAG)
    - [Indexing Phase](#Indexing-Phase)
    - [Query Phase](#Query-Phase)

# Limitations of traditional RAG
The main limitation of traditional RAG system is, it will not be able to take the questions which are spanning the complete document. But most of the  times user will have the questions realted to complete document to get the questions understood and answered intentionally rather than the direct question.

# Overview of Knowledge Graph
Knowledge graph on the other hand will summarize the information and create the multi layered structure. It will extract the entities and create the nodes. 

# Knowledge graph solutions 
Currently knowledge graph solution is provided by 3 approaches 
1. [Graphrag from Microsoft](https://www.microsoft.com/en-us/research/project/graphrag/)
2. [LlamaIndex Graph rag](https://docs.llamaindex.ai/en/stable/examples/query_engine/knowledge_graph_rag_query_engine/)
3. [Neo4j graph rag](https://neo4j.com/developer-blog/graphrag-llm-knowledge-graph-builder/)

# [GraphRAG from Microsoft](https://www.microsoft.com/en-us/research/project/graphrag/)

Overview and details of the Graph Rag are explained in below section. Graph RAG is split into 2 parts 
1. Indexing Phase
2. Query Phase

Complete details of Grap RAG and Git hub [link](https://microsoft.github.io/graphrag/). 


## [Indexing Phase](https://github.com/viswanath27/rag/blob/main/kg_rag/docs/md_files/indexing.md)
Indexing phase is approach of how input data indexing will happen in Graph RAG. More details are given in this link [Index details](https://github.com/viswanath27/rag/blob/main/kg_rag/docs/md_files/graphrag.md)

## [Query Phase](https://github.com/viswanath27/rag/blob/main/kg_rag/docs/md_files/query.md)
Query phase is approach of how the query will be executed in Graph RAG. More details are given [Querying Phase](https://github.com/viswanath27/rag/blob/main/kg_rag/docs/md_files/query.md)


## Query to run 

Global query 
`python -m graphrag.query --root ./ragtest --method global "What are the top themes in this story?"`

Local query 
`python -m graphrag.query --root ./ragtest --method local "Who is Scrooge, and what are his main relationships?`

## Cost 

# LlamaIndex Graph rag



# Neo4j graph rag