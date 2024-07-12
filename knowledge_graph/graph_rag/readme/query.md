<p align="right">
  <a href="https://github.com/viswanath27/rag/blob/main/kg_rag/docs/md_files/main.md">
    <img src="https://github.com/viswanath27/rag/blob/main/kg_rag/docs/images/cho_icon.png" alt="home" style="width:5%;">
  </a>
</p>

# Quering in GraphRAG
- [1. Overview](#Overview)
- [2. Architecture](#Architecture)
- [3. Query Phase](#Indexing-Phase)
    - [1. User Query](#User-Query)
    - [2. Select Community Level](#Select-Community-Level)
    - [3. Retrieve Relevant Community Service](#Retrieve-Relevant-Community-Service)
    - [4. General Partial Responses](#General-Partial-Responses)
    - [5. Combine Responses](#Combine-Responses)
    - [6. Final Answer](#Final-Answer)

## Overview
Overview and details of the Graph Rag are explained in below section. There are 2 main phases for this operation.
* Indexing Phase
* Quering Phase 

## Architecture
Graph Rag architecure is shown below 

![GraphRagArchitecture](https://github.com/viswanath27/rag/blob/main/kg_rag/docs/images/query_arch.png)


## Query Phase
This below section provides information about the all the stages involved in the query phase. 

### User Query
---
This is the user Query which user wants to know the response about. 

### Select Community Level
---
The first action before we do any thing is choose the community level against which Answer has to be extracted today this is done manually while we are giving the command. But this should be done automatically so that there is a seemless response. 

### Retrieve Relevant Community Service
---
This is where the retrieve the relevant community services based on the question. If there are multiple communities against which this question is matching, that should also be fetched.

### General Partial Responses
---
Based on this communities there will be responses, there can be multiple responses as there are multiple communities. 

### Combine Responses 
---
Once the partial responses are generated these will be combined and augumented to form the answer. 

### Final Answer 
---
Final Answer is generated based on the responses from the above partial answers. 