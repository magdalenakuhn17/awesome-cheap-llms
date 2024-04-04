<div align="center">
  <h1>awesome-cheap-llms</h1>
  <p align="center">
    :yellow_heart: <a href="https://www.canva.com/design/DAGAzJWIcnw/FIWWonF55d9FARA57xT8vg/edit?utm_content=DAGAzJWIcnw&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton">Costs of RAG based applications</a> <br>
    :blue_heart: <a href="https://www.linkedin.com/in/joannastoffregen/">Follow Joanna on LinkedIn</a> :heavy_plus_sign: <a href="https://www.linkedin.com/in/magdalenakuhn/">Follow Magdalena on LinkedIn</a> <br>
    :white_heart: <a href="https://github.com/DataTalksClub/llm-zoomcamp">Sign up to DataTalksClub LLM Zoomcamp</a>  
  </p>
</div>
<br/>
<p align="center">
  Cost reduction tools and techniques for LLM based systems <br> <br>
  <img src="images/Screenshot%202024-04-04%20at%2007.41.00.png" alt="Alt text" title="Expectation vs. Reality">
</p>


:point_right: Let’s make sure that your LLM application doesn’t burn a hole in your pocket. <br>
:point_right: Let’s instead make sure your LLM application generates a positive ROI for you, your company and your users.

# Tools & frameworks to reduce costs

## 1) :blue_book: Model family and type 
Selecting a suitable model or combination of models builds the foundation of building const-sensible LLM applications.

### In-depth papers that explain underlying concepts
* Naveed, Humza, et al. ["A comprehensive overview of large language models."](https://arxiv.org/abs/2307.06435?utm) arXiv preprint arXiv:2307.06435 (2023).
* Minaee, Shervin, et al. ["Large Language Models: A Survey."](https://arxiv.org/abs/2402.06196) arXiv preprint arXiv:2402.06196 (2024).
* :speaking_head: call-for-contributions :speaking_head:
### Tools & frameworks that help with selecting the correct model
* Hugging face open leaderboard
### Hands-on blog posts & courses with step by step guide
* [How to Evaluate, Compare, and Optimize LLM Systems](https://wandb.ai/ayush-thakur/llm-eval-sweep/reports/How-to-Evaluate-Compare-and-Optimize-LLM-Systems--Vmlldzo0NzgyMTQz?utm)
* :speaking_head: call-for-contributions :speaking_head: 

## 2) :blue_book: Model size 
After chosing the suitable model family, you should consider models with fewer parameters and other techniques that reduce model size.
* Selection of model parameter size 
* Quantization of models
* Higher degree of model customization (i.e. through RAG or fine-tuning) can achieve the same performance as a bigger model
* Distillation 

### In-depth papers that explain underlying concepts
* :speaking_head: call-for-contributions :speaking_head:

### Tools & frameworks that help reducing model size 
* [LoRA](https://huggingface.co/docs/diffusers/training/lora#lora) and [QLoRA](https://medium.com/@dillipprasad60/qlora-explained-a-deep-dive-into-parametric-efficient-fine-tuning-in-large-language-models-llms-c1a4794b1766) make training large models more efficient
* :speaking_head: call-for-contributions :speaking_head:

### Hands-on blog posts & courses with step by step guide
* :speaking_head: call-for-contributions :speaking_head: 
## 3) :blue_book: Open source vs. proprietary models
Consider self-hosting models instead of using proprietary models if you have capable developers in house. Still, have an oversight of Total Cost of Ownership, when benchmarking managed LLMs vs. setting up everything on your own. 

### In-depth papers that explain underlying concepts
* :speaking_head: call-for-contributions :speaking_head: 
### Tools & frameworks that help with self-hosting
* Huggingface
* LocalAI
* Ollama 
* vLLM
* :speaking_head: call-for-contributions :speaking_head: 
### Hands-on blog posts & courses with step by step guide
* :speaking_head: call-for-contributions :speaking_head: 
## 4) :blue_book: Input/Output tokens
A key cost driver is the amount of input token (user prompt + context) and output token you allow for your LLM. Different techniques to reduce the amount of tokens help in saving costs.
* Compression
* Summarization

### In-depth papers that explain underlying concepts
* :speaking_head: call-for-contributions :speaking_head: 
### Tools & frameworks that help with reducing tokens
* :speaking_head: call-for-contributions :speaking_head: 
### Hands-on blog posts & courses with step by step guide
* :speaking_head: call-for-contributions :speaking_head: 
## 5) :blue_book: Prompt and model routing 
Add automatic checks to route all incoming user prompts to a suitable model. Follow Least-Model-Principle, which means to by default use the simplest possible logic or LM to answer a users question and only route to more complex LMs if necessary (aka. "LLM Cascading"). This can result to answering certain questions with a predefined response, using SLMs for simple questions and LLMs for complex questions. 

### Tools & frameworks that help with routing
* Native implementation in Python of your custom logic 
* **Nemo guardrails** to detect and Route based on intent 
* :speaking_head: call-for-contributions :speaking_head: 
### Hands-on blog posts & courses with step by step guide
* :speaking_head: call-for-contributions :speaking_head: 
## 6) :blue_book: Caching 
If your users tend to send very similar prompts to your LLM system, you can reduce costs by using different cachin techniques:
* :speaking_head: call-for-contributions :speaking_head: 
### In-depth papers that explain underlying concepts
* :speaking_head: call-for-contributions :speaking_head: 
### Tools & frameworks that help with caching
* :speaking_head: call-for-contributions :speaking_head: 
### Hands-on blog posts & courses with step by step guide
* :speaking_head: call-for-contributions :speaking_head: 
## 7) :blue_book: Rate limiting 
Make sure one single customer is not able to penetrate your LLM and skyrocket your bill. Track amount of prompts per month per user and either hard limit to max amount of prompts or reduce response time when a user is hitting the limit. In addition, detect unnatural/sudden spikes in user requests (similar to DDOS attacks, users/competitors can harm your business by sending tons of requests to your model).
### Tools & frameworks that help with rate limiting:
* Simple tracking logic can be implemented in native Python 
* :speaking_head: call-for-contributions :speaking_head: 
### Hands-on blog posts & courses with step by step guide
* :speaking_head: call-for-contributions :speaking_head: 
## 8) :blue_book: Cost tracking  
"You can't improve what you don't measure" --> Make sure to know where your costs are coming from. Is it super active users? Is it a premium model? etc.
### Tools & frameworks that help with cost tracking
* Simple tracking logic can be implemented in native Python 
* :speaking_head: call-for-contributions :speaking_head: 
### Hands-on blog posts & courses with step by step guide
* :speaking_head: call-for-contributions :speaking_head: 
## 9) :blue_book: During development time 
* Make sure to not send endless API calls to your LLM during development and manual testing.
* Make sure to not send automated API calls to your LLM via automated CICD workflows, integration tests etc. 

# Contributions welcome 
* We’re happy to review and accept your Pull Request on LLM cost reduction techniques and tools. 
* We plan to divide the content into subpages to further structure all chapters.
<br><br>