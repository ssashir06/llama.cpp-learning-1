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
$env:CMAKE_ARGS="-DGGML_CUDA=on -DMULTITHREADED_BUILD=6"
pip install `
    --force-reinstall `
    --no-cache-dir `
    llama-cpp-python # Not using any cache to be able to use the CMake options correctly.
mkdir -p models

# Download "lmsys/vicuna-13b-v1.5"
python .\download.py `
    "lmsys/vicuna-13b-v1.5" `
    "models/vicuna-hf"
python .\llama.cpp\convert_hf_to_gguf.py models\vicuna-hf `
    --outfile models/vicuna-13b-v1.5.gguf `
    --outtype q8_0

# Download "mmnga/ELYZA-japanese-Llama-2-7b-fast-instruct-gguf"
python .\download.py `
    "mmnga/ELYZA-japanese-Llama-2-7b-fast-instruct-gguf" `
    "models/mmnga/ELYZA-japanese-Llama-2-7b-fast-instruct-gguf" `
    "ELYZA-japanese-Llama-2-7b-fast-instruct-q2_K.gguf"
```

## Run the CLI command

```shell
# PowerShell
llama-cli -m .\models\vicuna-13b-v1.5.gguf -p "I believe the meaning of life is" -n 128

llama-cli -m .\models\mmnga\ELYZA-japanese-Llama-2-7b-fast-instruct-gguf\ELYZA-japanese-Llama-2-7b-fast-instruct-q2_K.gguf -p "I believe the meaning of life is" -n 128
```

## Run a Python code

```shell

python .\llamacpp-demo-1.py .\models\vicuna-13b-v1.5.gguf "Q: Name the planets in the solar system? A: "

python .\llamacpp-demo-1.py .\models\vicuna-13b-v1.5.gguf "私が思うに、明日は"

python .\llamacpp-demo-1.py .\models\mmnga\ELYZA-japanese-Llama-2-7b-fast-instruct-gguf\ELYZA-japanese-Llama-2-7b-fast-instruct-q2_K.gguf "Q: Name the planets in the solar system? A: "

python .\llamacpp-demo-1.py .\models\mmnga\ELYZA-japanese-Llama-2-7b-fast-instruct-gguf\ELYZA-japanese-Llama-2-7b-fast-instruct-q2_K.gguf "私が思うに、明日は"
```

## References:

- https://github.com/ggerganov/llama.cpp/blob/master/README.md
- https://www.substratus.ai/blog/converting-hf-model-gguf-model/
