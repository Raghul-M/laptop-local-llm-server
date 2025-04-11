
# Local LLM Server with Ollama + Cloudflare Tunnel

![Streamlit -app](https://github.com/user-attachments/assets/b28c7fc9-8a98-4414-ad42-4fad5a9bb348)


This project turns an old laptop into a **fully functional AI server** that can serve LLMs locally and access them globally using Cloudflare Tunnel on API . A simple **Streamlit app** provides a friendly frontend to interact with the model via API .

> 🔗 **Blog post:** [Run a Local AI Server for Free with Ollama & Cloudflare Tunnel](https://blog.raghul.in/local-ai-server-for-free-with-ollama-cloudflare-tunnel)



## 🚀 What You Can Build

- Personal chatbot
- Code generation tool
- Lightweight AI backend for your apps
- Home AI server on a budget



## 💻 Requirements

- A Old laptop with Linux  (preferably with 4GB+ RAM)
- Python 3.9+
- Ollama
- Cloudflared



## 🔧 Setup Instructions

### 1. Install Ollama and pull models
```bash
$ curl -fsSL https://ollama.com/install.sh | sh

$ ollama pull tinyllama  # or any other model like deepseek-llm
```

### 2. Serve the model locally
```bash
$ OLLAMA_HOST=0.0.0.0 ollama serve

# Or run on a custom port

$ OLLAMA_HOST=0.0.0.0 OLLAMA_PORT=11435 ollama serve
```

### 3. Expose with Cloudflare Tunnel
```bash
$ wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -O cloudflared

$ chmod +x cloudflared

$ cloudflared --version

$ cloudflared tunnel --url http://localhost:11435
```

This will give you a public URL like:
```
https://your-unique-subdomain.trycloudflare.com
```

### 4. Run the Streamlit App on Client machine 
Install dependencies:
```bash
pip install -r requirements.txt
```

Run app:
```bash
streamlit run app.py
```

> Make sure to update your `app.py` with the correct Cloudflare URL.

![WhatsApp Image 2025-04-11 at 7 46 12 PM (1)](https://github.com/user-attachments/assets/c496b3e1-f9e9-43e9-bcb0-53b69f3fb006)



## Example Request

```bash
curl https://your-unique-subdomain.trycloudflare.com/api/generate -d '{
  "model": "deepseek-llm:1.5b",
  "prompt": "Write a Python function to reverse a string"
}'
```

![WhatsApp Image 2025-04-11 at 7 46 12 PM](https://github.com/user-attachments/assets/03a7ab53-1fa1-42ff-904e-0bcde2b2fdbb)


## 📊 Bonus Tips

- Use `htop` or `glances` to monitor usage
- Check disk with `lsblk` and `df -h`
- Stick to lightweight models for faster inference

![WhatsApp Image 2025-04-11 at 7 46 13 PM (1)](https://github.com/user-attachments/assets/c885e3ed-8408-48f9-a9fb-aab960c9da3b)


## 📁 Project Structure
```
local-ai-server/
├── app.py                # Streamlit frontend
├── requirements.txt      # Python deps
├── README.md             # You are here
```



## 📢 Credits

Built with ❤️ by [Raghul M](https://www.linkedin.com/in/m-raghul/)

Inspired by a simple idea: *"What if I could run AI server without the cloud?"*

