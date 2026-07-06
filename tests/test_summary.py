import json
from unittest.mock import MagicMock, patch

from src.summary import generate_summary


@patch("src.summary.client")
def test_generate_summary_returns_model_output(mock_client):
    expected = json.dumps({"titre": "Réunion", "resume": "ok", "points_cles": [], "decisions_et_actions": []})
    mock_response = MagicMock()
    mock_response.choices[0].message.content = expected
    mock_client.chat.completions.create.return_value = mock_response

    result = generate_summary("une transcription")

    assert result == expected


@patch("src.summary.client")
def test_generate_summary_uses_json_response_format(mock_client):
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "{}"
    mock_client.chat.completions.create.return_value = mock_response

    generate_summary("une transcription")

    _, kwargs = mock_client.chat.completions.create.call_args
    assert kwargs["response_format"] == {"type": "json_object"}
    assert kwargs["messages"][1] == {"role": "user", "content": "une transcription"}
