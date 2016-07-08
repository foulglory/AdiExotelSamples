<?php
header('Content-Type:text/plain');
$from = $_GET['From']."\n";
$body = $_GET['Body'];
$fh = fopen("tmp/cfg.txt","a");
fwrite($fh,$from." ".$body);
fclose($fh);
$b = explode(" ",$body);

require("connect.php");

$sql = "INSERT INTO users (srno, name, number) VALUES (null, \"$b[1]\", \"$from\")";

if ($conn->query($sql) === TRUE) {
    echo "Registered successfully! ";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

echo "Welcome to Code for Good! You must be ".$b[1]." and your phone number is ".$from;
?>