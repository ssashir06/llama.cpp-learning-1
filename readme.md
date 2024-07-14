# About this document

This repo is a note of using Llama.cpp in Windows 11.

## Prerequisites

- Windows 11
- PowerShell
- CMake
- [CUDA Toolkit 12.x](https://developer.nvidia.com/cuda-toolkit)
- `Desktop development with C++ workload` of Visual Studio 2022

## Build llama.cpp

```shell
# PowerShell
cd llama.cpp
cmake -B build
cmake --build build --config Release
cd ..
$env:PATH= (Get-Item .\llama.cpp\build\bin\Release\).FullName + ';' + $env:PATH
```

## Download a model and convert it

```shell
# PowerShell
python3 -m venv venv
& .\venv\Scripts\activate
pip install `
    -r ./requirements.txt `
    -r ./llama.cpp/requirements.txt
mkdir -p models
python download.py
python .\llama.cpp\convert_hf_to_gguf.py vicuna-hf `
    --outfile models/vicuna-13b-v1.5.gguf `
    --outtype q8_0
```

## Run the CLI command

```shell
# PowerShell
llama-cli -m models/vicuna-13b-v1.5.gguf -p "I believe the meaning of life is" -n 128
```


## References:

- https://github.com/ggerganov/llama.cpp/blob/master/README.md
- https://www.substratus.ai/blog/converting-hf-model-gguf-model/
