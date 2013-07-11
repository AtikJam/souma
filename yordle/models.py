from web_ui import app, db, notification_signals
from web_ui.helpers import get_active_persona

class Word(Serializable, db.Model):
	__tablename__ = "words"
	id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
	persona = db.Column(db.String(32), db.ForeignKey('persona.id'), primary_key=True, nullable=False, autoincrement=False)
	word = db.Column(db.String(32))
	collection_id = db.Column(db.Integer, db.ForeignKey('word_collections.id'))

	def create_word():
		pass

class Word_Collection(Serializable, db.Model):
	__tablename__ = "word_collections"
	id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
	persona = db.Column(db.String(32), db.ForeignKey('persona.id'), primary_key=True, nullable=False, autoincrement=False)

	def create_collection():
		pass

	def update_counts(tags, counts):
		pass

	def get_counts(tags):
		pass

	def add_word(word):
		pass

	def get_words():
		pass

class Word_under_Tag_Count(Serializable, db.Model):
	__tablename__ = "word_under_tag_counts"
    id = db.Column(db.Integer, primary_key=True)
    persona = db.Column(db.String(32), db.ForeignKey('persona.id'), primary_key=True, nullable=False, autoincrement=False)
    collection_id = db.Column(db.Integer, db.ForeignKey('word_collections.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))
    count = db.Column(db.Integer)

class Tag(Serializable, db.Model):
	__tablename__ = "tags"
	id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
	persona = db.Column(db.String(32), db.ForeignKey('persona.id'), primary_key=True, nullable=False, autoincrement=False)
	word_collection_id = db.Column(db.Integer, db.ForeignKey('word_collections.id'))
	count = db.Column(db.Integer)

	def create_tag():
		pass

	def update_count(count):
		pass

	def get_count():
		pass

class Naive_Bayes_Model(Serializable, db.Model):
	__tablename__ = "naive_bayes_model"
	id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
	persona = db.Column(db.String(32), db.ForeignKey('persona.id'), primary_key=True, nullable=False, autoincrement=False)
	model = db.Column(db.PickleType)