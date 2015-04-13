<?php
	$params = "";

	$url =  $_GET['url'];
	$depth = $_GET['depth'];

	if($url!=""){
		$params .= "--url " . $url;
	}
	if($depth >= 0){
		$params .= " --spider " . $depth;
	}
	if(isset($_GET['xss'])){
		$params .= " --xss";
	}
	if(isset($_GET['sql'])){
		$params .= " --sql";
	}
	if(isset($_GET['javascript'])){
		$params .= " --javascript";
	}
	if(isset($_GET['bsql'])){
		$params .= " --bsql";
	}


	echo exec('whoami');
	if($params != ""){
		echo "Starting Grabber";
		$output = shell_exec("python grabber.py ".$params);
		print_r($output);
	}
	else{
		echo "Invalid Params";
	}
?>