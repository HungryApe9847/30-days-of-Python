from flashtext import KeywordProcessor

keyword_processor = KeywordProcessor()

keyword_processor.add_keyword("1")
keyword_processor.add_keyword("2")
keyword_processor.add_keyword("3")
keyword_processor.add_keyword("4")
keyword_processor.add_keyword("5")

while True:
    rating = input("Write a review (Make sure to include your star rating somewhere in it.): ")
    keywords_found = keyword_processor.extract_keywords(rating)
    if len(keywords_found) == 1:
        rating_number = keywords_found[0]
        break
    else:
        print("Please use only one star rating or number out of 5.")

print(f"Your review has been received! ({rating}, {rating_number} stars)")
