from config import Config, bot
import discord 
import whisper
import openai

@bot.tree.command(name="speechtosummary",description="上傳檔案，將檔案轉為文字，並總結內容")
# async def speechtotext(ctx:commands.Context):
async def speechtosummary(interaction: discord.Interaction, file: discord.Attachment):
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
    speech_messages = result["text"]
    print(speech_messages)
    # await interaction.followup.send(speech_messages)
    
    prompt = f"以下是逐字稿，請幫我整理重點: {speech_messages}"
    max_tokens = 4000 - 3*len(prompt)
    # print(len(prompt))
    # print(max_tokens)
    response = await openai.Completion.acreate(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=max_tokens,
        # top_p=1.0,
        # frequency_penalty=0.0,
        # presence_penalty=0.0
    )
    response_dict = response.get("choices")
    if response_dict and len(response_dict)>0:
        summary_message = response_dict[0]["text"]

    print(summary_message)
    await interaction.followup.send('逐字稿:\n'+ speech_messages + "\n\n總結:\n" + summary_message)
