# About

Evaluates LLM applications by using [promptfoo](https://www.promptfoo.dev/docs/intro/)

# Setup

1.- Setup Python 3.9 venv & install dependencies
```
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2.- Install promptfoo

Refer to the official [installation page](https://www.promptfoo.dev/docs/installation/)

# Evaluation examples

## Granite Model Family

Example: Refer to the `IBM Granite model family` [example evaluation](./granite-family-eval.yaml) and [results](./granite-family-eval-results.png).

Run evaluation:

```
export PROMPTFOO_CONFIG_DIR=./.promptfoo
export GRANITE_3_0_API_TOKEN=<YOUR_API_TOKEN>
export GRANITE_3_1_API_TOKEN=<YOUR_API_TOKEN>
export HF_API_TOKEN=<YOUR_API_TOKEN>

# Run evaluations.
npx promptfoo@latest eval -c granite-family-eval.yaml -o granite-family-eval-out.json

# View results.
npx promptfoo@latest view $PROMPTFOO_CONFIG_DIR -y -p 8080
```

## Ansible Chatbot (stage)

Example: Refer to the `Ansible Chatbot (stage)` links: 
* [example evaluation](./ansible-chatbot-eval.yaml)
* [example dataset and assertions](https://docs.google.com/spreadsheets/d/1G0d4-O8yEH4Mj1_6eUQ7C1ULwtZF4IqBL4fVas06wJM/edit?usp=sharing)
* [GHA actions](https://github.com/romartin/llm-apps-eval/actions)
* [GHA result example](./ansible-chatbot-eval-results.txt).

Run evaluation:

```
export PROMPTFOO_CONFIG_DIR=./.promptfoo
export CHATBOT_STAGE_TOKEN=<YOUR_API_TOKEN>
export HF_API_TOKEN=<YOUR_API_TOKEN>

# Run evaluations.
npx promptfoo@latest eval -c ansible-chatbot-eval.yaml -o ansible-chatbot-eval-out.json

# View results.
npx promptfoo@latest view $PROMPTFOO_CONFIG_DIR -y -p 8080
```

# GitHub Actions

Automated GHA can be integrated easily to evaluate and provide CD/CI integration.

Examples
* Evaluate Ansible Chatbot (stage) [workflow](./.github/workflows/granite-family-eval-workflow.yaml)
* Evaluate Granite Model Family [workflow](./.github/workflows/ansible-chatbot-eval-workflow.yaml)
* [Runs](https://github.com/romartin/llm-apps-eval/actions)

### TODO:
* Tests/Assertions
  * Perplexity
  * Model-graded
  * Factuality
  * Context (Referenced Docs/History)
* LLM
  * Support for other parameters
  * Support for chat & history (prompt)
* Response
  * Error handling
  * Handle other LLM response attributes (content, metadata, etc)
  * Handle other promptfoo response type's attributes (tokens, etc)
* Integrations
  * [LLM red teaming](https://www.promptfoo.dev/docs/red-team/)
* RAG
  * Ingestion (as promptfoo extension)
  * Relevant docs (prompt)
  * Retrieval
  * Multiple vectorDB's
* ChatBot E2E 

### TODO Lightspeed:
* Chatbot
  * Compare models/RAG/pipelines
    * with Tami's results: https://redhat-internal.slack.com/archives/C07L4FBTGLE/p1737151718432599?thread_ts=1737137842.074019&cid=C07L4FBTGLEç
      * LLM-rubric
    * with Sumit's results (OLS): https://docs.google.com/spreadsheets/d/1KpxaQyxkLzyuDdnI-oIqSUdPJeoQAOphWaSIjM8CbkU/edit?gid=1422959476#gid=1422959476
      * compare similar Qs as for the ground truth answer 
* Custom LLM provider -> Use same granite models as for similarity and other providers for testing assertions
* Separate comparison, per each user's query, per step in the pipeline
  * LLM
  * RAG
  * CHATBOT
