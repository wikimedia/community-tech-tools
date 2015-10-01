Then(/^I should see a Gadgets tab$/) do
	expect(on(SpecialPreferencesPage).gadgets_tab_element).to be_visible
end

When(/^I click the Gadgets tab$/) do
	on(SpecialPreferencesPage).gadgets_tab_element.when_present.click
end

Then(/^I should see a HotCat checkbox$/) do
	expect(on(SpecialPreferencesPage).hotcat_checkbox_element).to be_visible
end

When(/^I check the HotCat checkbox$/) do
	on(SpecialPreferencesPage).hotcat_checkbox_element.when_present.set(true)
end
