<?php
$num = $_POST['numero'];
 $f = fopen("numero.txt", "w+");
 fwrite($f,$num);
 fclose($f);
?>
