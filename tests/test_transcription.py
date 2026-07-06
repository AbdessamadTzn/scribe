import pytest
from unittest.mock import MagicMock, patch, mock_open

from src.transcription import transcribe


@patch("src.transcription.client")
def test_transcribe_calls_groq_with_expected_params(mock_client):
    mock_client.audio.transcriptions.create.return_value = MagicMock(text="bonjour")

    with patch("builtins.open", mock_open(read_data=b"audio-bytes")):
        result = transcribe("audios/demo.mp4")

    assert result.text == "bonjour"
    _, kwargs = mock_client.audio.transcriptions.create.call_args
    assert kwargs["response_format"] == "verbose_json"
    assert kwargs["language"] == "fr"
    assert kwargs["temperature"] == 0.0


def test_transcribe_raises_when_file_missing():
    with pytest.raises(FileNotFoundError):
        transcribe("audios/fichier_inexistant.mp3")
