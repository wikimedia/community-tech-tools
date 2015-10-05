Feature: HotCat

	Background:
		Given I am logged into the website

	Scenario: HotCat available
		When I am on the "Special:Preferences" page
		Then I should see a Gadgets tab
		When I click the Gadgets tab
		Then I should see a HotCat checkbox
		When I check the HotCat checkbox
		# This one isn't defined yet. Need to figure out how to deal with the save button being disabled
		When I save the preferences
		And I am on a random page
		Then I should see the HotCat UI
