from __future__ import annotations

import torch
from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('google/gemma-2-2b-it')
model = AutoModelForCausalLM.from_pretrained(
    'google/gemma-2-2b-it',
    device_map='auto',
    torch_dtype=torch.bfloat16,
)

model.save_pretrained('models/gemma-2-2b-it')
tokenizer.save_pretrained('models/gemma-2-2b-it')
