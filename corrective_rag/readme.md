# CORRECTIVE RAG 

## Overview

1. Employ a lightweight **retrieval evaluator** to assess the overall quality of retrieved documents for a query, returning a confidence score for each.
2. Perform **web-based document retrieval to supplement context** if vectorstore retrieval is deemed ambiguous or irrelevant to the user query.
3. Perform **knowledge refinement** of retrieved document by partitioning them into "knowledge strips", grading each strip, and filtering our irrelevant ones.