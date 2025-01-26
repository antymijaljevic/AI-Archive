from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import gradio as gr

# Configuration
model_path = "./models"
device = "mps"  # Apple Silicon
dtype = torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16

# Load model with optimizations
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=dtype,
    device_map="auto",
    trust_remote_code=True,
    low_cpu_mem_usage=True
).eval().to(device)

# Generation configuration
generation_config = {
    "max_new_tokens": 512,
    "do_sample": True,
    "top_p": 0.9,
    "temperature": 0.7,
    "repetition_penalty": 1.1,
    "pad_token_id": tokenizer.eos_token_id
}

def respond(message, chat_history):
    # Build conversation history
    messages = []
    for user_msg, bot_msg in chat_history:
        messages.extend([
            {"role": "user", "content": user_msg},
            {"role": "assistant", "content": bot_msg}
        ])
    messages.append({"role": "user", "content": message})
    
    # Tokenize with conversation template
    inputs = tokenizer.apply_chat_template(
        messages,
        return_tensors="pt",
        add_generation_prompt=True
    ).to(device)
    
    # Generate response
    with torch.no_grad():
        outputs = model.generate(
            inputs,
            **generation_config
        )
    
    # Decode and return response
    response = tokenizer.decode(
        outputs[0][inputs.shape[1]:], 
        skip_special_tokens=True
    )
    
    # Update chat history
    chat_history.append((message, response))
    return "", chat_history

# Create Gradio chat interface
with gr.Blocks() as demo:
    gr.Markdown("# DeepSeek Chat (M2 Optimized)")
    gr.Markdown("Interactive conversation with DeepSeek-7B")
    
    chatbot = gr.Chatbot(height=500)
    msg = gr.Textbox(
        placeholder="Ask me anything...",
        container=False,
        scale=7
    )
    clear = gr.Button("Clear")

    # Submit action
    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    
    # Clear action
    clear.click(lambda: None, None, chatbot, queue=False)

# Launch the app
demo.launch(server_port=7860, share=False)