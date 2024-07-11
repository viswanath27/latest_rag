# CORRECTIVE RAG 

## Overview

1. Employ a lightweight **retrieval evaluator** to assess the overall quality of retrieved documents for a query, returning a confidence score for each.
2. Perform **web-based document retrieval to supplement context** if vectorstore retrieval is deemed ambiguous or irrelevant to the user query.
3. Perform **knowledge refinement** of retrieved document by partitioning them into "knowledge strips", grading each strip, and filtering our irrelevant ones.

Pictorial view of the corrective rag 
![corrective rag](https://github.com/viswanath27/latest_rag/blob/main/corrective_rag/images/corrective_rag.png)

Paper which is giving the detail of the [Corrective Rag](https://github.com/viswanath27/latest_rag/blob/main/corrective_rag/docs/2401.15884v2.pdf)