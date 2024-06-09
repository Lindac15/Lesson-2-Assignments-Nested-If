# Task 1: Code Correction

# attendees = input("Enter number of attendees: ")
attendees = int (input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2: Venue Selection

# if there are less than 100 attendees the venue will be a conference room
# if there are 100 or more attendees the venue will be a large hall
# if there are 50 or less attendees you may need a projector
# if there are more than 50 attendees you may need an audio system
# if there are more than 100 attendees you may need both a projector and an audio system
# if there are 150 or more attendees you may need multiple projectors and an audio system


attendees = int (input("Enter number of attendees: "))

venue = "Large Hall" if attendees > 100 else "Conference Room"
print(venue)    
if attendees <= 50:
    additional_facilities = "a projector"
elif attendees >= 50:
    additional_facilities = "an audio system"
elif attendees == 100:
    additional_facilities = "both a projector and an audio system"
elif attendees >= 101 and attendees <= 150:
    additional_facilities = "both a projector and an audio system"
elif attendees >= 151:
    additional_facilities = "multiple projectors and an audio system"
print ("You may need", additional_facilities)


# Task 3: Catering Choices

caterer = "Veggie Delight Caterers" if input("Do you want vegetarian food? yes/no \n") == "yes" else "Gourmet Meals Caterers"
print("We recommend", caterer, "for your event.")
