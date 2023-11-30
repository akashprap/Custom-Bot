# Finance-Custom-Bot 💼🤖

The Finance-Custom-Bot is a project that harnesses the power of language chains and vector embeddings to find the best similarity score for a given text input. It's particularly adept in the finance sector, significantly enhancing operations through accurate and efficient text matching.

## Key Features 🚀
1. **Open API Key Setup 🔑**:
   - Before getting started, ensure your Open API key is set in the environment variable. This key is crucial for accessing various services and APIs used by the bot.

2. **URL Content Matching 🌐**:
   - Easily find similarity matches of texts within URL content. Add the URLs to the designated section (separated by commas), adjust your search query, and the bot will generate the best matching result from the text.

3. **Embedding Model 🤖**:
   - Utilizes a sentence transformer as the embedding model to create vector embeddings. These embeddings facilitate the discovery of the most similar texts.

4. **FAISS Integration 📚**:
   - Leverages Facebook's FAISS library for efficient storage, retrieval, similarity search, and clustering of dense vectors.

5. **OpenAI LLM Integration 🧠**:
   - Incorporates OpenAI's Language Model (LLM) to enhance text generation, enabling the bot to produce accurate and contextually relevant texts.

## Future Directions 🛤️
This project marks the beginning of my journey in the language chain field. Excited to explore more and implement advanced features in the future.

## Connect with me 🤝
LinkedIn: [Akash Prajapati](https://www.linkedin.com/in/akashprap/)

## Downloads and API Key Update 📥🔑
To set up the environment and update the Open API key, follow these steps:

1. **Downloading Requirements**:
   - Run `pip install -r req.txt` to install all necessary dependencies.

2. **Updating Open API Key**:
   - Create a bash script (`update_api_key.sh`) with the following:
     ```bash
     #!/bin/bash
     export OPEN_API_KEY="YOUR_NEW_API_KEY"
     ```

   - Replace `YOUR_NEW_API_KEY` with the updated API key.
   - Execute the script with `source update_api_key.sh` to update the Open API key in the environment variables.

---
