<?php

$con = mysqli_connect('localhost','root','1','scs');

$sql = "select * from people_data";

$records = mysqli_query($con, $sql);
	
?>

<html>
	<head>
		<title> Smart Community System </title>
	<head>

	<body>
	
	<table align = 'center' valign = 'center' width = "600" border = "1" cellpadding = "1" cellspacing = "1">
	
	<tr>
		<th> No </th>
		<th> People Entered </th>
		<th> Last Time of Entry </th>
		<th> People Exited </th>
		<th> Last Time of Exit </th>
		<th> Number of People in Hall </th>
	</tr>
	
	<?php
	
	while($data = mysqli_fetch_assoc($records)){
		
		echo "<tr>" ;
		
		echo "<td align = center>".$data['no']."</td>";
		echo "<td align = center>".$data['people_entered']."</td>";
		echo "<td align = center>".$data['time_of_entry']."</td>";
		echo "<td align = center>".$data['people_exited']."</td>";
		echo "<td align = center>".$data['time_of_exit']."</td>";
		echo "<td align = center>".$data['no_of_people']."</td>";
		
		echo "</tr>";
	}
	
	?>
	
	</table>
	
	</body>
	
</html>