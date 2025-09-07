# Define the story template with placeholders
story = "Once upon a time, a [adjective] [noun] went on a [adjective] adventure to a [place]. They met a [adjective] [animal] who taught them how to [verb] and [adverb] dance."

# Get user input for each placeholder
adjective1 = input ("Enter an adjective: ")
noun1 = input ("Enter a noun: ")
adjective2 = input ("Enter another adjective: ")
place1 = input ("Enter a place:  ")
adjective3 = input ("Enter a third adjective: ")
animal1 = input ("Enter an animal:  ")
verb1 = input ("Enter a verb:  ")
adverb1 = input ("Enter an adverb: ")

# Replace the placeholders with user input
filled_story = story.replace("[adjective]", adjective1, 1) # Replace first adjective
filled_story = filled_story.replace("[noun]", noun1, 1)
filled_story = filled_story.replace("[adjective]", adjective2, 1) # Replace second adjective
filled_story = filled_story.replace("[place]", place1, 1)
filled_story = filled_story.replace("[adjective]", adjective3, 1) # Replace third adjective
filled_story = filled_story.replace("[animal]", animal1, 1)
filled_story = filled_story.replace("[verb]", verb1, 1)
filled_story = filled_story.replace("[adverb]", adverb1, 1)

# Print the generated story
print("\nHere's your Mad Libs story:")
print(filled_story)
