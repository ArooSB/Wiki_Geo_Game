import wikipedia
import random

NUM_OF_SENT = 4


def grab_word_prefixes(country_name):
    prefixes = []
    if " " in country_name:
        country_words = country_name.split()
        for word in country_words:
            prefixes.append(word[:2])
    else:
        prefixes.append(country_name[:2])
    if country_name == "United States":
        prefixes.append("Am")
    if country_name == "Ivory Coast":
        prefixes.append("Cô")
        prefixes.append("d'")
    return prefixes


def remove_parenthesized(summary):
    summary_len = len(summary)
    i = 0
    without_parenthesized = ''
    while i < summary_len:
        if summary[i] == '(':
            parentheses_levels = 1
            i += 1
            while i < summary_len:
                if summary[i] == ')' and parentheses_levels == 1:
                    i += 1
                    break
                if summary[i] == '(':
                    parentheses_levels += 1
                if summary[i] == ')':
                    parentheses_levels -= 1
                i += 1
            if i < summary_len and summary[i] == ')':
                i += 1
                if i < summary_len and summary[i] == ' ':
                    i += 1
        if i < summary_len:
            without_parenthesized += summary[i]
        i += 1
    return without_parenthesized


def censor_partial_mentions(summary, country_name, prefixes):
    words_list = summary.split()
    summary = ""
    punct = (',', ':', ';', '-', "'s")
    i = 0
    while i < len(words_list):
        if country_name in words_list[i] and words_list[i].endswith(punct):
            words_list[i] = words_list[i].replace(country_name, "_____")
            summary += words_list[i] + " "
            i += 1
        elif words_list[i][:2] in prefixes and words_list[i][0].isupper():
            while i < len(words_list) and words_list[i][:2] in prefixes:
                i += 1
            summary += "_____ "
        else:
            summary += words_list[i] + " "
            i += 1
    return summary


def censor_country_name(summary, country_name):
    """2 Clean data: first fetch a list of country-words-2-letter-prefixes.
    Then split the string into word and loop through it. Replace mentions
    of country_word or parts thereof via prefix comparison"""
    prefixes = grab_word_prefixes(country_name)
    summary = remove_parenthesized(summary)
    # summary = summary.replace(country_name, "_____")
    summary = censor_partial_mentions(summary, country_name, prefixes)
    return summary


def get_summary_alternative(w_article):
    article_sections = w_article.sections
    if "Tourism" in article_sections and w_article.section("Tourism") != '':
        section = w_article.section("Tourism")
    elif "Culture" in article_sections and w_article.section("Culture") != '':
        section = w_article.section("Culture")
    elif "Cuisine" in article_sections and w_article.section("Cuisine") != '':
        section = w_article.section("Cuisine")
    elif "Music" in article_sections and w_article.section("Music") != '':
        section = w_article.section("Music")
    elif "Literature" in article_sections and w_article.section("Literature") != '':
        section = w_article.section("Literature")
    else:  # if no cool section we fall back to the junk summary
        return wikipedia.summary(w_article, sentences=NUM_OF_SENT)
    section_sentences = section.split(".")  # Extract 4 sentences only
    i = 0
    section = ""
    for sentence in section_sentences:
        if i == NUM_OF_SENT:
            break
        section += sentence + ". "
        i += 1
    return section


def pick_country(list_of_countries):
    return random.choice(list_of_countries)


def fetch_summary_for_country(country_name):
    """1 Fetch summary"""
    try:
        country_article = wikipedia.WikipediaPage(country_name)
        if country_article:
            summary = wikipedia.summary(country_article, sentences=NUM_OF_SENT)
            if summary is None or summary == '' or "Wikipedia" in summary:
                summary = get_summary_alternative(country_article)
            return summary
        # identify errors
        else:
            print(f"Sadly, no article found for {country_name}.")
    except wikipedia.exceptions.PageError:
        print(f"Summary for {country_name} doesn't exist. Please try another country.")
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Disambiguation Error for {country_name}. Options: {e.options}")


# previously called "set up game mechanics", parent function for tasks 1 and 2
def pick_country_and_format_summary(list_of_countries):
    country_name = pick_country(list_of_countries)
    summary = None
    summary = fetch_summary_for_country(country_name)
    if summary is None:
        print("No summary creation was possible, returning <Bogus>")
        return country_name, "<Bogus Text>"
    summary = censor_country_name(summary, country_name)
    return country_name, summary
