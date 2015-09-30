Given(/^I am logged into the website$/) do
  visit(LoginPage).login_with(user, password, false)
end

Given(/^I am on the "(.+)" page$/) do |article|
  # Ensure we do not cause a redirect
  article = article.gsub(/ /, '_')
  visit(ArticlePage, using_params: { article_name: article })
end
