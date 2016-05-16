<?php

$mysql_hostname = "localhost";
$mysql_user = "root";
$mysql_password = "trevize1";
$mysql_database = "luces";
$prefix = "";
$mysqli = mysqli_connect($mysql_hostname, $mysql_user, $mysql_password,$mysql_database) or die("Could not connect database");

?>