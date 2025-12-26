def create_prompt(text, age):
    if age == "kid":
        return f"""
        Explain this to a child (6-12 years old).
        Use very simple words and examples.

        Text: {text}
        """

    elif age == "adult":
        return f"""
        Explain this clearly to a normal adult.
        Be short and clear.

        Text: {text}
        """

    elif age == "elder":
        return f"""
        Explain this to an elderly person.
        Use simple language and short sentences.

        Text: {text}
        """
