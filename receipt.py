import cgi
fm = cgi.FieldStorage()
name = fm.getvalue("name")
email = fm.getvalue("email")
phone = fm.getvalue("phone")
delivdate = fm.getvalue("deliverydate")
gender = fm.getvalue("gender")
shippingaddress = fm.getvalue("shippingaddress")
city = fm.getvalue("city")
province = fm.getvalue("province")
country = fm.getvalue("country")
zipcode = fm.getvalue("zipcode")
riflequantity = fm.getvalue("quantity1")
canonquantity = fm.getvalue("quantity2")
sniperquantity = fm.getvalue("quantity3")
pistolquantity = fm.getvalue("quantity4")
riflebaseprice = 20000
canonbaseprice = 30000
sniperbaseprice = 18000
pistolbaseprice = 10000
import datetime
time=datetime.datetime.now()

import random
invoicenum = random.randint(100000, 999999)


r = riflebaseprice*int(riflequantity)
c = canonbaseprice*int(canonquantity)
s = sniperbaseprice*int(sniperquantity)
p = pistolbaseprice*int(pistolquantity)
pricelist = [r,c,s,p]

rifleprice = ("%s" %r)
canonprice = ("%s" %c)
sniperprice = ("%s" %s)
pistolprice = ("%s" %p)

str="Content-type: text/html"
print(str)
print()

import html5function
omarkup = html5function.opening_markup('receipt','Galactic Trade Market', 'style.css')
cmarkup = html5function.closing_markup()

print(omarkup)
markup = """
<nav>
	<a href="Home.html">Home</a>
	<a href="Form.html">Arsenal</a>
	<a href="Form.html">Links</a>
	<a href="Form.html">Contact Us</a>
</nav>
<br/>
<main>
"""
print(markup)
if (riflequantity == 0 and canonquantity == 0 and sniperquantity == 0 and pistolquantity == 0):
    print('<p> Please input the amount of weapons you wish to purchase </p>')
