from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, GenerationConfig

print("Loading model, please wait...")
model_name = 'google/flan-t5-base'
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)


def generate(user_input, max_new_tokens=50, do_sample=True, temperature=0.1, top_k = 50, top_p =1.0):

    generation_config = GenerationConfig(max_new_tokens=max_new_tokens, 
        do_sample=do_sample, 
        temperature=temperature,
        top_k = top_k,
        top_p = top_k)

    inputs = tokenizer(user_input, return_tensors='pt')
    output = tokenizer.decode(
        model.generate(
            inputs["input_ids"], 
            generation_config=generation_config,
        )[0], 
        skip_special_tokens=True
    )
    return output


def run():
    print("Enter something (Ctrl-C to exit):")
    try:
        while True:
            user_input = input("> ")
            output = generate(user_input)
            print(output)

    except KeyboardInterrupt:
        print("\nCtrl-C pressed. Exiting...")


if __name__ == "__main__":
    run()