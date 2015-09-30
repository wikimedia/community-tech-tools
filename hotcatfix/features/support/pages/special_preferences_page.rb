class SpecialPreferencesPage < ArticlePage
	include PageObject

	page_url 'Special:Preferences'

	a(:gadgets_tab, id: 'preftab-gadgets')
	checkbox(:hotcat_checkbox, id: 'mw-input-wpgadgets-HotCat')
	button(:save_button, id: 'prefcontrol')
end
