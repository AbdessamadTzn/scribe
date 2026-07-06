from src.main import to_markdown


def test_to_markdown_includes_all_sections():
    data = {
        "titre": "Point hebdo",
        "resume": "Résumé factuel.",
        "points_cles": ["Point A", "Point B"],
        "decisions_et_actions": ["Décision 1"],
    }

    result = to_markdown(data)

    assert "# Point hebdo" in result
    assert "## Résumé\nRésumé factuel." in result
    assert "- Point A" in result
    assert "- Point B" in result
    assert "- Décision 1" in result


def test_to_markdown_handles_missing_fields():
    result = to_markdown({})

    assert "# Compte rendu" in result
    assert "## Points clés" in result
    assert "## Décisions et actions" in result
