Then(/^I should see the HotCat UI$/) do
	sleep 5		# The gadget loads a few seconds later
	expect(on(ArticlePage).hotcat_link_element).to be_visible
end
