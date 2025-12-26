from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="ExplainIt AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    text: str
    age: str

@app.get("/")
def home():
    return {"message": "ExplainIt AI backend is running"}

@app.post("/explain")
def explain(data: UserInput):
    text = data.text.lower()
    age = data.age.lower()

    # PHOTOSYNTHESIS
    if "photosynthesis" in text:
        if age == "child":
            result = "🌱✨ Plants are tiny chefs! They use sunlight, air, and water to cook their own food inside their leaves. This special magic helps them grow strong and green!"
        elif age == "adult":
            result = "Photosynthesis is the process by which green plants use sunlight, carbon dioxide, and water to produce food (glucose) and release oxygen. It is essential for life on Earth."
        else:
            result = "Plants use sunlight, water, and air to prepare their own food. This process helps plants grow and provides oxygen."

    # GRAVITY
    elif "gravity" in text:
        if age == "child":
            result = "🍎⬇️ Gravity is the invisible force that pulls everything down to Earth. It keeps your toys, you, and even oceans from floating away!"
        elif age == "adult":
            result = "Gravity is a natural force that attracts objects toward each other. It keeps planets in orbit and objects grounded on Earth."
        else:
            result = "Gravity pulls objects toward the Earth. It keeps us standing on the ground and causes things to fall."

    # INTERNET
    elif "internet" in text:
        if age == "child":
            result = "🌐🚀 The internet is like a magical super-fast road! It lets you watch videos, play games, and talk to people far away in seconds."
        elif age == "adult":
            result = "The internet is a global network that connects millions of computers. It allows people to share information, communicate, and access services worldwide."
        else:
            result = "The internet connects people and computers across the world. It helps us communicate, learn, and find information easily."

    # ELECTRICITY
    elif "electricity" in text:
        if age == "child":
            result = "⚡💡 Electricity is invisible energy that travels through wires like tiny racers! It helps lights glow and fans spin."
        elif age == "adult":
            result = "Electricity is the flow of electric charge through a conductor. It is used to power devices, machines, and modern technology."
        else:
            result = "Electricity is a form of energy that powers homes and machines. It helps devices work properly."

    # ARTIFICIAL INTELLIGENCE
    elif "artificial intelligence" in text or "ai" in text:
        if age == "child":
            result = "🤖🧠 AI is when computers learn and think like humans! They can recognize faces, answer questions, and even play games."
        elif age == "adult":
            result = "Artificial Intelligence is a field of computer science that enables machines to learn, reason, and make decisions similar to human intelligence"
        else:
            result = "AI allows computers to learn from data and make smart decisions. It is used in apps, machines, and smart devices."

    # CLIMATE CHANGE
    elif "climate" in text:
        if age == "child":
            result =  "🌍🔥 Climate change means Earth is getting warmer, like wearing too many blankets! It affects animals, weather, and our planet."
        elif age == "adult":
            result = "Climate change refers to long-term changes in Earth's temperature and weather patterns. It is largely caused by human activities like pollution and deforestation."
        else:
            result = "Climate change affects weather, temperatures, and the environment. It can impact plants, animals, and humans."

    else:
        result = "⚠️ Topic not recognized. Please try another concept."

    return {"result": result}

