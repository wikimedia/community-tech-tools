class ArticlePage
  include PageObject

  page_url '<%=params[:article_name]%><%=params[:hash]%>'

  # UI elements
  a(:edit_link, text: 'Edit')

  # pre-content
  h1(:first_heading, id: 'firstHeading')
end
