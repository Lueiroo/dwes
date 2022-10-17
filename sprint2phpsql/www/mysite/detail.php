<html>
	<body>
		<?php
			$db = mysqli_connect('localhost', 'root', '1234', 'mysitedb') or die('Fail');
		?>
		<h1>Conexión establecida</h1>
		<?php
			if (!isset($_GET['cancion_id'])) {
				die('No se ha especificado una canción');
			}
			$cancion_id = $_GET['cancion_id'];
			$query = 'SELECT * FROM tCanciones WHERE id='.$cancion_id;
			$result = mysqli_query($db, $query) or die('Query error2');
			$only_row = mysqli_fetch_array($result);
			echo '<h1>'.$only_row[1].'</h1>';
			echo '<img src="/Imágenes/'.$only_row[2];
				echo'">';
			echo '<h2>'.$only_row[3].'</h2>';
			echo '<h2>'.$only_row[4].'</h2>';
			echo '<br><br><h3>Comentarios: </h3>';
			echo '<ul>';
			$query_2 = 'SELECT * FROM tComentarios WHERE cancion_id='.$cancion_id;
			$result_2 = mysqli_query($db, $query_2) or die('Query error2');
			while ($row = mysqli_fetch_array($result_2)) {
				echo '<li>'.$row['comentario'].'</li>';
			}
			mysqli_close($db);
			echo '</ul>';
		?>

		<p>Deja un nuevo comentario: </p>
		<form action="/comment.php" method="post">
			<textarea rows="4" cols="50" name="new_comment"></textarea><br>
		<input type="hidden" name="cancion_id" value="<?php echo $cancion_id; ?>">
			<input type="submit" value="Comentar">
		</form>
	</body>
</html>
