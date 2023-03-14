import re


# function to get the degree of profanity of a comment
def profanity_degree(uid, stmt):
    # defining the base profanity degree of any comment and the slurs against which the comment will be compared
    degree = 1
    slurs = {'americoon', 'black', 'chimp', 'darkey', 'egg', 'frog', 'gringo', 'hillbilly', 'injun', 'jewtard', 'racist', 'white'}

    # obtaining the max. length and the min. length from all the slurs defined above
    maxx, minn = len(max(slurs, key=len)), len(min(slurs, key=len))
    
    # splitting the comment to obtain individual words and checking if the word is profane or not
    for word in stmt.split(" "):
        # converting the word to lowercase and removing all characters except letters
        word = word.lower()
        pure_word = re.sub("[^a-z]", "", word)
        l = len(pure_word)

        # using the length of the pure word to find whether such a word exist's as a slur or not
        if l >= minn and l <= maxx:
            if pure_word in slurs:
                # incrementing the degree of profanity if the word is identified as a slur
                degree += 1

                # the degree of profanity can also be multiplicative in nature rather than being additive
                # degree *= 2

    print(f'User: {uid} made a comment with a profanity degree of {degree}')


# opening the file which contains the tweets
file = open('Tweets.txt', 'r')

# iterating through each comment one by one and checking the comment's degree of profanity
for comments in file.readlines():
    # splitting the line in the file to separate the uid and the comment
    data = comments.split(',')
    profanity_degree(data[0], "".join(data[1:]))

# closing the opened file
file.close()
