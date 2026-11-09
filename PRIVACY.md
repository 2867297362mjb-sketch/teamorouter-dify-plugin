# Privacy Policy

This plugin sends the configured TeamoRouter API key, the model ID, prompts, conversation messages, tool definitions, and request parameters directly to `https://api.teamorouter.com/v1`. Generated content, usage metadata, request IDs, and errors are returned to Dify. Each request also carries an `X-Client-Source: dify-teamorouter` header that identifies the plugin.

The plugin itself does not collect analytics or telemetry and does not store anything. Dify stores the API key using its normal plugin credential handling, and the key is sent only to TeamoRouter as bearer authentication.

TeamoRouter processes request content, usage data, and request metadata such as IP addresses to provide and secure the service and to account for usage. It forwards model requests to the relevant upstream model provider, whose terms and privacy policies also apply to that processing.

For TeamoRouter's current terms and privacy policy, see https://teamorouter.com.
