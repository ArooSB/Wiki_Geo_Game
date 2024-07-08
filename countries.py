import wikipedia
import os


def parse_html_for_countries():
    """ Parse the html from a hardcopy in data subdirectory """
    list_of_countries = []
    with open("data/countries_table_wiki_html_backup", "r") as fd:
        lines = fd.readlines()
    i = 0
    num_of_lines = len(lines)
    while i < num_of_lines:
        if "<tbody>" in lines[i]:  # find the beginning of the table
            break
        i += 1
    while i < num_of_lines:
        if "<tr>" in lines[i]: # find the beginning of each table row
            while i < num_of_lines:
                if "title=" in lines[i]:  # get country name
                    start = lines[i].find("title=") + len("title=") + len('"')
                    end = start
                    while lines[i][end] != '"':
                        end += 1
                    list_of_countries.append(lines[i][start:end])
                if "</tr>" in lines[i]:
                    break
                i += 1
        if "</tbody>" in lines[i]:
            break
        i += 1
    if "United Nations" in list_of_countries:
        list_of_countries.remove("United Nations")
    if "Wikipedia:Disputed statement" in list_of_countries:
        list_of_countries.remove("Wikipedia:Disputed statement")
    preset_file_path = os.path.join("data", "preset_list_of_countries")
    if not os.path.exists(preset_file_path):
        with open(preset_file_path, "w") as fd:
            for country in list_of_countries:
                fd.write(country + '\n')
    return list_of_countries


def look_for_preset_file():
    if not os.path.exists("data"):
        os.mkdir("data")
        return None
    preset_file_path = os.path.join("data", "preset_list_of_countries")
    if os.path.exists(preset_file_path):
        with open(preset_file_path, "r") as fd:
            list_of_countries = []
            lines = fd.readlines()
            for line in lines:
                list_of_countries.append(line.strip())
        return list_of_countries
    return None


def get_all_countries():
    """ If html hard copy not found in data directory, fetch it from Wiki.
    Else parse the html"""
    list_of_countries = look_for_preset_file()
    if list_of_countries is not None:
        return list_of_countries
    pg_html = None
    html_path = os.path.join("data", "countries_table_wiki_html_backup")
    if not os.path.exists(html_path):
        print("Er: Countries data not found, fetching from Wikipedia...")
        try:
            pg_html = wikipedia.WikipediaPage(
                "List of countries and dependencies by population").html()
        except wikipedia.exceptions.PageError:
            print("Page not found")
        except wikipedia.exceptions.DisambiguationError as e:
            print(f"Disambiguation error: {e.options}")
        except wikipedia.exceptions.HTTPTimeoutError as e:
            print(e)
        except wikipedia.exceptions.RedirectError as e:
            print(e)
        except wikipedia.exceptions.WikipediaException:
            print("Undefined error")
    if (pg_html is not None and
            not os.path.exists("data/countries_table_wiki_html_backup")):
        fd = open("data/countries_table_wiki_html_backup", "w")
        fd.write(pg_html)
        fd.close()
        list_of_countries = parse_html_for_countries()
    else:
        list_of_countries = parse_html_for_countries()
    return list_of_countries