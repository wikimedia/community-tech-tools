import MySQLdb
import random
from config import *

def main():

	wikis = ['ar', 'ru', 'en', 'fr', 'ja', 'de', 'commons', 'es', 'zh', 'pt']
	f1 = open( 'survey_bots.txt', 'w' )
	
	for wiki in wikis:
		db = MySQLdb.connect( host = wiki + 'wiki.labsdb', user = credentials['user'], passwd = credentials['pass'], db = wiki + 'wiki_p' )
		res = query( wiki, db )
		res = random.sample( res, 25 )
		f1.write( wiki + '\n' )
		for r in res:
			f1.write( r + '\n' )
		f1.write( '\n\n' )


def query( wiki, db ):
	cur = db.cursor()
	list1 = set()
	q = """SELECT rc_user, rc_user_text, COUNT(*) AS edits
		   FROM recentchanges
		   WHERE rc_bot = 1
		   GROUP by rc_user
		   ORDER BY edits DESC
		   LIMIT 100
		"""
	cur.execute( q )

	for row in cur.fetchall():
		list1.add( row[1] )

	print len( list1 )
	return list1

main()
