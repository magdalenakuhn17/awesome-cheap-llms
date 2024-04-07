<div align="center">
  <h1>awesome-cheap-llms</h1>
  <p align="center">
    :yellow_heart: <a href="https://www.linkedin.com/posts/magdalenakuhn_costs-of-rag-explained-activity-7181168603906359296-fHEW?utm_source=share&utm_medium=member_desktop">Costs of RAG based applications</a> <br>
    :blue_heart: <a href="https://www.linkedin.com/in/joannastoffregen/">Follow Joanna on LinkedIn</a> :heavy_plus_sign: <a href="https://www.linkedin.com/in/magdalenakuhn/">Follow Magdalena on LinkedIn</a> <br>
    :white_heart: <a href="https://github.com/DataTalksClub/llm-zoomcamp">Sign up to DataTalksClub LLM Zoomcamp</a> <br>
    :star: Give this repository a star to support the initiative! 
  </p>
</div>
<br/>
<p align="center">
  <img src="images/Screenshot%202024-04-04%20at%2007.41.00.png" alt="Alt text" title="Expectation vs. Reality"> <br>
</p>


:point_right: Let’s make sure that your LLM application doesn’t burn a hole in your pocket. <br>
:point_right: Let’s instead make sure your LLM application generates a positive ROI for you, your company and your users. <br>
:point_right: A nice side effect of choosing cheaper models over expensive models: the response time is shorter!

# Techniques to reduce costs

<p align="center">
  <img src="images/overview.png" alt="Alt text" title="Overview"> <br>
</p>

## 1) :blue_book: Choose model family and type 
Selecting a suitable model or combination of models based on factors, such as speciality, size and benchmark results, builds the foundation for developing cost-sensible LLM applications.

