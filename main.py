import os
import requests, time, datetime, ast, operator                         
TELEGRAM_TOKEN = "8895486701:AAFRVLnQ05Ou7xL7MZ0HhlafAUZdczlidmk"     
GROQ_KEY = os.getenv("GROQ_API_KEY")
SYSTEM = "You are SharpAI, a sharp Nigerian business assistant from Lagos. Speak in clear Nigerian Pidgin mixed with simple English. Always call user 'Boss'. Keep replies short, direct, practical."

def ask_groq(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_KEY}", "Content-Type": "application/json"}
    data = {"model": "openai/gpt-oss-20b", "messages": [{"role":"system","content":SYSTEM},{"role":"user","content":prompt}]}
    try:
        r = requests.post(url, json=data, headers=headers, timeout=60)
        result = r.json()
        if "choices" not in result:
            return f"Groq error Boss: {result}"
        return result['choices'][0]['message']['content']                  except Exception as e:
        return f"Wahala be: {e}"

def send(chat_id, text):                                                   requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", json={"chat_id": chat_id, "text": text[:4000]})

def calc(expr):                                                            try:
        return str(eval(expr, {"__builtins__": {}}))
    except:
        return "That calculation no correct Boss"                      
print("SharpAI V2 don start...")
offset = 0
while True:                                                                try:
        r = requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates", params={"offset": offset, "timeout": 30}, timeout=35).json()
        for u in r.get("result", []):
            offset = u["update_id"] + 1
            msg = u.get("message", {})
            chat_id = msg.get("chat", {}).get("id")                                text = msg.get("text", "")
            if not chat_id or not text: continue

            if text == "/start":                                                       send(chat_id, "How far Boss! Na SharpAI V2 be this.\n\nUse:\n/business shoe business for Lagos\n/content for shoe business\n/reply customer dey ask for discount\n/time\n/calc 2500*4")
            elif text == "/time":                                                      send(chat_id, datetime.datetime.now().strftime("Boss, na %I:%M %p, %A %d %B %Y"))
            elif text.startswith("/calc"):
                send(chat_id, "Answer: " + calc(text.replace("/calc","").strip()))
            elif text.startswith("/business"):
                idea = text.replace("/business","").strip() or "any business for Lagos"
                send(chat_id, ask_groq(f"Give step-by-step business plan for: {idea}. Include startup cost, how to get customers, and profit tip for Nigeria."))                                                                 elif text.startswith("/content"):
                topic = text.replace("/content","").strip() or "my business"
                send(chat_id, ask_groq(f"Give 5 viral content ideas for {topic} for TikTok and WhatsApp status to get customers for Nigeria."))                                                                                  elif text.startswith("/reply"):
                cust = text.replace("/reply","").strip()
                send(chat_id, ask_groq(f"Write a polite professional WhatsApp reply to this customer, for Nigerian business style: {cust}"))              else:
                send(chat_id, ask_groq(text))
    except Exception as e:
        print("Error:", e)
        time.sleep(5)                                                  ~ $ cat main.py
import os
import requests, time, datetime, ast, operator                         
TELEGRAM_TOKEN = "8895486701:AAFRVLnQ05Ou7xL7MZ0HhlafAUZdczlidmk"
GROQ_KEY = os.getenv("GROQ_API_KEY")                                   
SYSTEM = "You are SharpAI, a sharp Nigerian business assistant from Lagos. Speak in clear Nigerian Pidgin mixed with simple English. Always call user 'Boss'. Keep replies short, direct, practical."

def ask_groq(prompt):                                                      url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_KEY}", "Content-Type": "application/json"}                                                         data = {"model": "openai/gpt-oss-20b", "messages": [{"role":"system","content":SYSTEM},{"role":"user","content":prompt}]}
    try:
        r = requests.post(url, json=data, headers=headers, timeout=60)
        result = r.json()
        if "choices" not in result:
            return f"Groq error Boss: {result}"                                return result['choices'][0]['message']['content']
    except Exception as e:
        return f"Wahala be: {e}"

def send(chat_id, text):
    requests.post(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", json={"chat_id": chat_id, "text": text[:4000]})                
def calc(expr):
    try:
        return str(eval(expr, {"__builtins__": {}}))
    except:
        return "That calculation no correct Boss"
                                                                       print("SharpAI V2 don start...")
offset = 0
while True:
    try:
        r = requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates", params={"offset": offset, "timeout": 30}, timeout=35).json()                                                                            for u in r.get("result", []):
            offset = u["update_id"] + 1
            msg = u.get("message", {})
            chat_id = msg.get("chat", {}).get("id")
            text = msg.get("text", "")
            if not chat_id or not text: continue
                                                                                   if text == "/start":
                send(chat_id, "How far Boss! Na SharpAI V2 be this.\n\nUse:\n/business shoe business for Lagos\n/content for shoe business\n/reply customer dey ask for discount\n/time\n/calc 2500*4")
            elif text == "/time":
                send(chat_id, datetime.datetime.now().strftime("Boss, na %I:%M %p, %A %d %B %Y"))                                                         elif text.startswith("/calc"):
                send(chat_id, "Answer: " + calc(text.replace("/calc","").strip()))
            elif text.startswith("/business"):
                idea = text.replace("/business","").strip() or "any business for Lagos"
                send(chat_id, ask_groq(f"Give step-by-step business plan for: {idea}. Include startup cost, how to get customers, and profit tip for Nigeria."))
            elif text.startswith("/content"):
                topic = text.replace("/content","").strip() or "my business"
                send(chat_id, ask_groq(f"Give 5 viral content ideas for {topic} for TikTok and WhatsApp status to get customers for Nigeria."))                                                                                  elif text.startswith("/reply"):
                cust = text.replace("/reply","").strip()
                send(chat_id, ask_groq(f"Write a polite professional WhatsApp reply to this customer, for Nigerian business style: {cust}"))
            else:
                send(chat_id, ask_groq(text))
    except Exception as e:                                                     print("Error:", e)
        time.sleep(5)
