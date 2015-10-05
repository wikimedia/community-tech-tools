class ArticlePage
	include PageObject

	page_url '<%=params[:article_name]%><%=params[:hash]%>'

	# UI elements
	a(:edit_link, text: 'Edit')
	span(:hotcat_link, class: 'hotcatlink')

	# pre-content
	h1(:first_heading, id: 'firstHeading')
end
