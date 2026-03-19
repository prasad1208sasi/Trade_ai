from groq import Groq
import os
import asyncio

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def sync_groq_call(sector, data):

    prompt = f"""
    Analyze the Indian {sector} sector.

    Provide a structured markdown report with:
    - Overview
    - Current Trends
    - Trade Opportunities
    - Risks
    - Conclusion

    Data:
    {data}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return response.choices[0].message.content


async def analyze_data(sector, data):
    return await asyncio.to_thread(sync_groq_call, sector, data)