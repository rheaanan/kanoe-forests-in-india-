<?php 
	require 'connection.php';
	extract($_GET);
	$qry = "SELECT `Fore`,`Temperature`,`Rainfall`,`Population` FROM `table 1` WHERE Year = '$year' AND District = '$district'";
	$qryrun = mysql_query($qry) OR die(mysql_error());
	$rows = array();
	while($r = mysql_fetch_assoc($qryrun))
	{
		$rows[] = $r["Fore"];
		$rows[] = $r["Temperature"];
		$rows[] = $r["Rainfall"];
		$rows[] = $r["Population"];
	}
	echo json_encode($rows);
?>