# quotestagram.py
# the best quote-sharing service
class Quote(object):
	def __init__(self, quote_text, user_posted, location, num_likes):
		self.quote_text = quote_text
		self.user_posted = user_posted
		self.location = location
		self.num_likes = num_likes
	# adds one 'like' count
	def like(self):
		self.num_likes = self.num_likes + 1 
	# takes one away from the 'like' count
	def un_like(self):
		self.num_likes = self.num_likes - 1
	# prints the full quote 
	def show_quote(self):
		print("U:" +self.user_posted)
		print("L:" + self.location)
		print("Quote:" + self.quote_text)
		print("Likes:" + str(self.num_likes))
# add some quotes
x = Quote("Nothing with Shawn.", "kevin_is_kool", "san francisco", 0)
y = Quote("I'm kool.", "truue_fosho", "CS class", 0)
z = Quote("Sergio is raw.", "savage_19", "CS class", 0)
# print our quotes 
z.show_quote()
# put quotes in a list
my_quotes = []
my_quotes.append(x)
my_quotes.append(y)
my_quotes.append(z)
user_quote = "Hello. How are you?"
speaker = "Adele"
location = "London"
my_quotes.append(Quote(user_quote, speaker, location, 0))
# call our show_quote function for all of our Quote objects
for q in my_quotes:
	q.show_quote()

