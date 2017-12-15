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
		#customers tr:nth-child(even){background-color: #12a3bc;}
		#customers tr:hover {background-color: #ddd;}
		#customers th {
		    padding-top: 12px;
		    padding-bottom: 12px;
		    text-align: left;
		    background-color: #4CAF50;
		    color: white;
		}
		.bla2 {
			text-align: center;
		}
		.buttons{
			width: 100%;
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
		<section class="buttons">
			<td></td>
			<td class="bla2"><a href="/baeta"><h2>Bæta todo</h2></a></td>
			<td class="bla2"><a href="/eyda"><h2>eyda todo</h2></a></td>
			<td class="bla2"><a href="/breyta"><h2>breyta todo</h2></a></td>
			<td></td>
		</section>

	</table>
</body>
</html>
