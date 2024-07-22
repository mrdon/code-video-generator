"""Text to speech
"""
import hashlib, os
from manim import logger


def get_audio_path(input, engine, format):
    hash = hashlib.sha224(input.encode()).hexdigest()
    path = os.path.join("media", "audio", engine, hash + "." + format)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return path


def silence_tts(input):
    """Crude/effective subtitles silent clip generator.

    FEATURE: There is a little audible "tap-tap" when the subtitles change. This
             cues the reader about the next set of subtitles to read.
    """
    import wave

    length = len(input.split(" ")) / 250 * 60
    sample_rate = 44100
    path = get_audio_path(input, "silence", "wav")
    with wave.Wave_write(path) as f:
        f.setnchannels(1)
        f.setsampwidth(1)
        f.setframerate(sample_rate)
        f.writeframes(b"\x00" * int(sample_rate * length))
    return path, length


def local_tts(input):
    import subprocess
    import wave
    import contextlib

    path = get_audio_path(input, "local", "wav")
    command = ["say", "--data-format=LEI16", "-v", "Alex", input, "-o", path]
    logger.debug("Running: Popen(%s)" % (command))
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = proc.communicate()
    logger.debug("Popen(%s) exitied with status %d" % (command, proc.returncode))
    logger.debug("STDOUT>%s" % out)
    logger.debug("STDERR>%s" % err)
    length = 0.0
    with contextlib.closing(wave.open(path, "r")) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        length = frames / float(rate)
    print("Length of audio file: ", length)
    print(path, length)
    return path, length


def google_tts(input):
    from mutagen.mp3 import MP3
    from google.cloud import texttospeech

    logger.warning(
        "Performing TTS operation using Google Cloud Text-to-speech. This may cost actual money."
    )
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=input)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    path = get_audio_path(input, "google", "mp3")
    with open(path, "wb") as f:
        f.write(response.audio_content)
    return path, MP3(path).info.length
