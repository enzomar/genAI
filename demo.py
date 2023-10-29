from datasets import load_dataset
from transformers import AutoModelForSeq2SeqLM
from transformers import AutoTokenizer
from transformers import GenerationConfig

#huggingface_dataset_name = "knkarthick/dialogsum"

#dataset = load_dataset(huggingface_dataset_name)
#dash_line = '-'.join('' for x in range(100))


def demo():
	print("demo")

	example_indices = [40, 200]


	for i, index in enumerate(example_indices):
	    print(dash_line)
	    print('Example ', i + 1)
	    print(dash_line)
	    print('INPUT DIALOGUE:')
	    print(dataset['test'][index]['dialogue'])
	    print(dash_line)
	    print('BASELINE HUMAN SUMMARY:')
	    print(dataset['test'][index]['summary'])
	    print(dash_line)
	    print()

def summarize():
	print("summarize")

	model_name='google/flan-t5-base'

	model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

	tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)

	example_indices = [40, 200]


	for i, index in enumerate(example_indices):
	    dialogue = dataset['test'][index]['dialogue']
	    summary = dataset['test'][index]['summary']
	    
	    inputs = tokenizer(dialogue, return_tensors='pt')
	    output = tokenizer.decode(
	        model.generate(
	            inputs["input_ids"], 
	            max_new_tokens=50,
	        )[0], 
	        skip_special_tokens=True
	    )
	    
	    print(dash_line)
	    print('Example ', i + 1)
	    print(dash_line)
	    print(f'INPUT PROMPT:\n{dialogue}')
	    print(dash_line)
	    print(f'BASELINE HUMAN SUMMARY:\n{summary}')
	    print(dash_line)
	    print(f'MODEL GENERATION - WITHOUT PROMPT ENGINEERING:\n{output}\n')

def run():
	print("Loading model, please wait...")
	model_name='google/flan-t5-base'
	model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
	tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
	print("Enter something (Ctrl-C to exit):")
	try:
		while True:
			user_input = input("> ")
			inputs = tokenizer(user_input, return_tensors='pt')
			output = tokenizer.decode(
				model.generate(
					inputs["input_ids"], 
					max_new_tokens=50,
				)[0], 
				skip_special_tokens=True
			)
			print(output)

	except KeyboardInterrupt:
		print("\nCtrl-C pressed. Exiting...")

	

run()

	