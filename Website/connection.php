<?php
$mysql_host = 'localhost';
$mysql_user = 'root';
$mysql_pass = '';
$mysql_db = 'kanoe';

$bd = mysql_connect($mysql_host, $mysql_user, $mysql_pass) or die("Could not connect database");
mysql_select_db($mysql_db, $bd) or die("Could not select database");

?>