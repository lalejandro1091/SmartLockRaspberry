<?php
include 'getconexion.php';
$sql = "DELETE FROM luces WHERE luz1='luce1e' or luz1='luce1a'";
mysqli_query($mysqli, $sql);
$sql1 = "INSERT INTO luces (luz1) VALUES ('luce1a')";
mysqli_query($mysqli, $sql1);
echo "ok";
 ?>
