"""Text-to-Speech endpoint using ElevenLabs API for Jarvis-like voice.

Setup:
1. Sign up at elevenlabs.io and get your API key
2. Set environment variable: ELEVENLABS_API_KEY=your_key_here
3. Choose a voice ID (default: "pNInz6obpgDQGcFmaJgB" - Adam, deep British male)
"""
import os
import requests
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt


ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY", "")
# Adam voice (deep, British male - closest to Jarvis)
# Alternatives: "21m00Tcm4TlvDq8ikWAM" (Rachel), "ErXwobaYiN019PkySvjV" (Antoni)
VOICE_ID = os.environ.get("ELEVENLABS_VOICE_ID", "pNInz6obpgDQGcFmaJgB")


@csrf_exempt
@require_http_methods(["POST"])
def text_to_speech_view(request):
    """Convert text to speech using ElevenLabs API.
    
    Request body (JSON):
        {
            "text": "Student role selected. Use your student ID to sign in."
        }
    
    Returns:
        Audio file (MP3) or JSON error
    """
    if not ELEVENLABS_API_KEY:
        return JsonResponse({
            "error": "ElevenLabs API key not configured. Set ELEVENLABS_API_KEY environment variable."
        }, status=500)
    
    try:
        import json
        data = json.loads(request.body)
        text = data.get("text", "").strip()
    except (json.JSONDecodeError, AttributeError):
        return JsonResponse({"error": "Invalid JSON body"}, status=400)
    
    if not text:
        return JsonResponse({"error": "Text parameter required"}, status=400)
    
    # Call ElevenLabs TTS API
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": ELEVENLABS_API_KEY
    }
    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75,
            "style": 0.0,
            "use_speaker_boost": True
        }
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return JsonResponse({
            "error": f"ElevenLabs API request failed: {str(e)}"
        }, status=502)
    
    # Return audio as MP3
    return HttpResponse(response.content, content_type="audio/mpeg")
