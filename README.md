# Smart Product Search Assistant 🛍️

An intelligent product search system with natural language processing capabilities that provides detailed product information, price comparisons, and policy insights across multiple e-commerce platforms.

## Table of Contents
- [Tests](#tests)
- [Comparative Conceptual Map](#comparative-conceptual-map)
- [Short Written Analysis](#short-written-analysis)
- [Design Decisions](#design-decisions)
- [Challenges & Improvements](#challenges--improvements)
- [Installation](#installation)

## Tests
1. **Task A: Basic Item Search + Price Constraint**  
   - **Prompt** - Find a floral skirt under 4000 Rupees in size S. Is it in stock, and can I apply a discount code 'SPRING15'?
  
https://github.com/user-attachments/assets/3996b6eb-ea87-46cb-b12d-c1f8d68418e8
     
2. **Task B: Shipping Deadline**  
   - **Prompt** - I need white sneakers (size 8) for under 6000 Rupees that can arrive by Friday.
  
https://github.com/user-attachments/assets/9a2e7b77-4dc7-450d-bef4-4f51daf538db

3. **Task C: Competitor Price Comparison**  
   - **Prompt** - I found a 'casual denim jacket' at 6700 Rupees on SiteA. Any better deals?

https://github.com/user-attachments/assets/e8cb3021-0bfc-4e7d-9849-8cde8154cc2e

4. **Task D: Returns & Policies**  
   - **Prompt** - I want to buy a cocktail dress from SiteB, but only if returns are hassle-free. Do they accept returns?

https://github.com/user-attachments/assets/ac741ad9-c841-4618-bccf-209089e1b65e

5. **Task E: Combine multiple tool usages**  
   - **Prompt** - I want to buy a Sony WH-1000XM4 in Bangalore.  What is the shipping cost?

https://github.com/user-attachments/assets/dab97746-ac2c-4364-a936-21a714f09fc8

To Check more test prompts go to [Prompts.md](https://github.com/mayukhdeep12/smart-product-search/blob/main/Prompts.md)

## Comparative Conceptual Map

![ConMap](https://github.com/user-attachments/assets/f70feab9-209d-4c9c-b023-9ea2b141ebcc)

### Connections
1. **ReAct -> LATS: Smarter Planning**: LATS is built on top of ReAct. It takes ReAct’s simple Think -> Act -> Observe loop and makes it more advanced. Instead of just reacting step by step, LATS explores different possible solutions before choosing the best one. It also adds a new ability: reflection, meaning it looks back at past mistakes and improves its strategy.

2. **ReAct -> AutoToolChain: More Focus on Code**: AutoToolChain (ATC) also follows ReAct’s Think -> Act -> Observe process but uses it in a more structured way. Instead of just making API calls, ATC writes code to automate tool use. It also learns how to create and connect tools, making it more flexible for complex tasks.

3. **Toolformer -> LATS: Smarter Tool Choices**: Toolformer is all about picking the right tools at the right time. LATS takes this idea further—it evaluates different actions (just like how Toolformer picks APIs) and searches for the best possible path forward, similar to a strategy game.

4. **Reflection: The Key Upgrade in LATS**: What really makes LATS special is reflection. While ReAct just moves forward step by step, LATS pauses to analyze what went wrong, learns from it, and adjusts its approach for better results in the future.

![Connection](https://github.com/user-attachments/assets/916cbfca-4c1f-4d46-9d1e-77dd9031581c)

## Short Written Analysis


#### 1. How They Work: The Basic Idea
- **ReAct – Think and Do on the Spot**: ReAct quickly switches between thinking and taking action. It figures out what to do, does it, then looks at the result before deciding the next step.
- **Toolformer – Knows Which Tool to Use**: Toolformer is trained to recognize when and how to use different tools (like APIs) based on its internal knowledge.
- **Automatic Tool Chain (ATC) – Writes Code to Solve Tasks**: ATC follows instructions to generate code, helping it use tools in a structured, step-by-step way.
- **Language Agent Tree Search (LATS)**: LATS thinks ahead, mapping out different possible paths before choosing the best one. It also learns from trial and error.

#### 2. How They Think Through Problems
- **ReAct** follows a simple loop: Think -> Act -> Observe -> Repeat
- **Toolformer** recognizes when an API call is needed and inserts it at the right time.
- **ATC** breaks tasks into small steps and writes code to complete them.
- **LATS** tests multiple strategies, refines them, and improves over time.

#### 3. How They Use Tools
- **ReAct** can call different APIs as needed.
- **Toolformer** only uses APIs it was trained on.
- **ATC** can both use APIs and generate new code when needed.
- **LATS** relies on external data and testing different approaches.

#### 4. Which One is Best?
- **ReAct** is fast and works well with clear prompts and good APIs.
- **Toolformer** is smart about using APIs at the right time.
- **ATC** is great for automating tasks that need code.
- **LATS** is the best choice for tasks that require learning and planning over time.

## Design Decisions

### Agent Architecture

![pako_eNqdV1FP4zgQ_itWVvsGK9pC6fbhTlyB00pw4rbsnXSBB5M4rUVqR46zUAr__SYZO4njlHapkPA4830ez2eP7U0QyZgF02ChaLYkt3_cCQK_z5_JNeWCfBNZocllKp-w_0fO1N8FU-uwbJGqeU8OD38jV1fXN0pGLM-l2oCB30jd94YENX3pYj5yscDuvHjAMODjFV0zFbpepOq8R](https://github.com/user-attachments/assets/4a25f0b2-8f24-4d82-b902-3db43366d96f)

1. **Input Processing Layer**
   - Intent Detection
   - Constraint Extraction (Price, Size, Color, Date)

2. **Tool Selection Process**
   - Tool Categories:
     - Price Comparison Tool
     - Inventory Checker
     - Shipping Calculator
     - Policy Checker

3. **Execution Layer**
   - Data Orchestration

4. **Response Generation**
   - Data Aggregation
   - Natural Language Generation
   - Response Formatting

### Example Query Flow
For query "Find a floral skirt under 4000 Rupees in size S":
```python
tools = select_tools(query_type, constraints)
results = orchestrator.execute_tools(tools, constraints)
```

## Challenges & Improvements

### Challenges
1. **User Intent**
   - Figuring out what the user really wanted was tricky. People don't always type perfect queries. We had to teach the system to recognize whether they were asking about shipping, refunds, searching for something specific, or comparing prices, even with imperfect wording.
2. **LLM Quirks**
   - Plugging in the LLM (the AI brain) was cool, but it wasn't perfect. Sometimes it'd give weird summaries or take too long. Making sure the LLM gave concise, useful info in a reasonable time was a challenge.
  
### Improvements
1. **Intent**
   - We used regular expressions (fancy text pattern matching) to better understand the user's intent. This helped us steer the search in the right direction.
2. **Fuzzy Matching**
   - Instead of just looking for exact matches, we used "fuzzy matching." This means we could find products even if the user's search term was slightly off "airpod pro" instead of "AirPods Pro"
3. **Location**
   - We added code to detect cities and extract date information from the search query, to make sure we gave a relevant result.
4. **AI Recommendations**
   - If no matches found, it generates recommendation based on your prompt.


### Research References

1. [BERT-Based Hybrid RNN Model for Multi-class Text Classification to Study the Effect of Pre-trained Word Embeddings](https://thesai.org/Downloads/Volume13No9/Paper_79-BERT_Based_Hybrid_RNN_Model.pdf)
2. [A Fuzzy Approach to Approximate String Matching for Text Retrieval in NLP](https://www.researchgate.net/publication/333249900_A_Fuzzy_Approach_to_Approximate_String_Matching_for_Text_Retrieval_in_NLP)
3. [A Survey on Knowledge Distillation of Large Language Models](https://arxiv.org/pdf/2402.13116)


## Installation

Follow these steps to set up the Smart Product Search application:

1. Clone the repository:
```bash
git clone https://github.com/mayukhdeep12/Smart_product_search.git
```

2. Navigate to the project directory:
```bash
cd Smart_product_search
```

3. Install Ollama:
- Download from: https://ollama.com/download
- After installation, run Llama3.2 3B model in cmd:
```bash
ollama run llama3.2
```

4. Install Python dependencies:
```bash
pip install -r requirements.txt
```

5. Start the Streamlit application:
```bash
streamlit run agent.py
```
