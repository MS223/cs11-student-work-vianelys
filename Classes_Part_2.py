class Song(object):

    def __init__(self, lyrics, title, author):
        self.lyrics = lyrics
        self.title = title

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

peace_and_love = Song(["Life and death and love and birth,",
                   "And peace and war on the planet Earth.",
                   "Is there anything that's worth more"

                       ])

hotline_bling = Song(["You used to call me on my",
                      "You used to, you used to",
                      "Yeah",])
# This is your daily reminder that Drake is Canadian

happy_bday.sing_me_a_song()
hotline_bling.sing_me_a_song()

#
