Given(/^I am logged into the website$/) do
	#LoginPage is defined in mediawiki-selenium
	visit(LoginPage).login_with(user, password)
end

When(/^I am on the "(.+)" page$/) do |article|
	# Ensure we do not cause a redirect
	article = article.gsub(/ /, '_')
	visit(ArticlePage, using_params: { article_name: article })
end

When(/^I am on a random page$/) do
	#RandomPage is defined in mediawiki-selenium
	visit(RandomPage)
end
