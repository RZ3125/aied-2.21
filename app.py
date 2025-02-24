import chainlit as cl
from langflow.load import run_flow_from_json

TWEAKS = {
  "ChatInput-EzMe3": {},
  "Prompt-1wotK": {},
  "GroqModel-TLrpf": {"api_key": "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"},
  "ChatOutput-paMYV": {}
}

@cl.on_message
async def main(message: cl.Message):
    result = run_flow_from_json(flow="Langflow AIED 2.21.json",
                            input_value=message.content,
                            session_id="1234", # provide a session id if you want to use session state
                            fallback_to_env_vars=True, # False by default
                            tweaks=TWEAKS)
    await cl.Message(result[0].outputs[0].results["message"].text).send()