# 📊 Trade Opportunities Analyzer API

An AI-powered FastAPI application that analyzes Indian market sectors and generates structured trade opportunity reports using real-time data and LLM intelligence.

---

## 🚀 Features

- 🔍 Fetches real-time market trends data (DuckDuckGo API)  
- 🤖 AI-based sector analysis using Groq (LLM)  
- ⚡ FastAPI backend with async support  
- 🧠 Intelligent caching system for performance  
- 🔐 Token-based authentication  
- 🚦 Rate limiting (5 requests/minute per user)  
- 📊 Interactive web UI (served from root endpoint)  

---

## 🏗️ Tech Stack

- **Backend:** FastAPI  
- **HTTP Client:** httpx  
- **Rate Limiting:** slowapi  
- **AI Model:** Groq (LLaMA 3.1)  
- **Server:** Uvicorn  

---

## 📂 Project Structure


.
├── main.py # FastAPI app (UI + API routes)
├── auth.py # Token authentication
├── ai_analyzer.py # AI report generation (Groq)
├── data_fetcher.py # Fetch market data
├── cache.py # In-memory caching
├── session.py # Session tracking
├── rate_limiter.py # Rate limiting config
├── requirements.txt # Dependencies
├── Dockerfile # Docker deployment


---

## ⚙️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/trade-analyzer.git
cd trade-analyzer
2️⃣ Install Dependencies
pip install -r requirements.txt
🔑 Environment Variables

Create a .env file or set environment variables:

GROQ_API_KEY=your_groq_api_key
API_TOKEN=your_secure_token
▶️ Run the Application
uvicorn main:app --reload

App will be available at:
👉 http://127.0.0.1:8000/

🌐 Usage
🔹 Web UI

Open browser → http://127.0.0.1:8000/

Enter a sector (e.g., technology)

Click Analyze

🔹 API Endpoint

GET /analyze/{sector}

Example:
curl -H "Authorization: your_token" \
http://127.0.0.1:8000/analyze/technology
📊 How It Works

User inputs a sector

API fetches real-time data

Cache is checked for existing results

AI generates structured report

Result is returned in Markdown format

🔒 Security

Token-based authentication

Rate limiting (5 requests/minute per user)

🐳 Docker Deployment
docker build -t trade-analyzer .
docker run -p 8000:8000 trade-analyzer
📌 Future Improvements

📈 Add real stock market APIs (NSE/BSE)

🧾 Save reports to database

📊 Add charts & visual analytics

👤 User authentication system

☁️ Deploy to cloud (AWS / Hugging Face Spaces)

🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

👨‍💻 Author

Bejjanki Venkata Siva Prasad
