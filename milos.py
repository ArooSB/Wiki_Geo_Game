import wikipedia
import random

NUM_OF_BAD_ANSWERS = 3


def gen_bad_answers(correct_answer, list_of_countries):
    the_3_bad_answers = []
    while len(the_3_bad_answers) < NUM_OF_BAD_ANSWERS:
        bad_answer_candidate = random.choice(list_of_countries)
        if bad_answer_candidate != correct_answer:
            the_3_bad_answers.append(bad_answer_candidate)
    return the_3_bad_answers
        

"""
def main():
    
    list_of_countries = countries.get_all_countries() # Milos
    total_score = 0
    for i in range(NUM_OF_ROUNDS): # Ahmed
        # country_tuple = fetch_summary(list_of_countries)  # Aroosha
        countries_scription = formatsummary.pick_country_and_format_summary(list_of_countries)
        
        # cleaned_country_tuple = clean_summary(country_tuple)  # Aroosha
        # bad_answers = get_bad_answers(cleaned_country_tuple[0])  # Milos

        score = artjom.play_one_round(cleaned_country_tuple, bad_answers)
        # score = play_one_round(cleaned_country_tuple, bad_answers)  # Artjom
        total_score += score
        #
    display_counter.display_score(total_score, NUM_OF_ROUNDS) # return print out of the score.

if __name__ == "__main__":
    main()
"""