else:
    print('<p> Invoice number:')
    print(invoicenum)
    print('</p>')
    print('<address>')
    if(gender == 'mr'):
        print('Mr.'+ name + '<br/>' + shippingaddress + '<br/>' + city +', ' + province+', ' + country + ', ' + zipcode + '</address>')
    elif(gender == 'mrs'):
        print('Mrs.'+ name + '<br/>' + shippingaddress + '<br/>' + city +', ' + province+', ' + country + ', ' + zipcode + '</address>')
    elif(gender == 'ms'):
        print('Ms.' + name + '<br/>' + shippingaddress + '<br/>' + city +', ' + province+', ' + country + ', ' + zipcode + '</address>')
    print('<p>')
    print(time)
    print('</p>')
    if(riflequantity == 0):
        markup += """
<table>
    <thead>
        <tr>
            <th> Item </th>
            <th> Quantity </th>
            <th> Price </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> R-110 Pulse-Wave Saboteur Assault Cannon </td>
            <td>
"""
        markup += canonquantity
        markup += """</td>
<td>
"""
        markup += canonprice
        markup += """ </td>
</tr>
        <tr>
            <td> R-55 Searing Disruptor Sniper Rifle </td>
            <td>
"""
        markup += sniperquantity
        markup += """</td>
<td>
"""
        markup += sniperprice
        markup += """ </td>
</tr>
        <tr>
            <td> A-300 Heavy Sonic Needler Blaster Pistol </td>
            <td>
"""
        markup += pistolquantity
        markup += """</td>
<td>
"""
        markup += pistolprice
        markup += """ </td>
</tr>
        <tr>
            <td colspan = "2"> Tax </td>
            <td>
"""
        total = (sum(pricelist))
        tx = total*0.07
        tax = ("%s" %tx)
        markup += tax
        markup += """ </td>
</tr>
        <tr>
            <td colspan = "2"> Total </td>
            <td>
"""
        total *= 1.07
        totalcost = ("%s" %total)
        markup += totalcost
        markup += """</td>
</tr>
"""

    elif(canonquantity == 0):
        markup = """
<table>
    <thead>
        <tr>
            <th> Item </th>
            <th> Quantity </th>
            <th> Price </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> Renegade Interceptor Blaster Rifle </td>
            <td>
"""
        markup += riflequantity
        markup += """</td>
<td>
"""
        markup += rifleprice
        markup += """ </td>
</tr>
        <tr>
            <td> R-55 Searing Disruptor Sniper Rifle </td>
            <td>
"""
        markup += sniperquantity
        markup += """</td>
<td>
"""
        markup += sniperprice
        markup += """ </td>
</tr>
        <tr>
            <td> A-300 Heavy Sonic Needler Blaster Pistol </td>
            <td>
"""
        markup += pistolquantity
        markup += """</td>
<td>
"""
        markup += pistolprice
        markup += """ </td>
</tr>
        <tr>
            <td colspan = "2"> Tax </td>
            <td>
"""
        total = (sum(pricelist))
        tx = total*0.07
        tax = ("%s" %tx)
        markup += tax
        markup += """ </td>
</tr>
        <tr>
            <td colspan = "2"> Total </td>
            <td>
"""
        total *= 1.07
        totalcost = ("%s" %total)
        markup += totalcost
        markup += """</td>
</tr>
"""

    elif(sniperquantity == 0):
        markup = """
<table>
    <thead>
        <tr>
            <th> Item </th>
            <th> Quantity </th>
            <th> Price </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> R-110 Pulse-Wave Saboteur Assault Cannon </td>
            <td>
"""
        markup += canonquantity
        markup += """</td>
<td>
"""
        markup += canonprice
        markup += """ </td>
</tr>
        <tr>
            <td> Renegade Interceptor Blaster Rifle </td>
            <td>
"""
        markup += riflequantity
        markup += """</td>
<td>
"""
        markup += rifleprice
        markup += """ </td>
</tr>
        <tr>
            <td> A-300 Heavy Sonic Needler Blaster Pistol </td>
            <td>
"""
        markup += pistolquantity
        markup += """</td>
<td>
"""
        markup += pistolprice
        markup += """ </td>
</tr>
        <tr>
            <td colspan = "2"> Tax </td>
            <td>
"""
        total = (sum(pricelist))
        tx = total*0.07
        tax = ("%s" %tx)
        markup += tax
        markup += """ </td>
</tr>
        <tr>
            <td colspan = "2"> Total </td>
            <td>
"""
        total *= 1.07
        totalcost = ("%s" %total)
        markup += totalcost
        markup += """</td>
</tr>
"""
    elif(pistolquantity == 0):
        markup = """
<table>
    <thead>
        <tr>
            <th> Item </th>
            <th> Quantity </th>
            <th> Price </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> R-110 Pulse-Wave Saboteur Assault Cannon </td>
            <td>
"""
        markup += canonquantity
        markup += """</td>
<td>
"""
        markup += canonprice
        markup += """ </td>
</tr>
        <tr>
            <td> R-55 Searing Disruptor Sniper Rifle </td>
            <td>
"""
        markup += sniperquantity
        markup += """</td>
<td>
"""
        markup += sniperprice
        markup += """ </td>
</tr>
        <tr>
            <td> Renegade Interceptor Blaster Rifle </td>
            <td>
"""
        markup += riflequantity
        markup += """</td>
<td>
"""
        markup += rifleprice
        markup += """ </td>
</tr>
        <tr>
            <td colspan = "2"> Tax </td>
            <td>
"""
        total = (sum(pricelist))
        tx = total*0.07
        tax = ("%s" %tx)
        markup += tax
        markup += """ </td>
</tr>
        <tr>
            <td colspan = "2"> Total </td>
            <td>
"""
        total *= 1.07
        totalcost = ("%s" %total)
        markup += totalcost
        markup += """</td>
</tr>
"""
    else:
        markup = """
<table>
    <thead>
        <tr>
            <th> Item </th>
            <th> Quantity </th>
            <th> Price </th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td> Renegade Interceptor Blaster Rifle </td>
            <td>
"""
        markup += riflequantity
        markup += """</td>
<td>
"""
        markup += rifleprice
        markup += """ </td>
</tr>
<tr>
            <td> R-110 Pulse-Wave Saboteur Assault Cannon </td>
            <td>
"""
        markup += canonquantity
        markup += """</td>
<td>
"""
        markup += canonprice
        markup += """ </td>
</tr>
<tr>
            <td> R-55 Searing Disruptor Sniper Rifle </td>
            <td>
"""
        markup += sniperquantity
        markup += """</td>
<td>
"""
        markup += sniperprice
        markup += """ </td>
</tr>
<tr>
            <td> A-300 Heavy Sonic Needler Blaster Pistol </td>
            <td>
"""
        markup += pistolquantity
        markup += """</td>
<td>
"""
        markup += pistolprice
        markup += """ </td>
</tr>
<tr>
        <td colspan = "2"> Tax </td>
        <td>
"""
        total = (sum(pricelist))
        tx = total*0.07
        tax = ("%s" %tx)
        markup += tax
        markup += """ </td>
</tr>
        <tr>
            <td colspan = "2"> Total </td>
            <td>
"""
        total *= 1.07
        totalcost = ("%s" %total)
        markup += totalcost
        markup += """</td>
</tr>
</table>
"""
markup += """
<form action="process.py">
<p>
    <select name="choice">
	<option value="Confirm">Confirm</option>
	<option value="Cancel">Cancel</option>
    </select>
</p>
<p> <input type="submit" name="action" value="Proceed" autofocus></p>
</form>
<br/>
</main>
"""
print(markup)
print(cmarkup)
