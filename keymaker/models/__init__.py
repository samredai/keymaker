from .openai import OpenAIChat, OpenAICompletion

def chatgpt(completion: bool = False, *args, **kwargs):
    if completion:
        return OpenAICompletion(model_name="gpt-3.5-turbo", max_total_tokens = 4096, *args, **kwargs)
    return OpenAIChat(model_name="gpt-3.5-turbo", max_total_tokens = 4096, *args, **kwargs)

def gpt4(*args, **kwargs):
    return OpenAIChat(model_name="gpt-4", max_total_tokens = 8192, *args, **kwargs)