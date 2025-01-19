# About

Evaluates LLM applications by using [promptfoo](https://www.promptfoo.dev/docs/intro/)

See the `IBM Granite model family` [example evaluation](./granite-family-eval.yaml) and [results](./example_granite_3_eval.png).

# Usage

1.- Setup Python 3.9 venv & install dependencies
```
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2.- Install promptfoo

Refer to the official [installation page](https://www.promptfoo.dev/docs/installation/)


3.- Run evaluations:

For Granite Model Family:

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

### TODO:
* Tests/Assertions
  * Perplexity
  * Model-graded
* LLM
  * Support for other parameters
  * Support for chat & history (prompt)
* Response
  * Error handling
  * Handle other LLM response attributes (content, metadata, etc)
  * Handle other promptfoo response type's attributes (tokens, etc)
* RAG
  * Ingestion (as promptfoo extension)
  * Relevant docs (prompt)
  * Retrieval
  * Multiple vectorDB's