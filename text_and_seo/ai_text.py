from transformers import AutoModelForCausalLM, AutoTokenizer

# Načítanie modelu DistilGPT-2
model_name = "gpt2"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Nastavenie pad_token na eos_token
tokenizer.pad_token = tokenizer.eos_token

# Príklad promptu
prompt = """
How to Start a Small Business at Home? Home-based small business startup
"""


inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True)

output = model.generate(
    inputs.input_ids, 
    attention_mask=inputs.attention_mask,
    max_length=600, 
    min_length=500,
    temperature=0.7, 
    top_p=0.95, 
    do_sample=True,
    repetition_penalty=1.5,
    
    pad_token_id=tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id
)

generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print("Generovaný text:",generated_text)
print("\n")
print("Input IDs:", inputs.input_ids)
print("Attention Mask:", inputs.attention_mask)
""" print("Model Configuration:", model.config) """


