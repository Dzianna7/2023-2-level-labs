"""
Language detection starter
"""
from lab_1_classify_by_unigrams.main import detect_language

from lab_1_classify_by_unigrams.main import create_language_profile


def main() -> None:
    """
    Launches an implementation
    """
    with open("assets/texts/en.txt", "r", encoding="utf-8") as file_to_read_en:
        en_text = file_to_read_en.read()
    with open("assets/texts/de.txt", "r", encoding="utf-8") as file_to_read_de:
        de_text = file_to_read_de.read()
    with open("assets/texts/unknown.txt", "r", encoding="utf-8") as file_to_read_unk:
        unknown_text = file_to_read_unk.read()
    english_profile = create_language_profile('en', en_text)
    deutsch_profile = create_language_profile('de', de_text)
    unknown_profile = create_language_profile('unk', unknown_text)
    if (
            isinstance(unknown_profile, dict) and
            isinstance(english_profile, dict) and
            isinstance(deutsch_profile, dict)
    ):
        result = detect_language(unknown_profile, english_profile, deutsch_profile)
        assert result, "Detection result is None"

if __name__ == "__main__":
    main()
