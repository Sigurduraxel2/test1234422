<!DOCTYPE html>
<html>
<head>
	<title>Forsíða</title>
	<style>
		#customers {
		    font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
		    border-collapse: collapse;
		    width: 100%;
		}
		#customers td, #customers th {
		    border: 1px solid #ddd;
		    padding: 8px;
		}
		#customers tr:nth-child(even){background-color: #f2f2f2;}
		#customers tr:hover {background-color: #ddd;}
		#customers th {
		    padding-top: 12px;
		    padding-bottom: 12px;
		    text-align: left;
		    background-color: #4CAF50;
		    color: white;
		}
		.breyta {
			text-align: center;
		}
	</style>
</head>
<body>
	<h1>Todo listinn minn</h1>
	<table id="customers">
	  <tr>
	    <th>ID</th>
	    <th>info</th>
	    <th>Staða</th>
	  </tr>

	%	for row in cur:	
		  <tr>
		    <td>{{row[0]}}</td>
		    <td>{{row[1]}}</td>
		    <td>{{row[2]}}</td>
		  </tr>
	% end
		<td></td>
		<td class="breyta"><a href="/baeta"><h2>Breyta</h2></a></td>
		<td></td>

	</table>
</body>
</html>
