Then(/^I should see the HotCat UI$/) do
	expect(on(ArticlePage).hotcat_link_element).to be_visible
end
