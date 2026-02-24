import discord
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
# URL Menggunakan Gemini 2.5 Flash
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def get_gemini_response(user_text):
    headers = {'Content-Type': 'application/json'}
    # Kita masukkan instruksi kepribadian sebagai pesan pertama dari 'user' 
    # agar AI paham perannya tanpa menyebabkan error JSON
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": "Instruksi Sistem: Kamu adalah Endeavour AI, asisten cerdas dan keren. Mulai sekarang, jawablah semua pesan dengan kepribadian tersebut."}]
            },
            {
                "role": "model",
                "parts": [{"text": "Siap! Saya adalah Endeavour AI. Ada yang bisa saya bantu?"}]
            },
            {
                "role": "user",
                "parts": [{"text": user_text}]
            }
        ]
    }
    
    response = requests.post(GEMINI_URL, headers=headers, data=json.dumps(payload))
    data = response.json()
    
    try:
        return data['candidates'][0]['content']['parts'][0]['text']
    except Exception:
        error_msg = data.get('error', {}).get('message', 'Gagal mengambil respon')
        return f"Waduh, ada kendala teknik: {error_msg}"

@client.event
async def on_ready():
    print(f'--- STATUS: {client.user} ONLINE (GEMINI 2.5 FLASH) ---')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    is_mentioned = client.user in message.mentions
    is_dm = isinstance(message.channel, discord.DMChannel)

    if is_mentioned or is_dm:
        clean_text = message.content.replace(f'<@!{client.user.id}>', '').replace(f'<@{client.user.id}>', '').strip()
        
        if not clean_text and is_mentioned:
            await message.reply("Ya? Ada yang bisa saya bantu?")
            return

        print(f"DEBUG: Memproses pesan dari {message.author}: {clean_text}")
        
        async with message.channel.typing():
            ai_response = get_gemini_response(clean_text)
            
            # --- LOGIKA CHUNKING (MEMOTONG PESAN) ---
            # Jika pesan lebih dari 2000 karakter, kita bagi per 1900 agar aman
            if len(ai_response) > 2000:
                for i in range(0, len(ai_response), 1900):
                    part = ai_response[i:i+1900]
                    await message.channel.send(part)
            else:
                await message.reply(ai_response)

client.run(DISCORD_TOKEN)