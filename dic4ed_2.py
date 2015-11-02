# The Best Dictionary in The World
# created in Sleepy Hollow NY  on October 28, 2015
# by Aneta Zolkiewicz for Edward Eames


print "You are the best in the world!\n"

world_best_dic = {'you are': "jestes", 'the best': "najlepsza", 'in': "na", 'the world': "swiecie"}


print world_best_dic['you are'], world_best_dic['the best'], world_best_dic['in'], world_best_dic['the world'] + "!\n"


print "Words to learn: \n"
 
for word in world_best_dic:
    print word, " - ", world_best_dic[word]

print " "

word_searched = raw_input("Edziu what word are you looking for? ")
for word in world_best_dic:
    if word_searched in world_best_dic:
        word = word_searched
        
        print word, " - ", world_best_dic[word]
        break
    else:
        print " Edziu the dictionary doesn't contain that word!"
        break
