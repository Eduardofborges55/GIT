from django.shortcuts import render
from core.llm import chat_with_llm

def home(request):
    resposta = None

    if request.method == "POST":
        prompt = request.POST.get("prompt")
        resposta = chat_with_llm(prompt)

    return render(request, "frontend/home.html", {
        "resposta": resposta
    }) 
