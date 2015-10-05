from time import mktime
from datetime import datetime
import re
import time

def main():
	fa = open( 'hits.txt' )
	final = open( 'automate_bash.sh', 'w' )
	final.write( 'export MEDIAWIKI_USER="Community Tech bot"\n' )
	final.write( 'export MEDIAWIKI_PASSWORD=\n\n' ) # Bot password goes here

	for l in fa:
		site = map(str, l.split('\t'))[0]
		res = findch( site )
		host = str(res[0])
		url = str(res[1])

		if res > 0:
			website = host + '.' + url + '.org'
			final.write( 'printf ' + website + '\n' )
			final.write( 'export MEDIAWIKI_URL=http://' + website + '/wiki/\n' )
			final.write( 'bundle exec cucumber\n\n' )
			

def findch( site ):
	if site.find('wikinews') > 0:
		return [ site[0:site.find( 'wikinews' )], site[site.find('wikinews'):] ]
	elif site.find('wikibooks') > 0:
		return [ site[0:site.find( 'wikibooks' )], site[site.find('wikibooks'):] ]
	elif site.find('wikiquote') > 0:
		return [ site[0:site.find( 'wikiquote' )], site[site.find('wikiquote'):] ]
	elif site.find('comm') > 0:
		return [ 'commons', 'wikimedia' ]
	elif site.find('wikisource') > 0:
		return [ site[0:site.find( 'wikisource' )], site[site.find('wikisource'):] ]
	elif site.find('wikiversity') > 0:
		return [ site[0:site.find( 'wikiversity' )], site[site.find('wikiversity'):] ]
	elif site.find('wiktionary') > 0:
		return [ site[0:site.find( 'wiktionary' )], site[site.find('wiktionary'):] ]
	elif site.find('wikivoyage') > 0:
		return [ site[0:site.find( 'wikivoyage' )], site[site.find('wikivoyage'):] ]
	elif site.find('wikimedia') > 0:
		return [ site[0:site.find( 'wikimedia' )], site[site.find('wikimedia'):] ]
	elif site.find('mania') > 0:
		return [ site[0:13], 'wikimedia' ]
	elif site.find('meta') > 0:
		return [ 'meta', 'wikimedia' ]
	elif site.find('strategy') > 0:
		return [ 'strategy', 'wikimedia' ]
	elif site.find('incubator') > 0:
		return [ 'incubator', 'wikimedia' ]
	elif site.find('outreach') > 0:
		return [ 'outreach', 'wikimedia' ]
	elif site.find('wiki') > 0:
		return [ site[0:site.find('wiki')], 'wikipedia' ]
	else:
		return [ -1, -1 ]

if __name__ == '__main__':
	main()
