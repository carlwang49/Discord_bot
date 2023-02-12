from config import Config, bot
import discord 
import whisper

@bot.tree.command(name="speechtotext",description="上傳檔案，將檔案轉為文字")
async def speechtotext(interaction: discord.Interaction, file: discord.Attachment):
    await interaction.response.defer()

    audio_path = file.url
    model = whisper.load_model("base")

    audio = whisper.load_audio(audio_path)

    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    language = max(probs, key=probs.get)
    print(f"Detected language: {language}")

    result = model.transcribe(audio_path, fp16=False, language=language)
    print(result["text"])

    await interaction.followup.send(result["text"])