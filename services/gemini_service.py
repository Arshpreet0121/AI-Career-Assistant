import os
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-3.5-flash"


def ask_gemini(prompt):

    max_retries = 3

    for attempt in range(max_retries):

        try:

            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )

            return response.text

        except Exception as e:

            error = str(e).lower()

            if (
                "503" in error
                or "busy" in error
                or "temporarily unavailable" in error
            ):

                if attempt < max_retries - 1:
                    time.sleep(3)
                    continue

                return (
                    "⚠️ Gemini is currently busy.\n\n"
                    "Please wait a minute and try again."
                )

            elif (
                "quota" in error
                or "resource_exhausted" in error
            ):

                return (
                    "⚠️ API quota exceeded.\n\n"
                    "Please check your Gemini API quota or try again later."
                )

            else:

                return f"Unexpected Error:\n\n{e}"