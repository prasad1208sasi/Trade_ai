from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.responses import Response, JSONResponse, HTMLResponse

from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from auth import verify_token
from rate_limiter import limiter
from data_fetcher import fetch_sector_data
from ai_analyzer import analyze_data
from session import track_session
from cache import get_cache, set_cache

app = FastAPI()

# 🔹 Rate Limiter Setup
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request, exc):
    return JSONResponse(
        status_code=429,
        content={"detail": "Rate limit exceeded"}
    )

# 🔥 MAIN UI (NOW ROOT PAGE)
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head>
        <title>Trade Opportunities Analyzer</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                background: #0f172a;
                color: white;
                text-align: center;
                padding: 50px;
            }

            .container {
                background: #1e293b;
                padding: 30px;
                border-radius: 12px;
                max-width: 600px;
                margin: auto;
                box-shadow: 0px 0px 20px rgba(0,0,0,0.5);
            }

            h1 {
                color: #38bdf8;
            }

            input {
                padding: 12px;
                width: 70%;
                border-radius: 8px;
                border: none;
                margin-top: 20px;
                font-size: 16px;
            }

            button {
                padding: 12px 20px;
                margin-left: 10px;
                border: none;
                border-radius: 8px;
                background: #38bdf8;
                color: black;
                font-weight: bold;
                cursor: pointer;
            }

            button:hover {
                background: #0ea5e9;
            }

            #result {
                margin-top: 20px;
                text-align: left;
                background: black;
                padding: 15px;
                border-radius: 8px;
                max-height: 300px;
                overflow-y: auto;
                white-space: pre-wrap;
            }

            .loading {
                color: yellow;
                margin-top: 10px;
            }
        </style>
    </head>

    <body>
        <div class="container">
            <h1>📊 Trade Opportunities Analyzer</h1>
            <p>Analyze Indian market sectors using AI</p>

            <input id="sector" placeholder="Enter sector (e.g. technology)" />
            <button onclick="callAPI()">Analyze</button>

            <div class="loading" id="loading"></div>

            <div id="result"></div>
        </div>

        <script>
            async function callAPI() {
                let sector = document.getElementById("sector").value;
                let resultBox = document.getElementById("result");
                let loading = document.getElementById("loading");

                if (!sector) {
                    alert("Please enter a sector!");
                    return;
                }

                loading.innerText = "⏳ Analyzing... please wait";
                resultBox.innerText = "";

                try {
                    let res = await fetch(`/analyze/${sector}`, {
                        headers: { "Authorization": "abc" }
                    });

                    let data = await res.text();

                    loading.innerText = "";
                    resultBox.innerText = data;

                } catch (error) {
                    loading.innerText = "";
                    resultBox.innerText = "❌ Error occurred!";
                }
            }
        </script>
    </body>
    </html>
    """

# 🔹 API ENDPOINT
@app.get("/analyze/{sector}")
@limiter.limit("5/minute")
async def analyze_sector(
    request: Request,
    sector: str,
    user=Depends(verify_token)
):
    if not sector.isalpha():
        raise HTTPException(status_code=400, detail="Invalid sector")

    track_session(user["user"])

    cached = get_cache(sector)
    if cached:
        return Response(content=cached, media_type="text/markdown")

    raw_data = await fetch_sector_data(sector)
    report = await analyze_data(sector, raw_data)

    set_cache(sector, report)

    return Response(content=report, media_type="text/markdown")