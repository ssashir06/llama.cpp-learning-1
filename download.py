import sys
from huggingface_hub import snapshot_download, hf_hub_download
model_id=sys.argv[1]  #"lmsys/vicuna-13b-v1.5"
local_dir=sys.argv[2] #"models/vicuna-hf"
filename=sys.argv[3] if len(sys.argv)>3 else None #"ELYZA-japanese-Llama-2-7b-fast-instruct-q2_K.gguf"

if filename:
    hf_hub_download(repo_id=model_id, filename=filename,
        local_dir=local_dir)
else:
    snapshot_download(repo_id=model_id, local_dir=local_dir,
                  local_dir_use_symlinks=False, revision="main")
