<?php
include 'getconexion.php';
$sql = "DELETE FROM luces WHERE luz2='luce2e' or luz2='luce1a'";
mysqli_query($mysqli, $sql);
$sql1 = "INSERT INTO luces (luz2) VALUES ('luce2a')";
mysqli_query($mysqli, $sql1);
echo "ok";
 ?>
