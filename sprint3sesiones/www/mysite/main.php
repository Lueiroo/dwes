//prueba por favor que funcione
<html>
	<body>
		<?php
			$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
		?>
		<?php
			$query =  "SELECT * FROM tCanciones";
			$result = mysqli_query($db, $query) or die('Query error');
			echo"<table>";
			echo"<tr>";
				echo"<th>ID</th>";
				echo"<th>Nombre</th>";
				echo"<th>URL</th>";
				echo"<th>Autoría</th>";
				echo"<th>Fecha de publicación</th>";
			echo"</tr>";
			while ($row = mysqli_fetch_array($result)) {
				echo"<tr>";
					echo"<td>".$row[0]."</td>";
					echo"<td>" .$row[1]."</td>";
					echo'<td><img src="/Imágenes/'.$row[2];
						echo'"></td>';
					echo"<td>" .$row[3]."</td>";
					echo"<td>".$row[4]."</td>";
				echo"</tr>";
			}
			echo"</table>";
			mysqli_close($db);
			?>

		<br><br><a href="/logout.php">Si por lo que sea quieres cerrar sesión clícale aquí</a>

	</body>
</html>
