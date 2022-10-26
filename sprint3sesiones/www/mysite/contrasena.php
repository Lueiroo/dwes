<?php
    $db = mysqli_connect('localhost','root','1234','mysitedb') or die('Fail');

    $ant = $_POST['cont_antigua'];
    $nueva_1 = $_POST['cont_nueva_1'];
    $nueva_2 = $_POST['cont_nueva_2'];

    session_start();
    $user = $_SESSION['user_id'];
    $query = 'SELECT contraseña FROM tUsuarios WHERE id ="'.$user.'"';
    $result = mysqli_query($db, $query) or die('Error');
    $only_row = mysqli_fetch_array($result);

    if ($ant == $only_row[0]) {
        if($nueva_1 == $nueva_2){
            $query_2 = 'UPDATE tUsuarios SET contraseña = "'.$nueva_1.'" WHERE id = "'.$user.'"';
	    mysqli_query($db, $query_2) or die ('Error2');
            echo '<p>Contraseña cambiada correctamente</p>';
            header('Location: main.php');
        } else {
            echo '<p>Las nuevas contraseñas no coinciden</p>';
            header('Location: main.php');
        }
    } else {
        echo '<p>Contraseña antigua incorrecta</p>';
        header('Location: main.php');
    }
    mysqli_close($db);
?>
