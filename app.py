import gradio as gr
from gtts import gTTS
import os

def text_to_speech(text, language):
    if not text.strip():
        return None
    
    lang_code = {
        "Українська": "uk",
        "Англійська": "en",
        "Польська": "pl"
    }.get(language, "uk")

    try:
        tts = gTTS(text=text, lang=lang_code, slow=False)

        output_file = "output_audio.mp3"
        tts.save(output_file)
        
        return output_file
    except Exception as e:
        return f"Помилка: {e}"

print("Запуск локального веб-сервера")

app = gr.Interface(
    fn=text_to_speech,
    inputs=[
        gr.Textbox(lines=4, placeholder="Введіть текст тут...", label="Ваш текст"),
        gr.Radio(choices=["Українська", "Англійська", "Польська"], value="Українська", label="Мова озвучення")
    ],
    outputs=gr.Audio(type="filepath", label="Згенероване мовлення"),
    title="Генератор мовлення",
    description="Цей генератор мовлення перетворює текст на голос за допомогою безкоштовного Google TTS API. Напишіть щось і натисніть Submit.",
    theme="default"
)

if __name__ == "__main__":
    app.launch()