### Papers 
* Naveed, Humza, et al. ["A comprehensive overview of large language models."](https://arxiv.org/abs/2307.06435?utm) arXiv preprint arXiv:2307.06435 (2023).
* Minaee, Shervin, et al. ["Large Language Models: A Survey."](https://arxiv.org/abs/2402.06196) arXiv preprint arXiv:2402.06196 (2024).
### Tools & frameworks
* [MTEB (Massive Text Embedding Benchmark) Leaderboard](https://huggingface.co/spaces/mteb/leaderboard) by Huggingface
* [Models](https://huggingface.co/models) by Huggingface
### Blog posts & courses
* [Which LLM to choose for your use case?](https://ubiops.com/which-llm-to-choose-for-your-use-case/#:~:text=While%20choosing%20an%20LLM%20that,procedures%20and%20biases%2C%20and%20licensing.)
* [6x Key factors to consider in choosing an LLM](https://www.solitontech.com/key-factors-to-consider-in-llm/)

## 2) :blue_book: Reducing model size 
After chosing the suitable model family, you should consider models with fewer parameters and other techniques that reduce model size.
* Model parameter size (i.e. 7B, 13B ... 175B)
* Quantization of models
* Higher degree of model customization (i.e. through RAG or fine-tuning) can achieve the same performance as a bigger model
* Distillation 

### Papers 
* :speaking_head: call-for-contributions :speaking_head:

### Tools & frameworks
* [LoRA](https://huggingface.co/docs/diffusers/training/lora#lora) and [QLoRA](https://medium.com/@dillipprasad60/qlora-explained-a-deep-dive-into-parametric-efficient-fine-tuning-in-large-language-models-llms-c1a4794b1766) make training large models more efficient
* :speaking_head: call-for-contributions :speaking_head:

### Blog posts & courses
* [Basics of quantization in ML](https://iq.opengenus.org/basics-of-quantization-in-ml/)
* [How LLM quantization impacts model quality](https://deci.ai/blog/how-llm-quantization-impacts-model-quality/#:~:text=LLM%20Quantization%20Methods,-Quantization%20reduces%20the&text=Common%20quantization%20approaches%20include%20Bitsnbytes,and%20potentially%20speeding%20up%20computation.)
* [mlabonne/llm-course#quantization](https://github.com/mlabonne/llm-course?tab=readme-ov-file#7-quantization)
## 3) :blue_book: Use open source models
Consider self-hosting models instead of using proprietary models if you have capable developers in house. Still, have an oversight of Total Cost of Ownership, when benchmarking managed LLMs vs. setting up everything on your own. 

### Papers  
* :speaking_head: call-for-contributions :speaking_head: 
### Tools & frameworks
* [LocalAI](https://github.com/mudler/LocalAI)
* [Ollama ](https://github.com/ollama/ollama)
* [vLLM](https://github.com/vllm-project/vllm)
* [llama.cpp](https://github.com/ggerganov/llama.cpp)
### Blog posts & courses
* [5x easy ways to run an llm locally](https://www.infoworld.com/article/3705035/5-easy-ways-to-run-an-llm-locally.html)
* [mlabonne/llm-course#deploying-llms](https://github.com/mlabonne/llm-course?tab=readme-ov-file#6-deploying-llms)
## 4) :blue_book: Reduce input/output tokens
A key cost driver is the amount of input tokens (user prompt + context) and output tokens, that you allow for your LLM. Different techniques to reduce the amount of tokens help in saving costs.
* Chunking of input documents
* Compression of input tokens
* Summarization of input tokens
* Prompting to instruct the LLM how many output tokens are desired

### Papers  
* :speaking_head: call-for-contributions :speaking_head: 
### Tools & frameworks 
* [LLMLingua](https://github.com/microsoft/LLMLingua) by Microsoft to compress input prompts
* :speaking_head: call-for-contributions :speaking_head: 
### Blog posts & courses
* :speaking_head: call-for-contributions :speaking_head: 
## 5) :blue_book: Prompt and model routing 
Send your incoming user prompts to a model router (= Python logic + SLM) to automatically choose a suitable model for actually answering the question. Follow Least-Model-Principle, which means to by default use the simplest possible logic or LM to answer a users question and only route to more complex LMs if necessary (aka. "LLM Cascading"). 

### Tools & frameworks
* [LLamaIndex Routers and LLMSingleSelector](https://docs.llamaindex.ai/en/latest/module_guides/querying/router/#using-selector-as-a-standalone-module) to select the best fitting model from a range of potential models
* [Nemo guardrails](https://github.com/NVIDIA/NeMo-Guardrails) to detect and route based on intent 
### Blog posts & courses
* [Dynamically route logic based on input
](https://python.langchain.com/docs/expression_language/how_to/routing/) with LangChain, prompting and output parsing
## 6) :blue_book: Caching 
If your users tend to send semantically similar or repetitive prompts to your LLM system, you can reduce costs by using different caching techniques. The key lies in developing a caching strategy, that does not only look for exact matches, but rather semantic overlap to have a decent cache hit ratio.
* :speaking_head: call-for-contributions :speaking_head: 
### Tools & frameworks 
* [GPTCache](https://github.com/zilliztech/GPTCache) for semantic caching 
### Blog posts & courses
* :speaking_head: call-for-contributions :speaking_head: 
## 7) :blue_book: Rate limiting 
Make sure one single customer is not able to penetrate your LLM and skyrocket your bill. Track amount of prompts per month per user and either hard limit to max amount of prompts or reduce response time when a user is hitting the limit. In addition, detect unnatural/sudden spikes in user requests (similar to DDOS attacks, users/competitors can harm your business by sending tons of requests to your model).
### Tools & frameworks 
* Simple tracking and rate limiting logic can be implemented in native Python 
* :speaking_head: call-for-contributions :speaking_head: 
### Blog posts & courses 
* [How to design a scalable rate limiting algorithm](https://konghq.com/blog/engineering/how-to-design-a-scalable-rate-limiting-algorithm) 
## 8) :blue_book: Cost tracking  
"You can't improve what you don't measure" --> Make sure to know where your costs are coming from. Is it super active users? Is it a premium model? etc.
### Tools & frameworks 
* Simple tracking and cost attribution logic can be implemented in native Python 
* :speaking_head: call-for-contributions :speaking_head: 
### Blog posts & courses
* :speaking_head: call-for-contributions :speaking_head: 
## 9) :blue_book: During development time 
* Make sure to not send endless API calls to your LLM during development and manual testing.
* Make sure to not send automated API calls to your LLM via automated CICD workflows, integration tests etc. 

# Contributions welcome 
* We’re happy to review and accept your Pull Request on LLM cost reduction techniques and tools. 
* We plan to divide the content into subpages to further structure all chapters.
<br><br>
