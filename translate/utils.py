import random
import string


def generate_file_name(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def get_languages_and_codes():
    languages = [
        {
            "code": "af",
            "name": "Afrikaans"
        },
        {
            "code": "ak",
            "name": "Akan"
        },
        {
            "code": "sq",
            "name": "Albanian"
        },
        {
            "code": "am",
            "name": "Amharic"
        },
        {
            "code": "ar",
            "name": "Arabic"
        },
        {
            "code": "hy",
            "name": "Armenian"
        },
        {
            "code": "az",
            "name": "Azerbaijani"
        },
        {
            "code": "be",
            "name": "Belarusian"
        },
        {
            "code": "bn",
            "name": "Bengali"
        },
        {
            "code": "bh",
            "name": "Bihari"
        },
        {
            "code": "bs",
            "name": "Bosnian"
        },
        {
            "code": "br",
            "name": "Breton"
        },
        {
            "code": "km",
            "name": "Cambodian"
        },
        {
            "code": "ca",
            "name": "Catalan"
        },
        {
            "code": "chr",
            "name": "Cherokee"
        },
        {
            "code": "zh-CN",
            "name": "Chinese (Simplified)"
        },
        {
            "code": "zh-TW",
            "name": "Chinese (Traditional)"
        },
        {
            "code": "co",
            "name": "Corsican"
        },
        {
            "code": "hr",
            "name": "Croatian"
        },
        {
            "code": "cs",
            "name": "Czech"
        },
        {
            "code": "da",
            "name": "Danish"
        },
        {
            "code": "nl",
            "name": "Dutch"
        },
        {
            "code": "en",
            "name": "English"
        },
        {
            "code": "eo",
            "name": "Esperanto"
        },
        {
            "code": "et",
            "name": "Estonian"
        },
        {
            "code": "fl",
            "name": "Finnish"
        },
        {
            "code": "fr",
            "name": "French"
        },
        {
            "code": "fy",
            "name": "Frisian"
        },
        {
            "code": "ka",
            "name": "Georgian"
        },
        {
            "code": "de",
            "name": "German"
        },
        {
            "code": "el",
            "name": "Greek"
        },
        {
            "code": "iw",
            "name": "Hebrew"
        },
        {
            "code": "hi",
            "name": "Hindi"
        },
        {
            "code": "is",
            "name": "Icelandic"
        },
        {
            "code": "ig",
            "name": "Igbo"
        },
        {
            "code": "id",
            "name": "Indonesian"
        },
        {
            "code": "ia",
            "name": "Interlingua"
        },
        {
            "code": "ga",
            "name": "Irish"
        },
        {
            "code": "it",
            "name": "Italian"
        },
        {
            "code": "ja",
            "name": "Japanese"
        },
        {
            "code": "jw",
            "name": "Javanese"
        },
        {
            "code": "ko",
            "name": "Korean"
        },
        {
            "code": "kri",
            "name": "Krio"
        },
        {
            "code": "ckb",
            "name": "Kurdish"
        },
        {
            "code": "ky",
            "name": "Kyrgyz"
        },
        {
            "code": "lo",
            "name": "Laothian"
        },
        {
            "code": "la",
            "name": "Latin"
        },
        {
            "code": "lv",
            "name": "Latvian"
        },
        {
            "code": "ln",
            "name": "Lingala"
        },
        {
            "code": "lt",
            "name": "Lithuanian"
        },
        {
            "code": "loz",
            "name": "Lozi"
        },
        {
            "code": "lg",
            "name": "Luganda"
        },
        {
            "code": "ach",
            "name": "Luo"
        },
        {
            "code": "mk",
            "name": "Macedonian"
        },
        {
            "code": "mg",
            "name": "Malagasy"
        },
        {
            "code": "ms",
            "name": "Malay"
        },
        {
            "code": "ml",
            "name": "Malayalam"
        },
        {
            "code": "pcm",
            "name": "Nigerian Pidgin"
        },
        {
            "code": "nso",
            "name": "Northern Sotho"
        },
        {
            "code": "no",
            "name": "Norwegian"
        },
        {
            "code": "nn",
            "name": "Norwegian (Nynorsk)"
        },
        {
            "code": "fa",
            "name": "Persian"
        },
        {
            "code": "pl",
            "name": "Polish"
        },
        {
            "code": "pt-BR",
            "name": "Portuguese (Brazil)"
        },
        {
            "code": "pt-PT",
            "name": "Portuguese (Portugal)"
        },
        {
            "code": "pa",
            "name": "Punjabi"
        },
        {
            "code": "nyn",
            "name": "Runyakitara"
        },
        {
            "code": "ru",
            "name": "Russian"
        },
        {
            "code": "gd",
            "name": "Scots Gaelic"
        },
        {
            "code": "sr",
            "name": "Serbian"
        },
        {
            "code": "sh",
            "name": "Serbo-Croatian"
        },
        {
            "code": "st",
            "name": "Sesotho"
        },
        {
            "code": "sd",
            "name": "Sindhi"
        },
        {
            "code": "asif",
            "name": "Sinhalese"
        },
        {
            "code": "sk",
            "name": "Slovak"
        },
        {
            "code": "sl",
            "name": "Slovenian"
        },
        {
            "code": "so",
            "name": "Somali"
        },
        {
            "code": "es",
            "name": "Spanish"
        },
        {
            "code": "es-419",
            "name": "Spanish (Latin American)"
        },
        {
            "code": "su",
            "name": "Sundanese"
        },
        {
            "code": "sw",
            "name": "Swahili"
        },
        {
            "code": "sv",
            "name": "Swedish"
        },
        {
            "code": "ta",
            "name": "Tamil"
        },
        {
            "code": "tr",
            "name": "Turkish"
        },
        {
            "code": "uk",
            "name": "Ukrainian"
        },
        {
            "code": "ur",
            "name": "Urdu"
        },
        {
            "code": "vi",
            "name": "Vietnamese"
        },
        {
            "code": "cy",
            "name": "Welsh"
        },
        {
            "code": "wo",
            "name": "Wolof"
        },
        {
            "code": "xh",
            "name": "Xhosa"
        },
        {
            "code": "yo",
            "name": "Yoruba"
        },
        {
            "code": "zu",
            "name": "Zulu"
        }
    ]
    return languages


def get_language_by_code_name(code_name):
    for language_obj in get_languages_and_codes():
        if language_obj.get('code') == code_name:
            return language_obj.get('name')
