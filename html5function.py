def opening_markup(title_str, header_str, css_str):
	if (title_str == ''):
	    title_str= 'A dynamically generated webpage' 
	markup="""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>""" 
	markup += title_str 
	markup += """</title>
""" 
	if (css_str != '' or not css_str):
		markup += '<link rel="stylesheet" type="text/css" title="Default" media="all" href="' + css_str + '"/>'
	markup += """
</head>
<body>
<header>
<h1> """ 
	markup += header_str + "</h1></header>" 
	return markup


def closing_markup(): 
	markup2="""</body></html>""" 
	return markup2
	


