# MAL-BUD

### STEP 1. make .env file
```
GROQ_API_KEY=<YOUR API KEY>
SK_OPEN_API_KEY=<YOUR API KEY>
```
You can manage your API keys here: https://console.groq.com/playground , https://openapi.sk.com/mypage/dashboard

### STEP 2-0. install tkinter (if needed)
```shell
python3 -m tkinter
```
if nothing pops up with above command, then install tkinter
```shell
brew install tcl-tk
echo 'export PATH="/usr/local/opt/tcl-tk/bin:$PATH"' >> ~/.zshrc
echo 'export LDFLAGS="-L/usr/local/opt/tcl-tk/lib"' >> ~/.zshrc
echo 'export CPPFLAGS="-I/usr/local/opt/tcl-tk/include"' >> ~/.zshrc
source ~/.zshrc
```

### STEP 2-1. install dependencies
```
python3.12 -m venv .venv
source .venv/bin/activate # or .venv\Scripts\activate
pip install -r requirements.txt
```

### STEP 2-2 . reinstall pytorch (if needed)
```shell
# CUDA is not available on MacOS, please use default package
pip3 install torch torchvision torchaudio
```

### STEP 2-3. download pretrained model (if needed)
```shell
chmod +x download_models.sh
./download_models.sh
```
download model from hugging-face


### STEP 3. run LLM - TTS
```shell
python llm_tts.py
```
