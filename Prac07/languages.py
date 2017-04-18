from Prac07.programminglanguage import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, vb]
    dynamic_typed_languages = [str(language.name) for language in languages if language.is_dynamic()]
    print("The Dynamically typed languages are:")
    for language in dynamic_typed_languages:
        print(language)



main()
