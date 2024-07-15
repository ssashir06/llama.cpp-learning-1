import sys
from llama_cpp import Llama

model_path = sys.argv[1]
prompt = sys.argv[2]

llm = Llama(
      model_path=model_path,
      n_gpu_layers=-1, # Uncomment to use GPU acceleration
)
output = llm(
      prompt, # Prompt
      max_tokens=None, # Generate up to 32 tokens, set to None to generate up to the end of the context window
) # Generate a completion, can also call create_completion

print(f'Model: {model_path}')
print(f'Prompt: {prompt}')
print(f'Response: {output['choices'][0]['text']}')
print(f'Output: {output}')
