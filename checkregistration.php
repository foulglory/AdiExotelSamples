<?php
header('Content-Type:text/plain');
$from = $_GET['From']."\n";
$body = $_GET['Body'];
$fh = fopen("tmp/cfg.txt","a");
fwrite($fh,$from." ".$body);
fclose($fh);
$b = explode(" ",$body);
 
require("connect.php");
 
$sql = "SELECT name FROM users WHERE number=\"$from\"";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    echo "We remember you! ";
    $row = $result->fetch_assoc();
    $name = $row["name"];
    echo "Welcome to Code for Good! You must be ".$name." and your phone number is ".$from;

} else {
    echo "Your earlier registration SMS has not worked! Please try again. ";
}
 

?>		