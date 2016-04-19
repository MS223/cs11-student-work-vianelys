a = [1, 2, 4]
b = a
# B does not a because b is equal to a so theere will be no change.

# input: a list of ints
# output: an int
def update_list(a_list):
    a_list[3] = "yo"
    b = a_list[4]
    b = 100
my_list = [1, 2, 3, 4, 5]
update_list(my_list)
print my_list
# my_list will print out as [1,2,3,yo,5]
# I was right!

var_1 = "kittens" #global
var_2 = "cookies" #global
# input: a string
# output: a string
def my_function(my_favorite_things): #global
    song_lyrics = "rain drops on roses," #local
    combined_song = song_lyrics + my_favorite_things #local
    return combined_song #local
# input: a string
# output: a string
def my_function_2(item, item2):
    full_lyrics = item + "on " + item2 #local
    full_song = my_function(full_lyrics) #local
    return full_song #local
my_song = my_function_2(var_1, var_2) #local

var_1 = 'cat'
var_2 = 'dog'

def print_out_my_favorite(favorite_pet):
    if favorite_pet == var_1:
        print("My favorite pet is the cat.")
    if favorite_pet == var_2:
        print("My favorite pet is the dog.")
    var_2 = "cat" #delete this.

print_out_my_favorite(var_1)
print(var_2)

my_num = 3
