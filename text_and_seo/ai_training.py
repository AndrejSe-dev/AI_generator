from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from datasets import load_dataset

def main():
    # Načítanie modelu a tokenizeru
    model_name = "gpt2"
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Nastavenie pad_token ako eos_token
    tokenizer.pad_token = tokenizer.eos_token

    # Načítanie dátového súboru
    dataset = load_dataset("text", data_files={"train": "your_dataset.txt"})

    # Tokenizácia dát
    def tokenize_function(examples):
        tokenized_inputs = tokenizer(examples["text"], padding="max_length", truncation=True, max_length=128)
        tokenized_inputs["labels"] = tokenized_inputs["input_ids"]  # Nastavenie labels na input_ids
        return tokenized_inputs

    tokenized_datasets = dataset.map(tokenize_function, batched=True, num_proc=2)

    # Nastavenie tréningových argumentov
    training_args = TrainingArguments(
        output_dir="./results",
        overwrite_output_dir=True,
        num_train_epochs=1,
        per_device_train_batch_size=1,
        save_steps=10_000,
        save_total_limit=1,
        logging_dir='./logs',
        logging_steps=700,
        no_cuda=True  # Zakázať GPU, aby sa trénovalo iba na CPU
    )

    # Nastavenie trénera
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
    )

    # Spustenie tréningu
    trainer.train()
    trainer.save_model("fine_tuned_distilgpt2")
    # Uloženie modelu
    model.save_pretrained("fine_tuned_distilgpt2")
    tokenizer.save_pretrained("fine_tuned_distilgpt2")
    
    print("Hotovo")

if __name__ == '__main__':
    main()
