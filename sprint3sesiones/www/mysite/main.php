<html>
	<head>
		<style>
			table{
			    border-collapse: collapse;
			}

			td, th{
			    border: 1px solid black;
			    color: white;
			    background-color: sienna;
			}

			td:hover{
			    color: red;
			    background-color: burlywood;
			}

			img{
			    width: 250px;
			    height: 250px;
			    transition: 1s linear;
			}

			img:hover{
			    width: 1000px;
			    height:50px;
			}

    		</style>
	</head>
	<body>
		<?php
			$db = mysqli_connect('172.16.0.1', 'root', '1234', 'mysitedb') or die('Fail');
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
		<br><a href="/contrasena.html">Cambiar contraseña</a>
	</body>
</html>
