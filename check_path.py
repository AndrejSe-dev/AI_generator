import os

# Skontrolujte, či priečinok existuje
model_dir = "fine_tuned_distilgpt2"
if os.path.exists(model_dir):
    print(f"Model uložený v priečinku: {os.path.abspath(model_dir)}")
else:
    print("Priečinok s modelom neexistuje.")
