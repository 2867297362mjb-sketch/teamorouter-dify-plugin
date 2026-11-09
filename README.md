# TeamoRouter for Dify

[TeamoRouter](https://teamorouter.com) is a model gateway with one API key for Claude, GPT, Gemini, DeepSeek, GLM, Kimi, and Qwen models. This plugin connects Dify to TeamoRouter's OpenAI-compatible Chat Completions API at `https://api.teamorouter.com/v1`.

> Maintained by TeamoRouter. Source: https://github.com/2867297362mjb-sketch/teamorouter-dify-plugin

## Setup

1. Create an API key in the [TeamoRouter dashboard](https://teamorouter.com/dashboard).
2. Install this plugin in Dify.
3. Open **Settings > Model Provider > TeamoRouter**.
4. Paste the key and save. The plugin validates it with `GET https://api.teamorouter.com/v1/models`. That call needs a valid key and is not billed.

## Included models

- `claude-sonnet-5-5`, `claude-opus-5-5`, `claude-haiku-5-5`
- `gpt-5.5`
- `gemini-3.8-flash`
- `deepseek-v4-pro`, `deepseek-v4-flash`
- `glm-5.3`
- `kimi-k3`
- `qwen3.8-max`

These are convenience entries, not the full catalog. To use another model, add it through the customizable model option with the exact model ID from [teamorouter.com/models](https://teamorouter.com/models). The token prices in the model entries are the model vendors' list prices.

## Usage

Select TeamoRouter and a model in an LLM, Agent, Chatflow, or Workflow node. Streaming and tool calling are enabled by default. Image input is enabled for the Claude, GPT, and Gemini entries.

## Connection requirements

- Outbound HTTPS to `api.teamorouter.com`.
- Every request carries an `X-Client-Source: dify-teamorouter` header, so TeamoRouter can tell which traffic comes from this plugin.

## Privacy

See [PRIVACY.md](PRIVACY.md).
