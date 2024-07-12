





<p align="right">
  <a href="https://github.com/viswanath27/rag/blob/main/kg_rag/docs/md_files/main.md">
    <img src="https://github.com/viswanath27/rag/blob/main/kg_rag/docs/images/cho_icon.png" alt="home" style="width:5%;">
  </a>
</p>

# Indexing in GraphRAG
- [1. Overview](#Overview)
- [2. Architecture](#Architecture)
- [3. Indexing Phase](#Indexing-Phase)
    - [1. Source documents](#Source-documents)
    - [2. Text Chunking](#Text-Chunking)
    - [3. Entity Extraction](#Entity-Extraction)
    - [4. Relationship Extraction](#Relationship-Extraction)
    - [5. Knowledge Graph Generation](#Knowledge-Graph-Generation)
    - [6. Community Detection](#Community-Detection)
    - [7. Heirarchial Community Structure](#Heirarchial-Community-Structure)
    - [8. Community Levels](#Community-Levels)
    - [9. Generate Community Services](#Generate-Community-Services)




## Overview
Overview and details of the Graph Rag are explained in below section. There are 2 main phases for this operation.
* Indexing Phase
* Quering Phase 

## Architecture
Graph Rag architecure is shown below 

![GraphRagArchitecture](https://github.com/viswanath27/rag/blob/main/kg_rag/docs/images/kg_arch.png)

## Indexing Phase
Indexing phase is used to create the index for the given text. This index is used to query

### Source documents
----
All the soruce documents are processed and organized in this stage. This is more of understanding the format and accordingly process the documents to extract the data.

### Text Chunking 
---
This is the chunking strategy which is used to chunk the documents. This is completly dependent upon the how is our document organized and what is the best approach to do so.

### Entity Extraction
---
Within each chunk, we need to identify the entities. These entities can be people, places, dates and other important artifacts which are necessary for processing the document. 

### Relationship Extraction
---
Relationship extraction will mainly look for the relation ships between these entities. Above both steps should be performed in an best way to get the great results.

### Knowledge Graph Generation
---
This is the stage where we are creating the knowledge graph using the above 2 important steps, Entity extraction and Relationship extraction. 

### Community Detection
---
This more of idetifying the communities which are more related. 

### Heirarchial Community Structure 
---
There will be heirarchial communities which are established and these communities provide the relation between the informaiton 


### Community Levels
---
* Root Level C0
* High Level C1 
* Low Level C3 

### Generate Community Services
--- 