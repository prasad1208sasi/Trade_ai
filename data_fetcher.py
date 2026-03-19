import httpx

async def fetch_sector_data(sector: str):
    query = f"{sector} India market trends"

    url = f"https://api.duckduckgo.com/?q={query}&format=json"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    data = response.json()

    results = data.get("RelatedTopics", [])

    extracted = []
    for item in results:
        if isinstance(item, dict) and "Text" in item:
            extracted.append(item["Text"])

    return "\n".join(extracted[:5])