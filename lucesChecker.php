<?php
include 'getconexion.php';
$query = "select * from luces";
$result = mysqli_query($mysqli,$query);
$sql = "DELETE FROM luces WHERE luz1='luce1e' or luz1='luce1a'";
mysqli_query($mysqli, $sql);
$sql = "DELETE FROM luces WHERE luz2='luce2e' or luz1='luce2a'";
mysqli_query($mysqli, $sql);
$titles = array();
$titles2 = array();
while($row = mysqli_fetch_array($result))
{
    $titles[] = $row['luz1'];
    $titles2[] = $row['luz2'];
}
$titlestring = implode("", $titles);
$titlestring2 = implode("", $titles2);
$var = "luce1a";
if (strcmp($titlestring, $var) !== 0) {
    $sql = "INSERT INTO luces (luz1) VALUES ('luce1e')";
    mysqli_query($mysqli, $sql);
    echo $titlestring;
}else{
    $sql = "INSERT INTO luces (luz1) VALUES ('luce1a')";
    mysqli_query($mysqli, $sql);
    echo $titlestring;
}
$var = "luce2a";
if (strcmp($titlestring, $var) !== 0){
    $sql = "INSERT INTO luces (luz2) VALUES ('luce2e')";
    mysqli_query($mysqli, $sql);
    echo $titlestring2;
}else{
    $sql = "INSERT INTO luces (luz2) VALUES ('luce2a')";
    mysqli_query($mysqli, $sql);
    echo $titlestring2;
}
?>
