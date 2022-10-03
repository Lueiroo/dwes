<html>
<body>
<h1>Jubilación</h1>
<?php
function edad_en_3_años($edad) {
	return $edad + 3;
}

function mensaje($age) {
	if (edad_en_3_años($age) > 65) {
		return "En 3 años tendrás edad de jubilación";
	} else {
		return "¡Disfruta de tu tiempo!";
	}
}?>

<table>
<tr>
<th>Edad</th>
<th>Info</th>
</tr>

<?php
$lista = array(60,61,62,63,64);
foreach ($lista as $aux) {
	echo "<tr>";
	echo "<td>".$aux."</td>";
	echo "<td>".mensaje($aux)."<td>";
	echo "</tr>";
}?>
</table>
</body>
</html>
